# optivoraback/urls.py
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.http import HttpResponse

# Swagger (rest_framework_swagger) — patterns argumenti shart emas
schema_view = get_swagger_view(
    title='Optivora API documentation',
    url='/api/v1/'  # API bazaviy prefiksi
)

def health(request):
    return HttpResponse("OK")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Health-check
    path('health/', health),

    # Swagger docs
    path('', schema_view),                 # rootda ham ochilsin
    path('api/v1/docs/', schema_view),     # siz xohlagan yo‘l

    # DRF login/logout UI
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Asosiy API marshrutlari
    path('api/v1/', include('restapp.urls')),
]

# DEBUG=True bo‘lsa, static’ni Django bersin (WhiteNoise bilan ham ishlaydi)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# MEDIA fayllar (past trafik uchun mos)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
