from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_filters.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from root import settings

urlpatterns = [
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('apps.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
                  # Optional UI:
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)