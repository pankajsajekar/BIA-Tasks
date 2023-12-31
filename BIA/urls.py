
from django.contrib import admin
from django.urls import path
from django.urls import include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BIA API",
        default_version='v1',
    ),
    public=True,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # swagger path
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('task1/', include('task1.urls') ),
    path('task2/', include('task2.urls') ),
    path('task3/', include('task3.urls') ),
    path('task4/', include('task4.urls') ),
    path('task5/', include('task5.urls') ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
