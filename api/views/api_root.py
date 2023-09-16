from api.models import Language, Platform, Base, Translation
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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def api_root(request, format=None):
    permission_classes = [
        IsAuthenticated,
    ]
    return Response(
        {
            "languages": reverse("language-list", request=request, format=format),
            "platforms": reverse("platform-list", request=request, format=format),
            "bases": reverse("base-list", request=request, format=format),
            "translations": reverse("translation-list", request=request, format=format),
        }
    )
