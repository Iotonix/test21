from django.contrib.auth.models import User
from rest_framework import serializers

from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.translation import Translation
from api.models.uniquetext import UniqueText
from api.models.base_text_set import BaseText


class LanguageSerializer(serializers.ModelSerializer):
    flagCode = serializers.SerializerMethodField()
    nameSimplified = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = ("id", "locale", "name_en", "name", "flagCode", "nameSimplified")

    def get_flagCode(self, instance):
        code = instance.locale.split("_")
        return "{}.svg".format(code[-1]).lower()

    def get_nameSimplified(self, instance):
        code = instance.name_en.split("(")
        return code[0]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = (
            "id",
            "name",
        )


class UniqueTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueText
        fields = (
            "id",
            "textlabel",
        )


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ("id", "platform", "key")


class BaseTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseText
        fields = ("id", "base", "text")


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ("language", "uniquetext", "trans")
