from django.db import models

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    tahun_terbit = models.IntegerField()

class RakBuku(models.Model):
    nomor_rak = models.CharField(max_length=10)
    lokasi = models.CharField(max_length=50)

class Penerbit(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.TextField()

class Pengarang(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
