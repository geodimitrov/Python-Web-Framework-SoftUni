# Generated by Django 3.2.5 on 2021-08-07 19:13

import book_center.utils.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCenterContactFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english, django.core.validators.MinLengthValidator(5)])),
                ('email', models.EmailField(max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('message', models.CharField(max_length=500, validators=[book_center.utils.validators.validate_alphabet_characters_english, django.core.validators.MinLengthValidator(10)])),
                ('date_received', models.DateField(auto_now_add=True)),
                ('reply', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Contact Form',
            },
        ),
    ]
