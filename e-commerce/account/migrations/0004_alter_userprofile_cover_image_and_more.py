# Generated by Django 4.2.2 on 2023-06-20 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_image',
            field=models.ImageField(blank=True, default='images/defaults/cover_image.png', null=True, upload_to='users/cover_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/defaults/profile_image.png', null=True, upload_to='users/profile_image'),
        ),
    ]
