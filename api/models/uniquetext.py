from django.db import models


class UniqueText(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    textlabel = models.TextField(blank=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.textlabel
