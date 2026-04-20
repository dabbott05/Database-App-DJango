from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views
from mythical_mane import views as mythical_views  # <-- Add this import

urlpatterns = [
    path("", core_views.index),
    path("admin/", admin.site.urls),
    
    # Patient URL
    path("patients/", mythical_views.patient_list, name="patient_list"),
    
    # Owner CRUD URLs
    path("owners/", mythical_views.OwnerListView.as_view(), name="owner_list"),
    path("owners/new/", mythical_views.OwnerCreateView.as_view(), name="owner_create"),
    path("owners/<int:pk>/edit/", mythical_views.OwnerUpdateView.as_view(), name="owner_update"),
    path("owners/<int:pk>/delete/", mythical_views.OwnerDeleteView.as_view(), name="owner_delete"),
    
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)