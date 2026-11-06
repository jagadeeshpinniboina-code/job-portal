from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages

from Job_portalApp.forms import RegistrationForm,JobApplicationForm,JobForm
from Job_portalApp.models import Jobs,Application
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from Job_portalApp.form1 import LoginForm

@login_required(login_url='/app/login/')
def jobs_view(request):
    jobs = Jobs.objects.all().order_by('-created_at')
    keyword=request.GET.get('keyword')
    location=request.GET.get('location')
    job_type=request.GET.get('job_type')

    if keyword:
        jobs = (Jobs.objects.filter(title__icontains=keyword)|
                Jobs.objects.filter(company__icontains=keyword)|
                Jobs.objects.filter(skills_required__icontains=keyword))
    if location:
        jobs = (Jobs.objects.filter(location__icontains=keyword))
    if job_type:
        jobs = (Jobs.objects.filter(job_type=job_type))

    context={
        'jobs':jobs,
        'keyword':keyword,
        'location':location,
        'job_type':job_type,
    }
    return render(request,'jobs.html',context)





def registration_view(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            messages.success(
                request,
                f'Account created successfully for {username}'
            )

            return redirect('login')

        else:

            username = form.cleaned_data.get('username')

            messages.error(
                request,
                f'Account could not be created for {username}'
            )

    else:

        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)

def login_view(request):
        if request.method == 'POST':

            form1 = LoginForm(request.POST)

            if form1.is_valid():

                username = form1.cleaned_data['username']
                password = form1.cleaned_data['password']

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if user is not None:
                    login(request, user)

                    next_url = request.GET.get('next')

                    if next_url:
                        return redirect(next_url)

                    return redirect('jobs')

        else:
            form1 = LoginForm()
            context = {
                'form1': form1
            }

            return render(request, 'login.html', context)
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url='/app/login/')
def apply_job_view(request, pk):

    job = get_object_or_404(Jobs, id=pk)

    already_applied = Application.objects.filter(
        job=job,
        user=request.user
    ).exists()

    if already_applied:
        messages.warning(
            request,
            'You already applied for this job.'
        )
        return redirect('jobs')

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()

            messages.success(
                request,
                'Your application submitted successfully!'
            )

            return redirect('jobs')

        else:
            messages.error(
                request,
                'Please correct the errors below.'
            )

    else:
        form = JobApplicationForm()
        context = {
            'form': form,
            'job': job,
        }
        return render(request, 'apply_job.html', context)

@login_required(login_url='/app/login/')
@user_passes_test(lambda user: user.is_staff,login_url='/app/')
def create_view(request):
    if request.method == 'POST':
        form=JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            context={
                'form':form
            }
            return render(request,'create.html',context)
    else:
        form=JobForm()
        context={
            'form':form
        }
        return render(request,'create.html',context)
