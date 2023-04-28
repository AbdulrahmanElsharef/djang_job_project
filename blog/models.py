from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django.utils import timezone
from board.models import Category
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    author= models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title=models.CharField(_("title"), max_length=100)
    subtitle=models.CharField(_("subtitle"), max_length=250)
    image=models.ImageField( upload_to='posts')
    published_at=models.DateTimeField(_("published_at"), default=timezone.now)
    category=models.ForeignKey(Category,related_name='post_Category', on_delete=models.SET_NULL,null=True,blank=True)
    article=models.TextField(_("article"),max_length=5000)
    tag=TaggableManager()
    slug=models.SlugField(_("slug"),null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs) # Call the real save() method
    
class Review(models.Model):
    post=models.ForeignKey(Post, verbose_name=_("post"),related_name='post_review', on_delete=models.CASCADE)
    author=models.ForeignKey(User, related_name='review_author', on_delete=models.SET_NULL,null=True,blank=True)
    date=models.DateTimeField(_("date"),default=timezone.now)
    review=models.TextField(_("review"),max_length=2000)