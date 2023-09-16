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


class DownloadAllTranslationView(views.APIView):
    # parser_classes = (FileUploadParser,)
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, format=None):
        code = 200
        print("Hello from Download All Translation")
        platform_name = request.query_params.get("platform")
        key = request.query_params.get("key")

        try:
            platform = None
            if platform_name is not None:
                platform = Platform.objects.get(name__iexact=platform_name)
        except Platform.DoesNotExist:
            print("platform Not Found", platform_name)
            return Response(status=500)
        # print('we found the platform: ', platform.id)

        cursor = connection.cursor()
        sql_statement = (
            "SELECT 1 AS id, pl.name, base.key, utext.id, utext.textlabel, trans.trans, trans.language_id, trans.id"
            " FROM api_base base "
            " INNER JOIN api_basetext btext ON base.id = btext.base_id"
            " INNER JOIN api_uniquetext utext ON btext.uniquetext_id = utext.id"
            " INNER JOIN api_platform pl ON pl.id = base.platform_id"
            " INNER JOIN api_translation trans ON trans.uniquetext_id = btext.uniquetext_id"
            " WHERE pl.id = " + str(platform.id)
        )

        if key is not None:
            print("We have a key:", key)
            sql_statement += ' and base.key = "' + key + '"'

        sql_statement += " order by utext.textlabel, base.key, trans.language_id"
        # print(sql_statement)
        cursor.execute(sql_statement)
        # result = Base.objects.raw(sql_statement)
        result = cursor.fetchall()
        data = {}

        for row in result:
            keyVal = row[1] + "." + row[2] + "." + str(row[3]) + "." + row[4]

            # print(keyVal)

            cObj = data.get(keyVal)
            if cObj is None:
                data[keyVal] = {
                    "p": row[1],
                    "key": row[2],
                    "utid": row[3],
                    "l": row[4],
                    "tr": [
                        {
                            "l": row[6],
                            "t": row[5],
                            "tid": row[7],
                        }
                    ],
                }
            else:
                cTranslation = {
                    "l": row[6],  # language
                    "t": row[5],  # the actual translation
                    "tid": row[7],
                }
                cObj["tr"].append(cTranslation)
        # print(len(data))
        print("End of download all translations", len(data))

        # return JsonResponse(data, json_dumps_params={'indent': 2})
        return Response(data)
