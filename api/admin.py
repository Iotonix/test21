from django.contrib import admin

# Register your models here.
from api.models.language import Language
from api.models.platform import Platform
from api.models.base import Base
from api.models.translation import Translation
from api.models.uniquetext import UniqueText
from api.models.base_text_set import BaseText
from django.contrib.admin import SimpleListFilter


class BaseAdmin(admin.ModelAdmin):
    search_fields = ("key",)


class BaseTextAdmin(admin.ModelAdmin):
    search_fields = ("base__key", "uniquetext__textlabel")


class UniqueTextAdmin(admin.ModelAdmin):
    search_fields = ("textlabel",)


class TranslationAdmin(admin.ModelAdmin):
    list_display = (
        "language",
        "uniquetext",
        "trans",
    )
    list_filter = ("language",)
    search_fields = (
        "uniquetext__textlabel",
        "trans",
    )
    # change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_template = "admin/change_list.html"

    def __str__(self):
        return (
            self.language.name + ":" + self.uniquetext.textlabel + " => " + self.trans
        )


admin.site.site_header = "Language Service"

admin.site.register(Base, BaseAdmin)
admin.site.register(UniqueText, UniqueTextAdmin)
admin.site.register(BaseText, BaseTextAdmin)
admin.site.register(Platform)
admin.site.register(Language)
admin.site.register(Translation, TranslationAdmin)
