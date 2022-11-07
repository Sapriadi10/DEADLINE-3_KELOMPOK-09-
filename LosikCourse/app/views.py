from atexit import register
import re
from socket import IP_DROP_MEMBERSHIP
from django.shortcuts import render,redirect
from django.shortcuts import render,redirect
from . import models
from datetime import datetime
from django.http import HttpResponse

# # Create your views here.
def dashboard(request):
    jumlahsiswa = models.Siswa.objects.all().count()
    jumlahkelas = models.Kelas_Mata_Kursus.objects.all().count()
    jumlahregistrasi = models.Registrasi.objects.all().count()
    jumlahdetailregistrasi = models.DetailRegistrasi.objects.all().count()
    return render(request, 'homey.html',{ 
        "jumlahsiswa" : jumlahsiswa,
        "jumlahkelas" : jumlahkelas,
        "jumlahregistrasi" : jumlahregistrasi,
        "jumlahdetailregistrasi" : jumlahdetailregistrasi
    })

def profile(request):
    return render(request, "profile.html")

def formsiswa(request):
    return render(request, "formregistrasi.html")

def siswa(request):
    allsiswaobj = models.Siswa.objects.all()
    return render(request, 'sisway.html', {
        'allsiswaobj' : allsiswaobj,
    })

def createsiswa(request):
    if request.method == "GET":
        return render(request, 'createsisway.html')
    else:
        Nama_Siswa = request.POST["Nama_Siswa"]
        Tanggal_Lahir = request.POST["Tanggal_Lahir"]
        Alamat_Siswa = request.POST["Alamat_Siswa"]
        Nomor_Telepon_Siswa = request.POST["Nomor_Telepon_Siswa"]

        newsiswa = models.Siswa(
            Nama_Siswa = Nama_Siswa,
            Tanggal_Lahir = Tanggal_Lahir,
            Alamat_Siswa = Alamat_Siswa,
            Nomor_Telepon_Siswa = Nomor_Telepon_Siswa,   
        )
        newsiswa.save()
        return redirect('siswa')

def formsiswa(request):
    if request.method == "GET":
        return render(request, 'formsiswa.html')
    else:
        Nama_Siswa = request.POST["Nama_Siswa"]
        Tanggal_Lahir = request.POST["Tanggal_Lahir"]
        Alamat_Siswa = request.POST["Alamat_Siswa"]
        Nomor_Telepon_Siswa = request.POST["Nomor_Telepon_Siswa"]

        newsiswa = models.Siswa(
            Nama_Siswa = Nama_Siswa,
            Tanggal_Lahir = Tanggal_Lahir,
            Alamat_Siswa = Alamat_Siswa,
            Nomor_Telepon_Siswa = Nomor_Telepon_Siswa,   
        )
        newsiswa.save()
        return redirect('formregistrasi')

def updatesiswa(request,id):
    siswaobj = models.Siswa.objects.get(Id_Siswa=id)
    tanggal = datetime.strftime(siswaobj.Tanggal_Lahir, '%Y-%m-%d')
    if request.method == "GET" :
        return render(request, 'updatesisway.html', {
            'allsiswa' : siswaobj,
            'tanggal':tanggal
        })
    else :
        siswaobj.Nama_Siswa = request.POST['Nama_Siswa']
        siswaobj.Tanggal_Lahir = request.POST['Tanggal_Lahir']
        siswaobj.Alamat_Siswa = request.POST['Alamat_Siswa']
        siswaobj.Nomor_Telepon_Siswa = request.POST['Nomor_Telepon_Siswa']
        siswaobj.save()
        return redirect('siswa')

def deletesiswa(request,id):
    siswaobj = models.Siswa.objects.get(Id_Siswa=id)
    siswaobj.delete()
    return redirect('siswa')

def CustomerService(request):
    allCustomerServiceobj = models.CustomerService.objects.all()

    return render(request, 'CustomerServicey.html', {
        "allCustomerService" : allCustomerServiceobj,
    })

