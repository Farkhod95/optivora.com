# optivoraback/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Swagger UI (rest_framework_swagger) – mavjud bo‘lsa ishlaydi, bo‘lmasa fallback beradi
try:
    from rest_framework_swagger.views import get_swagger_view
    schema_view = get_swagger_view(
        title='Optivora API documentation',
        url='/api/v1/'   # API bazaviy prefiks
    )
except Exception:
    # Agar paket yo‘q/versiya mos kelmasa ham 404 bo‘lmasin:
    def schema_view(request):
        return HttpResponse(
            "Docs UI uchun 'rest_framework_swagger' kerak. Hozircha bu fallback ishlayapti.",
            content_type="text/plain"
        )

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Health-check
    path('health/', health),

    # Swagger / Docs
    path('', schema_view, name='root_docs'),             # rootda ham ochiladi
    path('api/v1/docs/', schema_view, name='swagger'),   # siz so‘ragan URL

    # DRF auth UI
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API marshrutlari
    path('api/v1/', include('restapp.urls')),
]

# DEBUG=True bo‘lsa statikni Django beradi (prod’da WhiteNoise beradi)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Media fayllar (kerak bo‘lsa)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
