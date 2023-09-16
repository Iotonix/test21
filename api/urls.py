"""url configuration file"""

from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from api.views.platform import PlatformViewSet
from api.views.language import LanguageViewSet
from api.views.base import BaseViewSet
from api.views.tool_download_translation_all_languages import (
    ToolDownloadTranslationAllLanguagesView,
)
from api.views.tool_download_unused_keys import ToolDownloadUnusedView
from api.views.translation import TranslationViewSet
from api.views.upload import (
    FileUploadView,
    langUpload,
    langAdd,
    langGet,
    langNew,
    getIncoming,
    updateTranslation,
)
from api.views.delete import delete
from api.views.download_translation import DownloadTranslationView
from api.views.add_translation import AddTranslationView
from api.views.update_translation import UpdateTranslationView
from api.views.unique_text import UniqueTextViewSet
from api.views.download_all_translation import DownloadAllTranslationView
from api.views.single_translation import SingleTranslationView
from api.views.tool_download_translation import ToolDownloadTranslationView

# from api.views.excel_upload import FileUploadView
schema_view = get_swagger_view(title="Language Service API")


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"platforms", PlatformViewSet)
router.register(r"languages", LanguageViewSet)
router.register(r"bases", BaseViewSet)
router.register(r"translations", TranslationViewSet)
router.register(r"uniquetexts", UniqueTextViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r"^", include(router.urls)),
    re_path(r"upload$", FileUploadView.as_view()),
    re_path(r"download_all", DownloadAllTranslationView.as_view()),
    re_path(r"translate_one", SingleTranslationView.as_view()),
    re_path(r"tool_unused", ToolDownloadUnusedView.as_view()),
    re_path(r"tool_trans_bykey", ToolDownloadTranslationAllLanguagesView.as_view()),
    re_path(r"del_entry", delete),
    re_path(r"tool_download", ToolDownloadTranslationView.as_view()),
    re_path(r"download", DownloadTranslationView.as_view()),
    re_path(r"updateTranslation", updateTranslation),
    re_path(r"update", UpdateTranslationView.as_view()),
    re_path(r"languageUp", langUpload),
    re_path(r"languageAdd", langAdd),
    re_path(r"languageGet", langGet),
    re_path(r"languageNew", langNew),
    re_path(r"incomingRequests", getIncoming),
    re_path(r"create", AddTranslationView.as_view()),
    re_path(r"^swagger/", schema_view),
]
