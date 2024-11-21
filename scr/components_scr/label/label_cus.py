from PySide6.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class CustomLabel(QLabel):
    def __init__(self, text="", parent=None, **kwargs):
        super().__init__(text, parent)
        # Áp dụng stylesheet từ các tham số đầu vào
        self.setStyleSheet(self.get_stylesheet(**kwargs))
        self.setAlignment(Qt.AlignCenter)

    @staticmethod
    def get_stylesheet(
        bg_color=None,    # Màu nền
        text_color=None,  # Màu chữ
        font_size=None,   # Kích thước font
        font_weight=None, # Độ đậm font
        border_radius=None,  # Bo góc
        padding=None,     # Khoảng cách bên trong
        border_color=None,  # Màu viền
        border_width=None,   # Độ dày viền
        text_align=None,  # Căn chỉnh văn bản

    ):
        # Giá trị mặc định
        bg_color = bg_color or "transparent"
        text_color = text_color or "#000000"
        font_size = font_size or 14
        font_weight = font_weight or "normal"
        border_radius = border_radius or 0
        padding = padding or "4px"
        border_color = border_color or "transparent"
        border_width = border_width or 0
        text_align = text_align or "center",  # Căn chỉnh văn bản


        return f"""
        QLabel {{
            background-color: {bg_color};
            color: {text_color};
            font-size: {font_size}px;
            font-weight: {font_weight};
            border-radius: {border_radius}px;
            padding: {padding};
            border: {border_width}px solid {border_color};
            text-align: {text_align}
        }}
        """
    
# Khởi động ứng dụng
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Thêm nút vào layout
    button = CustomLabel("Click Me")
    layout.addWidget(button)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Outline Button Example")
    window.resize(300, 200)
    window.show()

    app.exec()
