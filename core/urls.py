from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("guetech/", admin.site.urls),
    path("", include("missions.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
