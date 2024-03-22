from django import forms
from .models import Anggota

class BagianPendaftaran(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['nama', 'alamat', 'nomor_telepon']

class BagianPinjamBuku(forms.Form):
    id_anggota = forms.IntegerField()
    id_buku = forms.IntegerField()
    tanggal_pinjam = forms.DateField()