def createCustomerService(request):
    if request.method == "GET":
        return render(request, 'createCustomerServicey.html')
    else:
        nama_cs = request.POST['nama_cs']
        nomer_telepon_cs = request.POST['nomer_telepon_cs']
        Alamat_cs = request.POST['Alamat_cs']
        
        newCustomerService = models.CustomerService(
            nama_cs = nama_cs,
            nomer_telepon_cs= nomer_telepon_cs,
            Alamat_cs = Alamat_cs,
        )
        newCustomerService.save()

        return redirect('CustomerService')

def updateCustomerService(request,id):
    CustomerServiceobj = models.CustomerService.objects.get(ID_CS=id)
    if request.method == "GET" :
        return render(request, 'updateCustomerServicey.html', {
            'allCustomerService' : CustomerServiceobj,
        })
    else :
        CustomerServiceobj.nama_cs = request.POST['nama_cs']
        CustomerServiceobj.nomer_telepon_cs = request.POST['nomer_telepon_cs']
        CustomerServiceobj.Alamat_cs = request.POST['Alamat_cs']
        CustomerServiceobj.save()
        return redirect('CustomerService')

def deleteCustomerService(request,id):
    CustomerServiceobj = models.CustomerService.objects.get(ID_CS=id)
    CustomerServiceobj.delete()
    return redirect('CustomerService')

def registrasi(request):
    allregistrasiobj = models.Registrasi.objects.all()
    getregistrasiobj = models.Registrasi.objects.get(Id_Registrasi=2)

    return render(request, 'registrasiy.html',{
        'allregistrasiobj' : allregistrasiobj,
        'getregistrasiobj' : getregistrasiobj,
    })

def createregistrasi(request):
    if request.method == "GET":
        allsiswaobj = models.Siswa.objects.all()
        allCustomerServiceobj = models.CustomerService.objects.all()
        return render(request, 'createregistrasiy.html',{
            'datasiswa' : allsiswaobj, 'datacustomerservice': allCustomerServiceobj
        })

    if request.method == "POST":
        Id_Siswa = request.POST['Id_Siswa']
        allsiswaobj = models.Siswa.objects.get(Id_Siswa = Id_Siswa)

        ID_CS = request.POST['ID_CS']
        allCustomerServiceobj = models.CustomerService.objects.get(ID_CS = ID_CS)
        Tanggal_Registrasi = request.POST['Tanggal_Registrasi']

        newregistrasi = models.Registrasi(
            Id_Siswa = allsiswaobj,
            ID_CS = allCustomerServiceobj,
            Tanggal_Registrasi = Tanggal_Registrasi
        )
        newregistrasi.save()

        return redirect('registrasi')

def formregistrasi(request):
    if request.method == "GET":
        allsiswaobj = models.Siswa.objects.all()
        allCustomerServiceobj = models.CustomerService.objects.all()
        return render(request, 'formregistrasi.html',{
            'datasiswa' : allsiswaobj, 'datacustomerservice': allCustomerServiceobj
        })

    if request.method == "POST":
        Id_Siswa = request.POST['Id_Siswa']
        allsiswaobj = models.Siswa.objects.get(Id_Siswa = Id_Siswa)

        ID_CS = request.POST['ID_CS']
        allCustomerServiceobj = models.CustomerService.objects.get(ID_CS = ID_CS)
        Tanggal_Registrasi = request.POST['Tanggal_Registrasi']

        newregistrasi = models.Registrasi(
            Id_Siswa = allsiswaobj,
            ID_CS = allCustomerServiceobj,
            Tanggal_Registrasi = Tanggal_Registrasi
        )
        newregistrasi.save()

        return redirect('formdetailregistrasi')

