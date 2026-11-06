from django.urls import path

from Job_portalApp import views

urlpatterns = [
    path('',views.jobs_view, name='jobs'),

    path('register/',views.registration_view, name='register'),

    path('login/',views.login_view, name='login'),

    path('logout/',views.logout_view, name='logout'),

    path('<int:pk>/apply/',views.apply_job_view, name='apply'),

    path('create/',views.create_view, name='create'),
]