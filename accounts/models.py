from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile',null=True,blank=True,default='default.png')
    code = models.CharField(max_length=8,default=generate_code)
    job = models.CharField(max_length=50)
    name=models.CharField(_("name"), max_length=100)
    email=models.CharField(_("email"), max_length=100)
    linkedin=models.URLField(_("linkedin"), max_length=100)
    cv=models.FileField(_("cv"), upload_to='cv', max_length=200)
    phone=models.CharField(max_length=20)

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


    
phone_number = (
    ('Home','Home'),
    ('Work','Work')
)    
    
    
class UserNumbers(models.Model):
    user = models.ForeignKey(User, related_name='user_phones', on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=12 , choices=phone_number)
    


address_choices = (
    ('Home','Home'),
    ('Office','Office'),
)    
    
    
class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name='User_Address', on_delete=models.CASCADE)
    type = models.CharField(max_length=12 , choices=address_choices)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    apartment = models.CharField(max_length=20)

