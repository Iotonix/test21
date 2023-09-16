from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]