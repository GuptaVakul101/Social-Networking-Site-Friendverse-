# Generated by Django 2.1.5 on 2019-03-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190309_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='home/ProfileImage/'),
        ),
    ]
