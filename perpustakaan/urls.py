from django.contrib import admin
from django.urls import path
from perpustakaan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pendaftaran/', views.pendaftaran, name='pendaftaran'),
    path('pinjam/', views.pinjam, name='pinjam'),
]