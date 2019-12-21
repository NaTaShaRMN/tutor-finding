
from django.shortcuts import get_object_or_404
from  django.contrib.auth import hashers
import coreapi
import coreschema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.schemas import ManualSchema
from django.core.paginator import Paginator
from rest_framework_jwt.settings import api_settings

from app.models import Gia_su
from app.serializers.ser_tutor import SerTutors, SerTutor
import jwt



class TutorList(APIView):

    """
    get:
     Trả về danh sách các gia sư mặc định
    """

    def get(self, request):
        tutors = Gia_su.objects.all()
        tutorSerializer = SerTutors(tutors, many=True)
        return Response(
            {
                "success": True,
                "tutors": tutorSerializer.data
            }
        )


class AuthTutor(APIView):
    # view cho xác thực tài khoản

    schema=ManualSchema(fields=[
        coreapi.Field(
            "phone",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "mat_khau",
            required=True,
            location="form",
            schema=coreschema.String()
        ),

    ])
    def post(seft, request):
        phone = request.data['phone']
        mat_khau = request.data['mat_khau']

       
        try:
           gia_su = Gia_su.objects.get(phone=phone)
        except Exception as e:
            print("Error:",e)
            return Response({"success": False, "message": "Tài khoản không tồn tại"})

        if hashers.SHA1PasswordHasher().verify(mat_khau,gia_su.mat_khau):
            tutorSerializer = SerTutors(gia_su)
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER(tutorSerializer.data)
            return Response({"success": True,"token": jwt_encode_handler,"role":gia_su.role, "data":tutorSerializer.data} )
        else:
            return Response({"success": False,"message": "Tài khoản hoặc mật khẩu không đúng"})


class Tutor(APIView):
    # view for TuTor
    schema=ManualSchema(fields=[
        coreapi.Field(
            "ho_ten",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "email",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "mat_khau",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "phone",
            required=True,
            location="form",
            schema=coreschema.String()
        )])
    def post(self, request):
        ho_ten=request.data['ho_ten']
        email=request.data['email']
        mat_khau=request.data['mat_khau']
        phone=request.data['phone']
        hinh_dai_dien_url='https://api.adorable.io/avatar/200/account'
        role=1

        tutor_serializer=SerTutor(
            data={
                    "ho_ten": ho_ten,
                    "mat_khau": mat_khau,
                    "email": email,
                    "phone": phone,
                    "hinh_dai_dien_url": hinh_dai_dien_url,
                    "role":role

                })
        try:
            if tutor_serializer.is_valid():
                try:
                    tutor_serializer.save()
                    return Response({"success": True, "message": "Đăng kí thành công ", "data":tutor_serializer.data}, status.HTTP_200_OK)
                except Exception as e:
                    print("Error:", e)
                    return Response({"success": False, "message": "Số điện thoại đã tồn tại"}, status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
               print(tutor_serializer.errors)
               return Response({"success": False, "message":" tutor_serializer.errors"}, 400)
        except Exception as e:
            print("Error:", e)
            return Response({"success": False, "message": "Lỗi hệ thống"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateTutor(APIView):
    # view for TuTor

    schema=ManualSchema(fields=[
        coreapi.Field(
            "id_gia_su",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "ho_ten",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "email",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "mat_khau",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "hinh_dai_dien_url",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "gioi_thieu",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "gioi_tinh",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "dia_chi",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "hoc_phi_gs",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "hinh_thuc_day",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "kinh_nghiem",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
         coreapi.Field(
            "buoi_day",
            # required=True,
            location="form",
            schema=coreschema.String()
        ),
        ])
    def post(self, request):
        id_gia_su= request.data['id_gia_su']
        tutor=Gia_su.objects.get(id_gia_su=id_gia_su)
        old_tutor =  Gia_su.objects.get(id_gia_su=id_gia_su)
        print("request data:", request.data)

        if ("ho_ten" in request.data and(request.data['ho_ten']!='')) :
            ho_ten=request.data['ho_ten']
            tutor.ho_ten= ho_ten
              
        if ("email" in request.data and(request.data['email']!='')):
            email=request.data['email']
            tutor.email = email

        if ("mat_khau" in request.data and(request.data['mat_khau']!='')):
            mat_khau=hashers.SHA1PasswordHasher().encode(request.data['mat_khau'],salt='123')
            tutor.mat_khau = mat_khau

        if ("hinh_dai_dien_url" in request.data and(request.data['hinh_dai_dien_url']!='')):
            hinh_dai_dien_url=request.data['hinh_dai_dien_url']
            tutor.hinh_dai_dien_url = hinh_dai_dien_url

        if  ("gioi_thieu" in request.data and(request.data['gioi_thieu']!='')):
            gioi_thieu = request.data['gioi_thieu']
            tutor.gioi_thieu= gioi_thieu

        if  ("gioi_tinh" in request.data and(request.data['gioi_tinh']!='')):
            gioi_tinh = request.data['gioi_tinh']
            tutor.gioi_tinh = gioi_tinh

        if ("dia_chi" in request.data and(request.data['dia_chi']!='')):
            dia_chi= request.data['dia_chi']
            tutor.dia_chi= dia_chi

        if ("hoc_phi_gs" in request.data and(request.data['hoc_phi_gs']!='')):
            hoc_phi_gs = request.data['hoc_phi_gs']
            tutor.hoc_phi_gs = hoc_phi_gs

        if ("hinh_thuc_day" in request.data and(request.data['hinh_thuc_day']!='')):
            hinh_thuc_day= request.data['hinh_thuc_day']
            tutor.hinh_thuc_day= hinh_thuc_day

        if ("kinh_nghiem" in request.data and(request.data['kinh_nghiem']!='')):
            kinh_nghiem = request.data['kinh_nghiem']
            tutor.kinh_nghiem = kinh_nghiem

        if ("buoi_day" in request.data and(request.data['buoi_day']!='')):
            buoi_day = request.data['buoi_day']
            tutor.buoi_day = buoi_day    
                    
            
        try:
            try:
                tutor.save()
                return Response({"success": True, "message": "Cập nhập thành công ", "old_value":SerTutor(old_tutor).data, "new_value":SerTutor(tutor).data}, status.HTTP_200_OK)
            except Exception as e:
                print("Error:", e)
                return Response({"success": False, "message": e}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print("Error:", e)
            return Response({"success": False, "message": "Lỗi hệ thống"}, status.HTTP_500_INTERNAL_SERVER_ERROR)



class TutorDetail(APIView):
    """
    get:
     Trả về thông tin chi tiết của 1 gia sư
    """
    def get(self, request, id):
        tutor=Gia_su.objects.get(id_gia_su=id)
        tutorDetailSerializer=SerTutor(tutor)
        return Response(
            {
                "success": True,
                "data": tutorDetailSerializer.data
            }
        )

class TutorListPage(APIView):
    
    "Lấy danh sách các lớp theo page"
    def get(self, request, page):
        """
        get:
        Trả về danh sách theo page
        """
        tutor = Gia_su.objects.all()
        paginator = Paginatand(tutor,10)
        listTutor= paginator.get_page(page)
        listTutorSerializer = SerTutor(listTutor, many=True)

        return Response(
            {
                "success":True,
                "data":listTutorSerializer.data
            }
        )        
