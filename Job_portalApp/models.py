from django.contrib.auth.models import User
from django.db import models

class Jobs(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    description=models.TextField()
    skills_required=models.CharField(max_length=100)
    job_type=models.CharField(max_length=100,default='Full-time')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),

    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    resume=models.FileField(upload_to='resumes/')
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='Applied')
    applied_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.job}'
    class Meta:
        unique_together = ('user','job')


