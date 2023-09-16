from django.db import models


def flagImage_path(instance, filename):
    return 'language/{0}/{1}'.format(instance.name, filename)

class Language(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    locale = models.CharField(max_length=32, blank=True, default='xx_XX')
    name_en = models.CharField(max_length=32, blank=True, default='')
    name = models.CharField(max_length=32, blank=True, default='')
    # flag = models.FileField(upload_to=flagImage_path, null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name_en
