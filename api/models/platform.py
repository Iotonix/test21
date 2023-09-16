from django.db import models


class Platform(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=32, blank=True, default='')
    data_start_row = models.PositiveSmallIntegerField(blank=False, default=3)
    translation_start_col = models.PositiveSmallIntegerField(
        blank=False, default=4)
    key_col = models.PositiveSmallIntegerField(blank=False, default=4)
    default_col = models.PositiveSmallIntegerField(blank=False, default=4)
    regex = models.CharField(max_length=128, blank=False, default='\.([a-zA-Z]{2})_(.*)')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