def updateregistrasi(request,id):
    registrasiobj = models.Registrasi.objects.get(Id_Registrasi= id)
    allsiswaobj = models.Siswa.objects.all()
    allcustomerserviceobj = models.CustomerService.objects.all()
    tanggal = datetime.strftime(registrasiobj.Tanggal_Registrasi, '%Y-%m-%d')
    if request.method == "GET":
        return render(request,'updateregistrasiy.html',{
            'registrasi' : registrasiobj,
            'tanggal':tanggal,
            'allsiswaobj' : allsiswaobj,
            'allcustomerserviceobj' : allcustomerserviceobj,
        })
    else :
        getidsiswa = models.Siswa.objects.get(Id_Siswa = request.POST['Id_Siswa'])
        getidcs = models.CustomerService.objects.get(ID_CS = request.POST['ID_CS'])
        registrasiobj.ID_CS = getidcs
        registrasiobj.Id_Siswa = getidsiswa
        registrasiobj.Tanggal_Registrasi = request.POST['Tanggal_Registrasi']
        registrasiobj.save()
        return redirect('registrasi')

def deleteregistrasi(request,id):
    registrasiobj = models.Registrasi.objects.get(Id_Registrasi=id)
    registrasiobj.delete()
    return redirect('registrasi')

def kelasmatakursus(request):
    if request.method == "GET":
        allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.all()
        filterkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.all()
        return render(request, 'kelasmatakursusy.html', {
            "allkelasmatakursus" : allkelasmatakursusobj, "filterkelasmatakursusobj" : filterkelasmatakursusobj,
        })
    else:
        kelasobj = request.POST["filterkelas"]
        if kelasobj == "Full-stack Web Developer":
            nilai = "Full-stack Web Developer"
        elif kelasobj == "UI/UX Design and Produc Management":
            nilai = "UI/UX Design and Produc Management"
        elif kelasobj == 'Graphic and Motion Designer':
            nilai = 'Graphic and Motion Designer'
        else:
            nilai = 'Digital Marketing'
        filterkelasobj = models.Kelas_Mata_Kursus.objects.filter(Jenis_Kursus = nilai )
        return render(request, "filteringkelasy.html", {'filterkelasobj' : filterkelasobj})

def createkelasmatakursus(request):
    if request.method == "GET":
        return render(request, 'createkelasmatakursusy.html')
    else:
        JenisKursus = request.POST['JenisKursus']
        JenisKelas = request.POST['JenisKelas']
        JumlahPertemuan = request.POST['JumlahPertemuan']
        Jadwal = request.POST['Jadwal']
        Harga = request.POST['Harga']
        StatusKelas = request.POST['StatusKelas']
        
        newkelasmatakursus = models.Kelas_Mata_Kursus(
            Jenis_Kursus = JenisKursus,
            Jenis_Kelas = JenisKelas,
            Jumlah_Pertemuan = JumlahPertemuan,
            Jadwal = Jadwal,
            Harga = Harga,
            Status_Kelas = StatusKelas
        )
        newkelasmatakursus.save()

        return redirect('kelasmatakursus')

def updatekelasmatakursus(request,id):
    kelasmatakursusobj = models.Kelas_Mata_Kursus.objects.get(Id_Kelas_Mata_Kursus=id)
    if request.method == "GET" :
        return render(request, 'updatekelasmatakursusy.html', {
            'Kelas_Mata_Kursus' : kelasmatakursusobj,
        })
    else :
        kelasmatakursusobj.Jenis_Kursus = request.POST['JenisKursus']
        kelasmatakursusobj.Jenis_Kelas = request.POST['JenisKelas']
        kelasmatakursusobj.Jumlah_Pertemuan = request.POST['JumlahPertemuan']
        kelasmatakursusobj.Jadwal = request.POST['Jadwal']
        kelasmatakursusobj.Harga = request.POST['Harga']
        kelasmatakursusobj.Status_Kelas = request.POST['StatusKelas']
        kelasmatakursusobj.save()
        return redirect('kelasmatakursus')

def deletekelasmatakursus(request,id):
    kelasmatakursusobj = models.Kelas_Mata_Kursus.objects.get(Id_Kelas_Mata_Kursus=id)
    kelasmatakursusobj.delete()
    return redirect('kelasmatakursus')

