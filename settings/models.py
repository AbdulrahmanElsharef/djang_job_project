from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _# Create your models here.
from django.utils import timezone


class Company(models.Model):
    name=models.CharField(_("name"), max_length=30)
    slogan=models.CharField(_("slogan"), max_length=100)
    logo=models.CharField(_("icon"), max_length=50)
    about=models.TextField(_("about_us"),max_length=1000)
    about_image=models.ImageField(_("about_image"), upload_to='company')
    vision=models.TextField(_("vision"),max_length=1000)
    work_days=models.CharField(_("work_days"), max_length=250)
    phones=models.CharField(_("phones"), max_length=300)
    emails=models.CharField(_("emails"), max_length=300)
    Fb_link=models.CharField(_("facebook"), max_length=100)
    Gm_link=models.CharField(_("gmail"), max_length=100)
    Tw_link=models.CharField(_("twitter"), max_length=100)
    Yb_link=models.CharField(_("youtube"), max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Company'

