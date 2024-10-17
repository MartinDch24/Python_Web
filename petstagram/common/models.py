from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    class Meta:
        indexes = [models.Index(fields=['date_of_publication']),]
        ordering = ['-date_of_publication']

    text = models.TextField(
        max_length=300,
    )

    date_of_publication = models.DateField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )
