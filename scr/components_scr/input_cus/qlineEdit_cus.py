from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout 
from PySide6.QtCore import Qt


class CustomLineEdit(QLineEdit):
    def __init__(self, placeholder_text="", parent=None, **kwargs):
        super().__init__(parent)
        self.setPlaceholderText(placeholder_text)
        # Nhận các tham số tùy chỉnh và áp dụng stylesheet
        self.setStyleSheet(self.get_stylesheet(**kwargs))

    @staticmethod
    def get_stylesheet(
        font_size=None,
        padding=None,
        border_radius=None,
        border_color=None,
        bg_color=None,
        hover_border_color=None,
        focus_border_color=None,
    ):
        # Gán giá trị mặc định
        font_size = font_size or 14
        padding = padding or "6px 16px"
        border_radius = border_radius or 10
        border_color = border_color or "#d1d5db"
        bg_color = bg_color or "#f3f4f6"
        hover_border_color = hover_border_color or "#93c5fd"
        focus_border_color = focus_border_color or "#60a5fa"

        # Trả về stylesheet
        return f"""
        QLineEdit {{
            font-size: {font_size}px;
            padding: {padding};
            border: 1px solid {border_color};
            border-radius: {border_radius}px;
            background-color: {bg_color};
        }}
        QLineEdit:hover {{
            border-color: {hover_border_color};
        }}
        QLineEdit:focus {{
            border-color: {focus_border_color};
            outline: none;
        }}
        """

# Khởi động ứng dụng PyQt
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Tạo và thêm CustomLineEdit vào layout
    input_field = CustomLineEdit(
        placeholder_text="Enter text here"
    )
    layout.addWidget(input_field)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Custom LineEdit Example")
    window.resize(400, 150)
    window.show()

    app.exec()