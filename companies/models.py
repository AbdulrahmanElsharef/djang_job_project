from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _  # Create your models here.
from django.utils import timezone
from utils.generate_code import generate_code
from django.urls import reverse


# Create your models here.
class Employer(models.Model):
    company = models.CharField(_("company"), max_length=200)
    industry = models.CharField(_("Industry"), max_length=250)
    Em_image = models.ImageField( upload_to='Employer')
    founded = models.DateField(_("founded"), auto_now=False, auto_now_add=False)
    website = models.URLField(_("website"),max_length = 200)
    size = models.CharField(_("company size"), max_length=100)
    company_detail = models.TextField(_("company detail"), max_length=1000)
    Em_linkedin = models.URLField(_("linkedin"), max_length=200)
    Em_phone = models.CharField(_("phone"),max_length=50)
    Em_address = models.CharField(_("address"),max_length=350)
    slug = models.SlugField(_("slug"), null=True, blank=True, unique=True)

    def __str__(self):
        return self.company

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.company)}-company-{generate_code()[:4]}'
        # Call the real save() method
        super(Employer, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("employer", args=[self.slug])
# _____________________________________________________
