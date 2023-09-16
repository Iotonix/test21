from api.models.language import Language
from api.models.uniquetext import UniqueText
from api.models.base import Base
from api.models.translation import Translation
from api.serializers import UniqueTextSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, AllowAny


class UniqueTextViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]
        else:
            self.permission_classes = [
                IsAuthenticated,
            ]
        return super(UniqueTextViewSet, self).get_permissions()

    queryset = UniqueText.objects.all()
    serializer_class = UniqueTextSerializer
