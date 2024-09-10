import django.conf.urls.static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView
from root import settings

urlpatterns = ([

                   path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                   path('admin/', admin.site.urls),
                   path('api/v1/', include('apps.urls')),
                   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                   path("ckeditor5/", include('django_ckeditor_5.urls')),

               ] + django.conf.urls.static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
               django.conf.urls.static.static(settings.STATIC_URL, document_root=settings.STATIC_URL))
