from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _  # Create your models here.

USER_TYPE=(('Employee','Employee'),('Employer','Employer'))
class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='profile', null=True, blank=True, default='default.png')
    user_type=models.CharField(_("user type"), max_length=50,choices=USER_TYPE)
    code = models.CharField(max_length=8, default=generate_code)
    job = models.CharField(max_length=50)
    linkedin = models.URLField(_("linkedin"), max_length=100)
    cv = models.FileField(_("cv"), upload_to='cv', max_length=200)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
