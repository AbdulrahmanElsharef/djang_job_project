from django.contrib import admin

# Register your models here.
from .models import Category,Job,Candidate


admin.site.register(Category)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ('title', 'company','category')
#     list_filter=('job_type','salary', 'company','category')
#     search_fields=('title','description','category')
admin.site.register(Job)
admin.site.register(Candidate)