from django.contrib import admin


# Register your models here.
from .models import Job, category, Apply_job


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'published_at']
    list_filter = ['category', 'experience']
    search_fields = ['title', 'description']


class ApplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'Apply_at']


admin.site.register(Job, JobAdmin)
admin.site.register(category)
admin.site.register(Apply_job, ApplyAdmin)
