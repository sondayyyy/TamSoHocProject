from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout


class TextButton(QPushButton): 
    def __init__(self, text="", parent=None, **kwargs):
        super().__init__(text, parent)
        # Nhận các tham số tùy chỉnh và áp dụng stylesheet
        self.setStyleSheet(self.get_stylesheet(**kwargs))

    @staticmethod
    def get_stylesheet(
        bg_color=None,  # Màu nền mặc định
        text_color=None,  # Màu chữ mặc định
        font_family=None,  # Font chữ
        hover_color=None,  # Màu nền khi hover
        hover_text=None,  # Màu nền khi hover
        pressed_color=None,  # Màu nền khi nhấn
        pressed_text=None,  # Màu nền khi nhấn
        font_size=None,  # Kích thước font
        font_weight=None,  # Độ đậm chữ
        border_radius=None,  # Bo góc
        padding=None,  # Padding
        border_color=None,  # Màu viền
        border_width=None,  # Độ dày viền
        text_align=None,  # Căn chỉnh văn bản
        margin=None  # Căn chỉnh văn bản
    ):
        # Gán giá trị mặc định
        bg_color = bg_color or "None"
        pressed_color = pressed_color or "None"
        hover_color = hover_color or "None"
        text_color = text_color or "#4CAF50"
        font_family = font_family or "Nunito Sans, Segoe UI, Arial, sans-serif"
        hover_text = hover_text or "#388E3C"
        pressed_text = pressed_text or "#2E7D32"
        font_size = font_size or 14
        font_weight = font_weight or "bold"
        border_radius = border_radius or 10
        padding = padding or "6px 12px"
        border_color = border_color or "None"
        border_width = border_width or 0
        text_align = text_align or "center"
        margin = margin or 0

        # Trả về stylesheet
        return f"""
        QPushButton {{
            font-family: {font_family};  /* Thay đổi theo nhu cầu */
            font-weight: {font_weight};
            font-size: {font_size}px;
            line-height: 1.7;
            color: {text_color};  /* Color of the text */
            background-color: {bg_color};  /* Transparent background */
            padding: {padding};
            border: {border_width}px solid {border_color};  /* No border */
            border-radius: {border_radius}px;  /* Rounded corners */
            text-align: {text_align};  /* Center-align text */
            margin: {margin};
        }}
        QPushButton:hover {{
            background-color: {hover_color};
            color: {hover_text};  /* Text color on hover */
        }}
        QPushButton:pressed {{
            background-color: {pressed_color};
            color: {pressed_text};
        }}
        """

# Khởi động ứng dụng
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Thêm nút vào layout
    button = TextButton("Click Me")
    layout.addWidget(button)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Outline Button Example")
    window.resize(300, 200)
    window.show()

    app.exec()
