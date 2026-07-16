TÀI LIỆU KIỂM THỬ UAT
Passerelles Numériques Academic Portal
Tài liệu hệ thống · Kịch bản kiểm thử · Hướng dẫn báo cáo

Hệ thống
Passerelles Numériques Academic Portal
Phiên bản tài liệu
1.0
Đối tượng
Sinh viên thực tập — UAT Team
Số module
9 modules + End-to-End
Người hướng dẫn
Thầy Vĩnh

PHẦN 1 — SƠ ĐỒ CONTEXT HỆ THỐNG
Sơ đồ này mô tả hệ thống Passerelles Numériques Academic Portal trong bối cảnh tổng thể: ai sử dụng hệ thống và hệ thống tương tác với những dịch vụ bên ngoài nào.

Người dùng hệ thống
Vai trò
Email domain
Quyền hạn
Nhân viên (Staff)
@passerellesnumeriques.org
Toàn quyền quản lý: học viên, điểm số, quan sát, thực tập, tài liệu đào tạo
Học viên (Student)
@student.passerellesnumeriques.org
Chỉ đọc: xem điểm cá nhân; submit báo cáo thực tập định kỳ

Hệ thống bên ngoài
Hệ thống
Vai trò
Ghi chú
Google Sheets
Cơ sở dữ liệu
Tất cả dữ liệu nghiệp vụ lưu trong các tab của Google Sheets
Google Drive
Lưu trữ file
Ảnh đại diện học viên, tài liệu đào tạo
Gmail
Email tự động
Gửi khi học viên nộp báo cáo thực tập (Module 6)
Google OAuth
Xác thực danh tính
Hệ thống không lưu mật khẩu — xác thực 100% qua Google

Quy trình xác thực danh tính
Người dùng truy cập URL hệ thống
↓
Google OAuth xác thực (tài khoản Google)
↓
Hệ thống kiểm tra email domain
├── @passerellesnumeriques.org → Giao diện Nhân viên (Staff Portal)
├── @student.passerellesnumeriques.org → Giao diện Học viên (Student Portal)
└── Email khác → Trang lỗi "Không có quyền truy cập"

Điểm quan trọng cho Tester

1. Không có màn hình đăng nhập riêng — hệ thống dùng tài khoản Google sẵn có.
2. Phân quyền hoàn toàn tự động — hệ thống tự nhận biết vai trò từ email domain.
3. Dữ liệu thật-thời — mọi thay đổi trên hệ thống được ghi ngay vào Google Sheets.
4. SPA (Single Page Application) — màn hình show/hide bằng JS, không reload trang.
5. Auth server-side — Session.getActiveUser() — client không thể giả mạo danh tính.
