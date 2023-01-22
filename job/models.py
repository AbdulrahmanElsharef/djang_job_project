from django.db import models
from django.utils.text import slugify

# Create your models here.


JOB_TYPE = (('full time', 'full time'), ('part time', 'part time'))


def upload_img(instance, filename):
    img_name, img_exct = filename.split(".")
    return f"jobs/{instance.slug}.{img_exct}"


class Job (models.Model):
    title = models.CharField(max_length=200)
    # LOCATION
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=upload_img,)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(
        'category', on_delete=models.CASCADE, related_name='category')
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)  # Call the real save() method


class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply_job(models.Model):
    job = models.ForeignKey(
        'Job', on_delete=models.CASCADE, related_name='Job')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    site = models.URLField()
    cv = models.FileField(upload_to='Apply_job/')
    cover = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
