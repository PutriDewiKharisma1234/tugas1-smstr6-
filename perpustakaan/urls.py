from django.urls import path
from .views import coba

urlpatterns = [
    path ('coba',coba, name= 'coba')
]