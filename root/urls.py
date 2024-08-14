from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView

from root.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
                  # Optional UI:
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_URL)