from django.shortcuts import render, redirect
from .frmlr import BagianPendaftaran, BagianPinjamBuku

#Pendaftaran siswa
def pendaftaran(request):
    if request.method == 'POST':
        form = BagianPendaftaran(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pinjam')
    else:
        form = BagianPendaftaran()
    return render(request, 'pendaftaran.html', {'form': form})


# Peminjaman buku
def pinjam(request):
    if request.method == 'POST':
        form = BagianPinjamBuku(request.POST)
        if form.is_valid():
            # Proses peminjaman buku
            return redirect('pinjam')
    else:
        form = BagianPinjamBuku()
    return render(request, 'pinjam.html', {'form': form})
