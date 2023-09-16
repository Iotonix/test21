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


class AddTranslationView(views.APIView):
    """TODOC"""

    permission_classes = [
        IsAuthenticated,
    ]  # permission_classes = [AllowAny, ]
    # parser_classes = (FileUploadParser,)
    # parser_classes = (MultiPartParser, FormParser)

    def put(self, request, fmt=None):
        """TODOC"""
        _ = fmt
        print("Hello from translation adder.")
        locale = request.data.get("lang")
        platform_name = request.data.get("platform")
        key = request.data.get("key")
        master = request.data.get("master")
        trans = request.data.get("trans")

        if None in {locale, platform_name, key, master, trans}:
            return Response(status=500)

        try:
            language = Language.objects.get(locale__iexact=locale)
        except Language.DoesNotExist:
            print("language Not Found", locale)
            return Response(status=500)
        print("we found the language: ", locale)

        try:
            platform = Platform.objects.get(name__iexact=platform_name)
        except Platform.DoesNotExist:
            print("platform Not Found")
            return Response(status=500)
        print("we found the platform: ", platform.id)

        base, created = Base.objects.get_or_create(platform=platform, key=key)
        msg = " created" if created else " fetched"
        print("BASE: ", base.key, msg)

        text, created = UniqueText.objects.get_or_create(textlabel=master)
        msg = " created" if created else " fetched"
        print("UNIQUE TEXT: ", text.textlabel, msg)

        base_text_set, created = BaseText.objects.get_or_create(
            base=base, uniquetext=text
        )
        msg = " created" if created else " fetched"
        print("BASE TEXT SET for ", text.textlabel, msg, base_text_set)
        print("Done setting the Base!")

        try:
            translation = Translation.objects.get(language=language, uniquetext=text)
            translation.trans = trans
            translation.save()
            print(
                "Updated Translation. language="
                + language.name_en
                + " unique="
                + text.textlabel
                + " val=",
                translation,
            )
        except Translation.DoesNotExist:
            translation = Translation.objects.create(
                language=language, uniquetext=text, trans=trans
            )
            print(
                "Created Translation. language="
                + language.name_en
                + " unique="
                + text.textlabel
                + " val=",
                translation,
            )

        return Response(status=200)
