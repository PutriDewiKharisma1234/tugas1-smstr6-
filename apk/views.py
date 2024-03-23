from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

def pendaftaran(request):
  print(request.user)
  return render(request, 'pendaftaran.html')

def BagianLogin(request):
  context = {
    'page_title': 'Daftar',
  }
  

  return render(request, 'masuk.html', context )

