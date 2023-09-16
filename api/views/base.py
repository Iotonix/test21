import json
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.translation import Translation
from api.models.uniquetext import UniqueText
from api.serializers import (
    LanguageSerializer,
    PlatformSerializer,
    BaseSerializer,
    TranslationSerializer,
)
from rest_framework.permissions import IsAuthenticated, AllowAny


class BaseViewSet(viewsets.ModelViewSet):
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
        return super(BaseViewSet, self).get_permissions()

    queryset = Base.objects.all()
    serializer_class = BaseSerializer

    @action(detail=False, methods=["get"])
    def get_unused_keys(self, request, pk=None):
        print("Looking for clues")
        result = UniqueText.objects.raw(
            "SELECT id, created, textlabel FROM api_uniquetext a WHERE a.id NOT IN ( SELECT uniquetext_id FROM api_translation)"
        )
        data = []
        for row in result:
            data.append({"key": row.textlabel})
        print(data)
        # return JsonResponse(data, json_dumps_params={'indent': 2})
        return Response(data)
