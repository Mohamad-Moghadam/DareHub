from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    vetbose_name = 'Challenge'
    verbose_name_plural = 'Challenges'