from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _  # Create your models here.
from django.utils import timezone
from utils.generate_code import generate_code
from django.urls import reverse


# Create your models here.
class Employer(models.Model):
    name = models.CharField(_("name"), max_length=100)
    industry = models.CharField(_("Industry"), max_length=250)
    icon = models.CharField(_("icon"), max_length=50)
    founded = models.DateField(_("founded"), auto_now=False, auto_now_add=False)
    location = models.CharField(_("location"), max_length=250)
    website = models.CharField(_("website"), max_length=150)
    size = models.IntegerField(_("company size"))
    Profile = models.TextField(_("company Profile"), max_length=1000)
    linkedin = models.CharField(_("linkedin"), max_length=100)
    slug = models.SlugField(_("slug"), null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-company-{generate_code()[:4]}'
        # Call the real save() method
        super(Employer, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("employer", args=[self.slug])
# _____________________________________________________
