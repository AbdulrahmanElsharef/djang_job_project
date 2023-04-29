from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name=models.CharField(_("name"), max_length=50)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category, self).save(*args, **kwargs) # Call the real save() method
    
class Job_Company(models.Model):
    name=models.CharField(_("name"), max_length=50)
    icon=models.CharField(_("icon"), max_length=50,default='logo.png')
    Fb_link=models.CharField(_("facebook"), max_length=100)
    Gm_link=models.CharField(_("gmail"), max_length=100)
    Tw_link=models.CharField(_("twitter"), max_length=100)
    Yb_link=models.CharField(_("youtube"), max_length=100)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Job_Company, self).save(*args, **kwargs) # Call the real save() method
    
    
JOB_TYPE=(('Full_Time','Full_Time'),('Part_Time','Part_Time'),('Remotely','Remotely'))

class Job(models.Model):
    author=models.ForeignKey(User, verbose_name=_("author"), on_delete=models.SET_NULL,null=True,blank=True,related_name='job_author')
    title=models.CharField(_("title"), max_length=100)
    image=models.ImageField(_("image"), upload_to='job')
    location=models.CharField(_("location"), max_length=200)
    company=models.ForeignKey(Job_Company, verbose_name=_("Company"), on_delete=models.SET_NULL,related_name='job_company',null=True,blank=True)
    category=models.ForeignKey(Category, verbose_name=_("Company"), on_delete=models.CASCADE,related_name='job_category')
    job_type=models.CharField(_("job_type"), max_length=50,choices=JOB_TYPE)
    published_at=models.DateTimeField(_("published_at"), default=timezone.now)
    vacancy=models.IntegerField(_("vacancy"))
    salary=models.IntegerField(_("salary"))
    description=models.TextField(_("description"),max_length=2500)
    Qualification=models.TextField(_("description"),max_length=2500)
    Responsibility=models.TextField(_("Responsibility"),max_length=2500)
    Benefits=models.TextField(_("Benefits"),max_length=2500)
    slug=models.SlugField(_("slug"),null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Job, self).save(*args, **kwargs) # Call the real save() method
    
    
class Candidates(models.Model):
    job=models.ForeignKey(Job, related_name='job_Candidates', on_delete=models.CASCADE)
    name=models.CharField(_("name"), max_length=100)
    email=models.CharField(_("email"), max_length=100)
    image=models.ImageField(_("image"), upload_to='Candidates')
    linkedin=models.URLField(_("linkedin"), max_length=100)
    cv=models.FileField(_("cv"), upload_to='cv', max_length=200)
    cover=models.TextField(_("cover"),max_length=1000)
    applied_at=models.DateTimeField(_("applied_at"), default=timezone.now)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Candidates'