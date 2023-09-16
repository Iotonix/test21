"""TODOC"""
from rest_framework.response import Response
from rest_framework import views

# from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
# from api.serializers import LanguageSerializer, PlatformSerializer, BaseSerializer, TranslationSerializer
from django.db import connection
from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.uniquetext import UniqueText
from api.models.base_text_set import BaseText
from api.models.translation import Translation
from rest_framework.permissions import IsAuthenticated, AllowAny


class UpdateTranslationView(views.APIView):
    """TODOC"""

    permission_classes = [
        IsAuthenticated,
    ]

    def put(self, request, fmt=None):
        """TODOC"""
        _ = fmt
        print("Hello from translation upvader.")

        locale = request.query_params.get("lang")
        platform_name = request.query_params.get("platform")
        key = request.query_params.get("key")
        master = request.query_params.get("master")
        trans = request.query_params.get("trans")

        if None in {locale, platform_name, key, master, trans}:
            return Response(status=500)

        try:
            language = Language.objects.get(locale__iexact=locale)
        except Language.DoesNotExist:
            print("language Not Found")
            return Response(status=500)
        print("we found the language: ", locale)

        try:
            platform = Platform.objects.get(name__iexact=platform_name)
        except Platform.DoesNotExist:
            print("platform Not Found")
            return Response(status=500)
        print("we found the platform: ", platform.id)

        try:
            base = Base.objects.get(platform=platform, key=key)
        except Base.DoesNotExist:
            print("Base Not Found")
            return Response(status=500)
        print("we found the base: ", base.id)

        try:
            text = UniqueText.objects.get(textlabel=master)
        except UniqueText.DoesNotExist:
            print("UT Not Found")
            return Response(status=500)
        print("we found the UT: ", text.id)
        translation = Translation.objects.filter(
            language=language, uniquetext=text
        ).update(trans=trans)
        print("++++++++++++++++++++++++++++")
        print(
            "Updated Translation. language="
            + language.name_en
            + " unique="
            + text.textlabel
            + " val=",
            translation,
        )

        return Response(status=200)
