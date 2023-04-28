from django.contrib import admin
from .models import Post,Review
# Register your models here.

admin.site.register(Post)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('author','title','category')
    list_filter=('published_at','category')
    search_fields=('title','subtitle','article')
admin.site.register(Review)