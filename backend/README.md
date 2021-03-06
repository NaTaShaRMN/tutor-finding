# Back-end

- Ngôn ngữ: Python 3
- Framework: Django 2.2

## Thành viên:
  1. Kiều Thanh Phong
  2. Kiều Chí Công
  3. Nguyễn Anh Tuấn
  4. Mai Thành Đạt

## Tiến độ api

- [x] Đăng ký tài khoản gia sư
- [x] Đăng nhập tài khoản gia sư
- [x] Lấy danh sách gia sư
- [x] Lấy thông tin gia sư theo id
- [x] Tạo danh sách môn học
- [x] Lấy danh sách tất cả môn học
- [x] Đăng ký tài khoản học sinh
- [x] Mở lớp cần tìm gia sư
- [dat] Đăng nhập tài khoản học sinh
- [ ] Lấy danh sách gia sư theo địa điểm, theo môn, theo lớp
- [ ] Chấp nhận yêu cầu nhận lớp của gia sư cho một lớp cần tìm gia sư
- [ ] Chấp nhận lời mời dạy của học học sinh
- [ ] Tạo, sửa, ẩn, hiện thông tin cho lớp cần tìm gia sư
- [dat] Lấy danh sách lớp cần tìm gia sư(lấy theo page, lấy tất cả)
- [dat] Lấy danh sách gia sư(lấy theo page, lấy tất cả)
- [ ] Tạo yêu cầu nhận lớp (Gia sư tạo yêu cầu đến cho học sinh)
- [ ] Tạo yêu cầu nhận mời gia sư (học sinh tạo yêu cầu mời gia sư dạy đối với các lớp mà học sinh đã tạo)
- [dat] Cập nhật tài khoản gia sư (update các thông tin cá nhân của gia sư)
- [dat] Cập nhật tài khoản học sinh (update các thông tin cá nhân học sinh)




## Các lệnh cần thiết 
  - **Chú ý**: 
    - Cài docker và docker-compose

    - Các lệnh để chạy project:
  ```python
        dockerd #start docker
        cd backend # move to folder to work 
        docker-compose build # build image(only build 1 time if no change in docker-compose))
        docker-compose run web bash -c "python manage.py makemigrations app && python manage.py migrate" #migrate database
        docker-compose up # start container (server) and wait fews minutes 
        docker-compose down # stop container (server) 
        mysql -P $8000 --protocol=tcp -u root -p #access to database if want(password is password)
  ```
    - Mở trình duyệt và vào *http://localhost:8000/docs* để xem api doc

## Nhiệm vụ:
  ### 1. Kết nối DB và query:
    - Cách kết nối và thao tác với DB<Có thể có thêm yêu cầu sau>.
    - Thống nhất với frontend về dữ liệu đầu ra của API.
  ### 2. Viết API:
    - Mỗi phần làm API cho cả gia sư và học sinh(mọi người có thể gắn tag để dễ quản lý):
      + Đăng ký tài khoản
      + Chỉnh sửa hồ sơ
      + Xóa hồ sơ
    - API chung:
      + Lấy danh sách lớp
      + Lấy thông tin lớp học
      + Lấy danh sách gia sư
      + Lấy thông tin gia sư

    - API riêng:
      + Chấp nhận gia sư (Học sinh)
      + Đánh giá gia sư (Học sinh)
      + Tạo yêu cầu nhận lớp (Gia sư)
      + Phê duyệt, quản lý  tài khoản (Admin)

## Cách thực hiện
   

   ### Phần 1: Kết nối DB và query: 1 thành viên
      Nguyễn Anh Tuấn
      Link hương dan ket noi django to myyql : https://www.youtube.com/watch?v=jo9jZ1GKFmw
   ### Phần 2: Viêt API: 3 thành viên
      Các API được liệt kê trong danh sách, thành viên chọn 1 API bất kỳ, gạch tên API đó đi 
      (để thành viên khác biết) và hoàn thành nó. Tiếp tục làm thế với các API còn lại.
      - Kiều Thanh Phong: + Đăng ký tài khoản
                          + Chỉnh sửa hồ sơ
                          + Xóa hồ sơ
      - Kiều Chí Công:    + Lấy danh sách gia sư
                          + Lấy thông tin gia sư
                          + Chấp nhận gia sư (Học sinh)
      - Mai Thành Đạt:    + Lấy danh sách lớp
                          + Lấy thông tin lớp học
                          + Đánh giá gia sư (Học sinh)
                          + Tạo yêu cầu nhận lớp (Gia sư)




