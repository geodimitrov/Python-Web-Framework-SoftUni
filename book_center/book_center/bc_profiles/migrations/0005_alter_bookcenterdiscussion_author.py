# Generated by Django 3.2.5 on 2021-08-05 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bc_profiles', '0004_bookcenterdiscussion_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcenterdiscussion',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
