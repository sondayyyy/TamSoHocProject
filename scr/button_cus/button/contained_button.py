from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
# from palette import palette 

class ContainedButton(QPushButton): 
    def __init__(self, theme_mode="light", disable=False):
        super().__init__()
        self.theme_mode = theme_mode  # Lưu trữ chế độ theme hiện tại
        self.disable = disable
        self.update_stylesheet()  # Cập nhật stylesheet ban đầu

        # Kích hoạt hoặc vô hiệu hoá nút
        self.setEnabled(not self.disable)
        if not self.disable:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        

    def update_stylesheet(self):
        # Đặt stylesheet động với các giá trị màu từ palette
        style = f"""
            QPushButton {{
                font-style: normal;
                font-weight: 700;
                font-size: 14px;
                font-family: "Nunito Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                color: {text_color};
                background-color: {primary_color};
                padding: 8px 16px;
                border: 2px solid {primary_color};
                border-radius: 8px;
                text-align: center;
            }}

            QPushButton:hover {{
                background-color: {hover_color};
                border-color: {primary_color};
                color: {text_color};
            }}

            QPushButton:pressed {{
                background-color: {pressed_color};
                border-color: {primary_color};
                color: {text_color}; 
            }}

            QPushButton:disabled {{
                background-color: {disabled_color};
                color: #8F8F8F;
                border-color: {disabled_color};
            }}
        """
        self.setStyleSheet(style)

    # def toggle_theme(self):
    #     # Chuyển đổi giữa "light" và "dark" và in ra để kiểm tra
    #     self.theme_mode = "dark" if self.theme_mode == "light" else "light"
    #     print(f"Chế độ theme hiện tại: {self.theme_mode}")  # Kiểm tra theme
    #     self.update_stylesheet()  # Cập nhật stylesheet sau khi chuyển theme
    #     self.repaint()  # Yêu cầu vẽ lại giao diện

# # Khởi động ứng dụng PyQt
# if __name__ == "__main__":
#     app = QApplication([])

#     # Tạo widget chính
#     window = QWidget()
#     layout = QVBoxLayout(window)

#     # Thêm nút vào layout
#     button = ContainedButton()
#     button.setText("Click to Toggle Theme")
#     layout.addWidget(button)

#     # Thiết lập và hiển thị cửa sổ
#     window.setLayout(layout)
#     window.setWindowTitle("Theme Toggle Button Example")
#     window.resize(300, 200)
#     window.show()

#     app.exec()
