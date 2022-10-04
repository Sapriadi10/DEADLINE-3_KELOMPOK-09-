#from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('kelasmatakursus', views.kelasmatakursus,name='kelasmatakursus'),
    path('createkelasmatakursus', views.createkelasmatakursus,name='createkelasmatakursus'),
    path('updatekelasmatakursus/<str:id>', views.updatekelasmatakursus,name='updatekelasmatakursus'),
    path('deletekelasmatakursus/<str:id>', views.deletekelasmatakursus,name='deletekelasmatakursus'),
    path('registrasi', views.registrasi, name='registrasi'),
    path('createregistrasi', views.createregistrasi, name='createregistrasi'),
    path('updateregistrasi/<str:id>', views.updateregistrasi, name='updateregistrasi'),
    path('CustomerService', views.CustomerService,name='CustomerService'),
    path('createCustomerService', views.createCustomerService, name='createCustomerService'),
    path('updateCustomerService/<str:id>', views.updateCustomerService, name='updateCustomerService'),
    path('deleteCustomerService/<str:id>', views.deleteCustomerService,name='deleteCustomerService'),
    path('siswa', views.siswa,name='siswa'),
    path('createsiswa', views.createsiswa,name='createsiswa'),
    path('updatesiswa/<str:id>', views.updatesiswa, name='updatesiswa'),
    path('deletesiswa/<str:id>', views.deletesiswa,name='deletesiswa'),
    path('DetailRegistrasi', views.DetailRegistrasi, name='DetailRegistrasi'),
    path('createdetailregistrasi', views.createdetailregistrasi, name='createdetailregistrasi'),
    path('deletedetailregistrasi/<str:id>', views.deletedetailregistrasi, name='deletedetailregistrasi'),
    path('updatedetailregistrasi/<str:id>', views.updatedetailregistrasi, name='updatedetailregistrasi'),
    path('deleteregistrasi/<str:id>', views.deleteregistrasi, name='deleteregistrasi'),
    path('Full stack Web Developer', views.FullstackWebDeveloper, name='FullstackWebDeveloper'),
    path('UIUXDesignandProducManagement', views.UIUXDesignandProducManagement, name='UIUXDesignandProducManagement'),
    path('GraphicandMotionDesign', views.GraphicandMotionDesign, name='GraphicandMotionDesign'),
    path('DigitalMarketing', views.DigitalMarketing, name='DigitalMarketing'),
    path('home',views.dashboard,name='dashboard')
    ]