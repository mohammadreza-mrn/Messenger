
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("user.urls", namespace="user")),

    # Home View
    path("",HomeView.as_view(),name = "homeview"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
