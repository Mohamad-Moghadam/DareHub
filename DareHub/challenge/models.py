from django.db import models
from user.models import CustomUser

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(CustomUser, blank=True, related_name='challenges')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_challenges')


    vetbose_name = 'Challenge'
    verbose_name_plural = 'Challenges'

    def create(self):
        creator = CustomUser.objects.get(id=self._id)
        self.save()