from django.contrib import admin

from Job_portalApp.models import Jobs, Application


@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title','company','location','salary','description','skills_required','job_type','created_at')
    search_fields = ('title','company','location')
    list_filter = ('job_type','created_at')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user','job','status','applied_at')
    list_filter = ('status','applied_at')
    search_fields = ('user__username','job__title')


