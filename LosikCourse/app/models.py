from django.db import models

# Create your models here.

class Siswa(models.Model):
    Id_Siswa = models.AutoField(primary_key=True)
    Nama_Siswa = models.CharField(max_length=50)
    Tanggal_Lahir = models.DateField() 
    Alamat_Siswa = models.TextField(blank=True, null=True)
    Nomor_Telepon_Siswa = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Nama_Siswa)

class CustomerService(models.Model):
    ID_CS = models.AutoField(primary_key=True)
    nama_cs = models.CharField(max_length=50)
    nomer_telepon_cs = models.PositiveIntegerField()
    Alamat_cs = models.TextField()

    def __str__(self):
        return str(self.nama_cs)

class Registrasi(models.Model):
    Id_Registrasi = models.AutoField(primary_key=True)
    Id_Siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    ID_CS = models.ForeignKey(CustomerService, on_delete=models.CASCADE)
    Tanggal_Registrasi = models.DateField()

    def __str__(self):
        return str(self.Id_Siswa)

class Kelas_Mata_Kursus(models.Model):
    Id_Kelas_Mata_Kursus = models.AutoField(primary_key=True)
    Jenis_Kursus = models.CharField(max_length=70)
    Jenis_Kelas = models.CharField(max_length=50)
    Jumlah_Pertemuan = models.PositiveIntegerField()
    Jadwal = models.CharField(max_length=100)
    Harga = models.PositiveIntegerField()
    Status_Kelas = models.CharField(max_length=30)

    def __str__(self):
        return str(self.Jenis_Kursus)

class DetailRegistrasi(models.Model):
    Id_DetailRegistrasi = models.AutoField(primary_key=True)
    Id_Registrasi = models.ForeignKey(Registrasi, on_delete=models.CASCADE)
    Id_Kelas_Mata_Kursus = models.ForeignKey(Kelas_Mata_Kursus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Id_DetailRegistrasi)