import re
import os
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import views
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from google.cloud import translate_v2
from rest_framework.permissions import IsAuthenticated, AllowAny

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"google_secret.json"


class SingleTranslationView(views.APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        code = 200
        print(format)
        target = request.data.get("target")
        label = request.data.get("label")
        if label is None or target is None:
            wpy_resp = {
                "target_language": "Nothing",
                "translation": "You are too stupid",
            }
            print(f"Translate {label} to {target}")
        else:
            print(f"Hello from Single Translation: translate {label} to {target}")
            translate_client = translate_v2.Client()
            translation = translate_client.translate(label, target_language=target)

            wpy_resp = {
                "target_language": target,
                "translation": translation,
            }
        # return JsonResponse(data, json_dumps_params={'indent': 2})
        # return Response(data)
        return JsonResponse(wpy_resp, json_dumps_params={"indent": 2})
