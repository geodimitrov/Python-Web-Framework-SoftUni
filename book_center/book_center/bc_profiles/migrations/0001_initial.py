# Generated by Django 3.2.5 on 2021-08-07 21:40

import book_center.utils.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCenterDiscussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english, django.core.validators.MinLengthValidator(5)])),
                ('description', models.CharField(max_length=200, validators=[book_center.utils.validators.validate_alphabet_characters_english, django.core.validators.MinLengthValidator(10)])),
                ('topic', models.CharField(max_length=20, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Discussion',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='BookCenterDiscussionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('discussion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bc_profiles.bookcenterdiscussion')),
            ],
            options={
                'verbose_name': 'Comment',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='CommentUpvote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bc_profiles.bookcenterdiscussioncomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookCenterUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('last_name', models.CharField(blank=True, max_length=20, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('bio', models.CharField(blank=True, max_length=200, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('profile_image', models.ImageField(default='profiles/default_profile_img.jpg', upload_to='profiles')),
                ('country', models.CharField(blank=True, choices=[('BG', 'Bulgaria'), ('UK', 'United Kingdom'), ('RO', 'Romania')], max_length=100)),
                ('city', models.CharField(blank=True, max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('twitter_account', models.CharField(blank=True, max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('facebook_account', models.CharField(blank=True, max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('instagram_account', models.CharField(blank=True, max_length=50, validators=[book_center.utils.validators.validate_alphabet_characters_english])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='BookCenterDiscussionLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bc_profiles.bookcenterdiscussion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
