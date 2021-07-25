from django.db import models


class BookCenterUserProfile(models.Model):
    class Meta:
        verbose_name = 'Profile'

    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    profile_image = models.FileField(
        upload_to='profiles',
        blank=True,
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)