def DetailRegistrasi(request):
    alldetailregistrasiobj = models.DetailRegistrasi.objects.all()
    getdetailregistrasiobj = models.DetailRegistrasi.objects.get(Id_DetailRegistrasi=5)
    return render(request, 'detailregistrasiy.html', {
        "alldetailregistrasiobj" : alldetailregistrasiobj,
        "getdetailregistrasiobj" : getdetailregistrasiobj,
    })

def filterdetailregistrasi (request, id) :
    filterdetailregis = models.DetailRegistrasi.objects.filter(Id_Registrasi=id)
    return render (request, 'filteringdetailregistrasiy.html', {'filterdetailregis' : filterdetailregis})

def createdetailregistrasi(request):
    if request.method == "GET":
        allregistrasiobj = models.Registrasi.objects.all()
        allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.all()
        return render(request, 'createdetailregistrasiy.html',{
            'dataregistrasi' : allregistrasiobj, 'datakelasmata' : allkelasmatakursusobj
        })
    if request.method == "POST":
        Id_Registrasi = request.POST['Id_Registrasi']
        allregistrasiobj = models.Registrasi.objects.get(Id_Registrasi=Id_Registrasi)
        Id_Kelas_Mata_Kursus = request.POST['Id_Kelas_Mata_Kursus']
        allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.get(Id_Kelas_Mata_Kursus=Id_Kelas_Mata_Kursus)

        newdetailregistrasi = models.DetailRegistrasi(
            Id_Registrasi = allregistrasiobj,
            Id_Kelas_Mata_Kursus = allkelasmatakursusobj
        )
        newdetailregistrasi.save()

        return redirect('DetailRegistrasi')

def formdetailregistrasi(request):
    if request.method == "GET":
        allregistrasiobj = models.Registrasi.objects.all()
        allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.all()
        return render(request, 'formdetailregistrasi.html',{
            'dataregistrasi' : allregistrasiobj, 'datakelasmata' : allkelasmatakursusobj
        })
    if request.method == "POST":
        Id_Registrasi = request.POST['Id_Registrasi']
        allregistrasiobj = models.Registrasi.objects.get(Id_Registrasi=Id_Registrasi)
        Id_Kelas_Mata_Kursus = request.POST['Id_Kelas_Mata_Kursus']
        allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.get(Id_Kelas_Mata_Kursus=Id_Kelas_Mata_Kursus)

        newdetailregistrasi = models.DetailRegistrasi(
            Id_Registrasi = allregistrasiobj,
            Id_Kelas_Mata_Kursus = allkelasmatakursusobj
        )
        newdetailregistrasi.save()

        return redirect('dashboard')

def updatedetailregistrasi(request,id):
    detailregistrasiobj = models.DetailRegistrasi.objects.get(Id_DetailRegistrasi=id)
    allregistrasiobj = models.Registrasi.objects.all()
    allkelasmatakursusobj = models.Kelas_Mata_Kursus.objects.all()
    if request.method == "GET" :
        return render(request, 'updatedetailregistrasiy.html', {
            'alldetailregistrasi' : detailregistrasiobj, 'allregistrasiobj' : allregistrasiobj, 'allkelasmatakursusobj' : allkelasmatakursusobj,
        })
    else :
        getidregistrasi = models.Registrasi.objects.get(Id_Registrasi = request.POST['Id_Registrasi']) 
        getidkelas = models.Kelas_Mata_Kursus.objects.get(Id_Kelas_Mata_Kursus = request.POST['Id_Kelas_Mata_Kursus'])
        detailregistrasiobj.Id_Registrasi = getidregistrasi
        detailregistrasiobj.Id_Kelas_Mata_Kursus = getidkelas
        detailregistrasiobj.save()
        return redirect('DetailRegistrasi')

def deletedetailregistrasi(request,id):
    detailregistrasiobj = models.DetailRegistrasi.objects.get(Id_DetailRegistrasi=id)
    detailregistrasiobj.delete()
    return redirect('DetailRegistrasi') 

