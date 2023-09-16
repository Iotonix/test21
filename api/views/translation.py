from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.translation import Translation
from api.serializers import (
    LanguageSerializer,
    PlatformSerializer,
    BaseSerializer,
    TranslationSerializer,
)
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


class TranslationViewSet(viewsets.ModelViewSet):
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
        return super(TranslationViewSet, self).get_permissions()

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    @action(detail=False, methods=["get"])
    def get_per_country(self, request, pk=None):
        lang = self.request.query_params.get("lang", None)
        longobject = None
        try:
            langobject = Language.objects.get(locale=lang)
        except Language.DoesNotExist:
            print("language nor Found: ", lang)
            return Response(status=404)

        print("Looking for translations", langobject)
        try:
            result = Translation.objects.filter(language=langobject)
        except Translation.DoesNotExist:
            print("Translations for language not found")
            return Response(status=404)
        print("We have translations...")
        data = []
        for row in result:
            # print(row.uniquetext, row.trans)
            data.append({"label": row.uniquetext.textlabel, "trans": row.trans})
        # return JsonResponse(data, json_dumps_params={'indent': 2})
        return Response(data)
