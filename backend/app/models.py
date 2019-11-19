from django.db import models
from django.utils import timezone
# Create your models here.
SEX = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    )

STATUS = (
    ('0','Chua xac thuc'),
    ('1','Da xac thuc')
)

class Level(models.Model):
    id_level = models.AutoField(primary_key = True,auto_created=True)
    ten_level = models.CharField(max_length=50)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ten_level

class Mon_hoc(models.Model):
    id_mon = models.AutoField(primary_key=True,auto_created=True)
    ten_mon = models.CharField(max_length=100)
    ten_mon_khong_dau = models.CharField(max_length=100)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ten_mon

class Gia_su(models.Model):
    id_gia_su = models.AutoField(primary_key=True,auto_created=True)
    ho_ten = models.CharField(max_length=50)
    mat_khau= models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20,unique=True)
    gioi_tinh = models.CharField(max_length=10,choices=SEX,null=True)
    gioi_thieu = models.TextField(null=True,blank=True)
    hinh_dai_dien_url = models.URLField(null=True,blank=True)
    dia_chi = models.TextField(blank=True)
    hoc_phi_gs = models.TextField(blank=True)
    hinh_thuc_day = models.CharField(max_length=150,blank=True)
    kinh_nghiem = models.TextField(blank=True)
    so_hoc_vien = models.IntegerField(null=True)
    buoi_day = models.CharField(max_length=50,null=True)
    id_level = models.ForeignKey(Level, on_delete=models.CASCADE,blank=True, null=True)
    id_mon = models.ForeignKey(Mon_hoc, on_delete=models.CASCADE,blank=True, null=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return self.ho_ten
           

class Phu_huynh(models.Model):
    id_phu_huynh = models.AutoField(primary_key=True,auto_created=True)
    ho_ten = models.CharField(max_length=100)
    mat_khau= models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20,unique=True)
    dia_chi = models.TextField(blank=True)
    gioi_tinh_yc = models.CharField(max_length=50,choices=SEX,blank=True)
    hinh_thuc_day = models.TextField(blank=True)
    so_buoi_hoc = models.IntegerField(blank=True)
    luong_tra = models.IntegerField(blank=True)
    buoi_hoc = models.TextField(blank=True)
    id_mon = models.ForeignKey(Mon_hoc, on_delete=models.CASCADE) # cai nay la khoa ngoai
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ho_ten

class Danh_sach_lop(models.Model):
    id_lop = models.AutoField(primary_key=True,auto_created=True)
    id_mon_hoc = models.ForeignKey(Mon_hoc, on_delete=models.CASCADE)
    ten_lop = models.CharField(max_length=50)
    gia = models.FloatField()
    mo_ta = models.TextField(null=True,blank=True)
    dia_chi = models.TextField()
    id_phu_huynh = models.ForeignKey(Phu_huynh, on_delete=models.CASCADE)
    id_gia_su = models.ForeignKey(Gia_su, on_delete=models.CASCADE)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten_lop

class So_lien_lac(models.Model):
    id_sll = models.AutoField(primary_key=True,auto_created=True)
    ngay = models.DateField(auto_now=False, auto_now_add=False)
    noi_dung = models.TextField(blank=True)
    id_lop = models.ForeignKey(Danh_sach_lop, on_delete=models.CASCADE)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)

class Danh_gia(models.Model):
    id_danh_gia = models.AutoField(primary_key = True,auto_created=True)
    diem = models.FloatField()
    mo_ta = models.TextField(blank=True)
    id_phu_huynh = models.ForeignKey(Phu_huynh, on_delete=models.CASCADE,blank=True, null=True)
    id_gia_su = models.ForeignKey(Gia_su, on_delete=models.CASCADE)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.diem

class Binh_luan(models.Model):
    id_binh_luan = models.AutoField(primary_key = True,auto_created=True)
    binh_luan = models.TextField()
    id_phu_huynh = models.ForeignKey(Phu_huynh, on_delete=models.CASCADE,blank=True)
    id_gia_su = models.ForeignKey(Gia_su, on_delete=models.CASCADE, blank=True)
    id_lop = models.ForeignKey(Danh_sach_lop, on_delete=models.CASCADE,blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)
    
class Lop_yeu_cau(models.Model):
    id_lop = models.AutoField(primary_key=True,auto_created=True)
    id_phu_huynh  = models.ForeignKey(Phu_huynh, on_delete=models.CASCADE) 
    trang_thai = models.CharField(max_length=20, choices = STATUS)## trang thai da nhan hay chua 
    mo_ta = models.TextField(null=True)
    hinh_thuc_day = models.CharField(max_length=150,null=True)
    id_gia_su = models.ForeignKey(Gia_su, on_delete=models.CASCADE)
    id_mon_hoc = models.ForeignKey(Mon_hoc, on_delete=models.CASCADE)
    yeu_cau_gioi_tinh = models.CharField(max_length=50,choices=SEX,null=True)
    ghi_chu = models.TextField(null=True)
    so_buoi_hoc = models.IntegerField(null=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_chinh_sua = models.DateTimeField(auto_now=True)
