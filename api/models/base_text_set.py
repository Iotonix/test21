from django.db import models
from api.models.base import Base
from api.models.uniquetext import UniqueText


class BaseText(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    uniquetext = models.ForeignKey(UniqueText, on_delete=models.CASCADE)

    def __str__(self):
        return self.base.key + " => " + self.uniquetext.textlabel
