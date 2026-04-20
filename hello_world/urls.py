from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views
from mythical_mane import views as mythical_views  # <-- Add this import

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    path("patients/", mythical_views.patient_list, name="patient_list"), # <-- Add this route
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)