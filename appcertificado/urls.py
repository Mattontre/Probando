from django.urls import path
from .views import certificado_view

app_name = 'appcertificado'

urlpatterns = [
    path('appcertificado/', certificado_view, name='certificado'),
]