from django.shortcuts import render

def pendaftaran(request):
  return render(request, 'pendaftaran.html')

def pinjam(request):
  return render(request, 'pinjam.html')