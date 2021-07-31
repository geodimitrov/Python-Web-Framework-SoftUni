# Generated by Django 3.2.5 on 2021-07-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bc_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcenteruserprofile',
            name='country',
            field=models.CharField(blank=True, choices=[('BG', 'Bulgaria'), ('UK', 'United Kingdom')], default='BG', max_length=100),
        ),
        migrations.AlterField(
            model_name='bookcenteruserprofile',
            name='profile_image',
            field=models.ImageField(default='profiles/default_profile_img.jpg', upload_to='profiles'),
        ),
    ]