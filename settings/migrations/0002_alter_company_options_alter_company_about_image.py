# Generated by Django 4.2 on 2023-04-29 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Company'},
        ),
        migrations.AlterField(
            model_name='company',
            name='about_image',
            field=models.ImageField(upload_to='company', verbose_name='about_image'),
        ),
    ]