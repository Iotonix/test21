from django.db import models
from api.models.platform import Platform


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    key = models.CharField(max_length=128, blank=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.key
