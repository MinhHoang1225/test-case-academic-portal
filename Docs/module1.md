MODULE 1 · Quản lý Khóa học & Học viên

Module này cho phép nhân viên tạo và quản lý các khóa học (batch) và hồ sơ học viên. Đây là nền tảng của toàn bộ hệ thống — mọi dữ liệu khác (điểm số, quan sát, thực tập) đều gắn với học viên và khóa học được quản lý ở đây.

Chức năng chính

1.1 Quản lý Khóa học (Batch)
Tạo khóa học: phải đúng định dạng PNVyyX (ví dụ PNV26A, PNV25B).
Sửa tên khóa học; bật/tắt trạng thái Active/Inactive.
Lưu trữ khóa học: đặt Active = false (không có xóa vĩnh viễn).
1.2 Quản lý Học viên (Student)
Thêm học viên đơn lẻ hoặc hàng loạt (bulk / CSV upsert).
Sửa thông tin: tên, mã học viên, ngày sinh, giới tính, email, ảnh đại diện.
Đánh dấu Follow-up (cờ ⚑), thay đổi trạng thái Active/Inactive.
Tìm kiếm real-time theo tên; lọc theo đánh giá quan sát; phân trang 10/trang.

Quy tắc nghiệp vụ
Chi tiết
Định dạng tên khóa học
Phải theo định dạng PNVyyX (yy=năm, X=chữ in hoa). Lỗi nếu sai.
Tên khóa học
Duy nhất trong toàn hệ thống (không phân biệt hoa/thường)
Mã học viên (student code)
Duy nhất toàn hệ thống (không phân biệt hoa/thường)
Status → Inactive
Ngày nghỉ học tự động điền ngày hiện tại
Status → Active
Ngày nghỉ học tự động xóa
Xóa vĩnh viễn
KHÔNG có — chỉ lưu trữ (inactive)

Thông báo lỗi cần biết (Module 1)
"Invalid batch name. Use format PNVyyX (e.g., PNV26A)" → tên khóa sai định dạng
"A batch named \"PNV26A\" already exists" → tên khóa trùng
"Duplicate student code: {code}" → mã học viên trùng (bulk)
"Server is busy. Please try again in a moment." → server quá tải
