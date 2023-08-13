# Generated by Django 4.2 on 2023-08-13 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.generate_code


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='user_image')),
                ('user_type', models.CharField(choices=[('Employee', 'Employee'), ('Employer', 'Employer')], max_length=50, verbose_name='user type')),
                ('user_code', models.CharField(default=utils.generate_code.generate_code, max_length=8, verbose_name='user code')),
                ('mobile', models.CharField(max_length=100, verbose_name='phone')),
                ('home', models.CharField(max_length=350, verbose_name='address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
