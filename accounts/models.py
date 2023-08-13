from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _  # Create your models here.
from django.utils.text import slugify



USER_TYPE=(('Employee','Employee'),('Employer','Employer'))
class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)
    user_image = models.ImageField(
        upload_to='user_image', null=True, blank=True, default='default.png')
    user_type=models.CharField(_("user type"), max_length=50,choices=USER_TYPE)
    user_code = models.CharField(_("user code"),max_length=8, default=generate_code)
    mobile = models.CharField(_("phone"),max_length=100)
    home = models.CharField(_("address"),max_length=350)


    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


