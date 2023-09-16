import re
from django.core.exceptions import MultipleObjectsReturned
from openpyxl import load_workbook
from rest_framework.response import Response
from rest_framework import views
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from api.serializers import (
    LanguageSerializer,
    PlatformSerializer,
    BaseSerializer,
    TranslationSerializer,
)
from api.models.language import Language
from api.models.platform import Platform
from api.models.incoming import TextRequest
from api.models.translation import Translation
from api.models.base import Base
from api.models.uniquetext import UniqueText
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.base_text_set import BaseText
from api.models.translation import Translation
import pandas as pd
from pandas import DataFrame as df


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete(request, format=None):
    print("New cleaning up")
    key = request.data.get("key")
    label = request.data.get("l")
    platform_name = request.data.get("p")
    utid = request.data.get("utid")

    print(f"{key} {platform_name} {utid}")
    platform = Platform.objects.get(name__iexact=platform_name)

    instance = Base.objects.filter(platform=platform, key__iexact=key)
    print(f"we found {instance.count()} base")
    if instance.count() == 1:
        instance.delete()

    instance = Translation.objects.filter(uniquetext=utid)
    print(f"we found {instance.count()} translations")
    instance.delete()

    instance = BaseText.objects.filter(uniquetext=utid)
    print(f"we found {instance.count()} Basetext sets for {utid}")
    print(instance.select_related)
    instance.delete()

    instance = UniqueText.objects.filter(id=utid)
    print(f"we found {instance.count()} Unique Textx")
    if instance.count() == 1:
        instance.delete()
    # locale = request.query_params.get('lang')
    # platform_name = request.query_params.get('platform')
    # keyid = request.query_params.get('keyid')
    # key = request.query_params.get('key')
    # utid = request.query_params.get('utid')

    # sql_statement = ('SELECT 1 AS id, pl.name, base.key, base.id, utext.id, utext.textlabel, trans.language_id, trans.id, trans.trans'
    #                     ' FROM api_base base '
    #                     ' INNER JOIN api_basetext btext ON base.id = btext.base_id'
    #                     ' INNER JOIN api_uniquetext utext ON btext.uniquetext_id = utext.id'
    #                     ' INNER JOIN api_platform pl ON pl.id = base.platform_id'
    #                     ' INNER JOIN api_translation trans ON trans.uniquetext_id = btext.uniquetext_id'
    #                     ' WHERE pl.id= ' + str(platform.id))
    return Response({"Code": "OK"})
