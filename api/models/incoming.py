from django.db import models


class TextRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text
