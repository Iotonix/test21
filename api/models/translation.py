from django.db import models
from api.models.language import Language
from api.models.base import Base
from api.models.uniquetext import UniqueText


class Translation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    uniquetext = models.ForeignKey(UniqueText, on_delete=models.CASCADE)
    trans = models.TextField(blank=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.language.name + " - " + self.uniquetext.textlabel + " - " + self.trans
