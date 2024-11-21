from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
# from palette import palette 

class ContainedButton(QPushButton): 
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
        bg_color = bg_color or "#262626"
        pressed_color = pressed_color or "#212121"
        hover_color = hover_color or "#595959"
        text_color = text_color or "#FFFFFF"
        pressed_text = pressed_text or "#999"
        hover_text = hover_text or text_color
        font_family = font_family or "Nunito Sans, Segoe UI, Arial, sans-serif"
        font_size = font_size or 14
        font_weight = font_weight or "bold"
        border_radius = border_radius or 10
        padding = padding or "6px 12px"
        border_color = border_color or "#262626"
        border_width = border_width or 10
        text_align = text_align or "center"
        margin = margin or 0

        # Trả về stylesheet
        return f"""
        QPushButton {{
            font-family: {font_family};  /* Thay đổi theo nhu cầu */
            font-weight: {font_weight};
            font-size: {font_size}px;
            color: {text_color};  /* Color of the text */
            background-color: {bg_color};  /* Transparent background */
            padding: {padding};
            border-radius: {border_radius}px;  /* Rounded corners */
            text-align: {text_align};  /* Center-align text */
            margin: {margin};
        }}
        QPushButton:hover {{
            background-color: {hover_color};
            color: {hover_text}
        }}
        QPushButton:pressed {{
            background-color: {pressed_color};
            color: {pressed_text};
        }}
        """

# Khởi động ứng dụng PyQt
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Thêm nút vào layout
    button = ContainedButton()
    button.setText("Click to Toggle Theme")
    layout.addWidget(button)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Theme Toggle Button Example")
    window.resize(300, 200)
    window.show()

    app.exec()
