# Generated by Django 3.2.5 on 2021-07-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bc_profiles', '0002_auto_20210730_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcenteruserprofile',
            name='country',
            field=models.CharField(blank=True, choices=[('BG', 'Bulgaria'), ('UK', 'United Kingdom'), ('RO', 'Romania')], max_length=100),
        ),
    ]
