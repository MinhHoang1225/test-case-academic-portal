NGUYÊN TẮC VIẾT TEST CASE

1. Mục đích

- Định nghĩa rõ ràng mục tiêu kiểm thử.
- Bảo đảm bước kiểm thử có thể thực hiện được bởi tester và dễ xác nhận kết quả.
- Dễ dàng so sánh giữa kết quả thực tế và kết quả mong đợi.

2. Định nghĩa một test case
   Mỗi test case là một kịch bản kiểm thử độc lập, có cấu trúc rõ ràng, gồm:

- ID duy nhất
- Module liên quan
- Tên / tiêu đề ngắn gọn
- Mục tiêu kiểm thử
- Tiền điều kiện
- Dữ liệu kiểm thử
- Các bước thực hiện
- Kết quả mong đợi
- Mức độ ưu tiên
- Ghi chú bổ sung

3. Trường thông tin bắt buộc

- ID: theo định dạng TC-Mx-yy (ví dụ TC-M1-01)
- Module: Module 1..9 hoặc End-to-End
- Tên test case: mô tả chức năng cần kiểm thử
- Mục tiêu: lý do test case này tồn tại
- Tiền điều kiện: trạng thái ban đầu cần có
- Dữ liệu kiểm thử: dữ liệu đầu vào, user, batch, giá trị mẫu
- Các bước thực hiện: từng bước chi tiết theo thứ tự
- Kết quả mong đợi: hành vi hoặc thông điệp chính xác
- Mức độ ưu tiên: Cao / Trung bình / Thấp
- Trạng thái / Ghi chú: ghi thêm thông tin điều kiện, giả định, lỗi tạm thời

4. Nguyên tắc viết

- Viết ngắn gọn, rõ ràng, dùng câu mệnh lệnh.
- Mỗi bước chỉ mô tả một hành động.
- Kết quả mong đợi phải định lượng được, không chung chung.
- Tránh dùng từ "kiểm tra" hoặc "xác nhận" trong bước thực thi.
- Dùng dữ liệu thực tế hoặc dữ liệu mẫu rõ ràng.

5. Quy tắc đặt tên file
   Các test case cùng module ghi trong cùng một file CSV nằm trong thư mục Tests.

- Tests/module1_test_cases.csv
- Tests/module2_test_cases.csv
- Tests/module3_test_cases.csv

6. Định dạng CSV
   File CSV phải có header và mỗi dòng là một test case.
   Header đề xuất:
   ID,Module,Title,Objective,Precondition,TestData,Steps,ExpectedResult,Priority,Notes

- Các bước thực hiện (`Steps`) có thể tách bằng `;` hoặc dấu ngắt dòng bên trong ô CSV được đóng trong dấu ngoặc kép.
- Dữ liệu kiểm thử (`TestData`) có thể viết dưới dạng `key=value` cách nhau bằng `;`.
- Nếu giá trị chứa dấu phẩy, dùng dấu ngoặc kép để bao toàn bộ ô.

7. Ví dụ file CSV cho Module 1
   ID,Module,Title,Objective,Precondition,TestData,Steps,ExpectedResult,Priority,Notes
   TC-M1-01,Module 1,Tạo khóa học mới với mã batch hợp lệ,Kiểm tra tạo batch mới khi tên batch hợp lệ,Staff đã đăng nhập ở trang Quản lý Khóa học,"Tên khóa học=PNV26A;Trạng thái=Active","1. Nhấn Tạo khóa học mới;2. Nhập PNV26A;3. Chọn Active;4. Nhấn Lưu","Hiển thị thông báo thành công và batch PNV26A xuất hiện trong danh sách",Cao,Tên batch phải theo quy tắc PNVyyX
   TC-M1-02,Module 1,Không tạo được khóa học khi tên batch sai định dạng,Kiểm tra validate tên batch khi nhập định dạng sai,Staff đã đăng nhập ở trang Quản lý Khóa học,"Tên khóa học=PNV26;Trạng thái=Active","1. Nhấn Tạo khóa học mới;2. Nhập PNV26;3. Chọn Active;4. Nhấn Lưu","Hiển thị thông báo lỗi định dạng tên khóa học",Cao,Định dạng hợp lệ là PNVyyX
