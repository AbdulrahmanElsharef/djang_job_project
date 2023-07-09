from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext as _  # Create your models here.
from django.utils import timezone
from utils.generate_code import generate_code
from django.urls import reverse
from companies.models import Employer


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    slug = models.SlugField(_("slug"), null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-category-{generate_code()[:4]}'
        # Call the real save() method
        super(Category, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("category", args=[self.slug])
    # ______________________________________________________


JOB_TYPE = (('Full_Time', 'Full_Time'), ('Part_Time',
            'Part_Time'), ('Remotely', 'Remotely'))


class Job(models.Model):
    publisher = models.ForeignKey(User, verbose_name=_(
        "publisher"), on_delete=models.SET_NULL, null=True, blank=True, related_name='job_author')
    name = models.CharField(_("job"), max_length=100)
    employer = models.ForeignKey(Employer, verbose_name=_(
        "employer"), on_delete=models.SET_NULL, related_name='job_employer', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name=_(
        "category"), on_delete=models.CASCADE, related_name='job_category')
    job_type = models.CharField(_("job type"), max_length=50, choices=JOB_TYPE)
    published_at = models.DateTimeField(_("published at"), auto_now_add=True)
    vacancy = models.IntegerField(_("vacancy"))
    salary = models.IntegerField(_("salary"))
    des = models.TextField(_("description"), max_length=2500)
    Qual = models.TextField(_("Qualifications"), max_length=2500)
    Res = models.TextField(_("Responsibility"), max_length=2500)
    Benefits = models.TextField(_("Benefits"), max_length=2500)
    slug = models.SlugField(_("slug"), null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-job-{generate_code()[:4]}'
        super(Job, self).save(*args, **kwargs)  # Call the real save() method

    # def get_absolute_url(self):
    #     return reverse("job", args=[self.slug])
# __________________________________________________


class Candidate(models.Model):

    job = models.ForeignKey(
        Job, related_name='job_Candidates', on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=254)
    image = models.ImageField(_("image"), upload_to='Candidates')
    linkedin = models.URLField(_("linkedin"), max_length=100)
    cv = models.FileField(_("cv"), upload_to='cv', max_length=200)
    cover = models.TextField(_("cover"), max_length=1000)
    applied_at = models.DateTimeField(_("applied_at"), auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.name)}-user-{generate_code()[:4]}'
        super(Candidate, self).save(*args, **kwargs)
