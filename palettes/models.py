from django.db import models
from django.contrib.auth.models import User


class LikedColor(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    hex_code = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'hex_code')


class SavedPalette(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    colors = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)