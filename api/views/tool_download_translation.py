import re
from rest_framework.response import Response
from rest_framework import views
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from api.serializers import (
    LanguageSerializer,
    PlatformSerializer,
    BaseSerializer,
    TranslationSerializer,
)
from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.uniquetext import UniqueText
from api.models.base_text_set import BaseText
from api.models.translation import Translation
from django.db import connection, transaction
from rest_framework.permissions import IsAuthenticated, AllowAny


class ToolDownloadTranslationView(views.APIView):
    # parser_classes = (FileUploadParser,)
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, format=None):
        code = 200
        print("Hello from Download Translation:")
        locale = request.query_params.get("lang")
        platform_name = request.query_params.get("platform")
        key = request.query_params.get("key")
        keyid = request.query_params.get("keyid")
        try:
            language = None
            if locale is not None:
                language = Language.objects.get(locale__iexact=locale)
        except Language.DoesNotExist:
            print("language Not Found")
            return Response(status=500)
        # print('we found the language: ', language.id)

        try:
            platform = None
            if platform_name is not None:
                platform = Platform.objects.get(name__iexact=platform_name)
        except Platform.DoesNotExist:
            print("platform Not Found")
            return Response(status=500)
        # print('we found the platform: ', platform.id)

        cursor = connection.cursor()
        #                              0   1         2        3          4               5                   6         7          8
        sql_statement = (
            "SELECT 1 AS id, pl.name, base.key, base.id, utext.id, utext.textlabel, trans.language_id, trans.id, trans.trans"
            " FROM api_base base "
            " INNER JOIN api_basetext btext ON base.id = btext.base_id"
            " INNER JOIN api_uniquetext utext ON btext.uniquetext_id = utext.id"
            " INNER JOIN api_platform pl ON pl.id = base.platform_id"
            " INNER JOIN api_translation trans ON trans.uniquetext_id = btext.uniquetext_id"
            " WHERE trans.language_id = "
            + str(language.id)
            + " and pl.id = "
            + str(platform.id)
        )

        if key is not None:
            print("We have a key:", key)
            sql_statement += " and base.key =  " + key

        if keyid is not None:
            print("We have a keyid:", keyid)
            sql_statement += " and base.id = " + keyid

        # print(sql_statement)
        cursor.execute(sql_statement)
        # result = Base.objects.raw(sql_statement)
        result = cursor.fetchall()
        data = []
        for row in result:
            # print(row)
            obj = {
                "p": row[1],
                "key": row[2],
                "kid": row[3],
                "utid": row[4],
                "label": row[5],
                "lid": row[6],
                "tid": row[7],
                "t": row[8],
            }
            data.append(obj)
        # print(data.count)
        # return JsonResponse(data, json_dumps_params={'indent': 2})
        return Response(data)
