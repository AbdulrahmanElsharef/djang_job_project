from django.contrib import admin

# Register your models here.
from .models import Category,Job_Company,Job,Candidates


admin.site.register(Category)
@admin.register(Job)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('title', 'company','category')
    list_filter=('job_type','salary', 'company','category')
    search_fields=('title','description','category')
admin.site.register(Job_Company)
admin.site.register(Candidates)