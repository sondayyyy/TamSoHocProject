from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


class SearchLineEdit(QLineEdit):
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
        text_color=None,
        placeholder_color=None,
        hover_border_color=None,
        focus_border_color=None,
    ):
        # Gán giá trị mặc định
        font_size = font_size or 14
        padding = padding or "8px"
        border_radius = border_radius or 8
        border_color = border_color or "transparent"
        bg_color = bg_color or "#f3f3f4"
        text_color = text_color or "#0d0c22"
        placeholder_color = placeholder_color or "#9e9ea7"
        hover_border_color = hover_border_color or "#b3b3b3"
        focus_border_color = focus_border_color or "#949494"

        # Trả về stylesheet
        return f"""
        QLineEdit {{
            font-size: {font_size}px;
            padding: {padding};
            border: 2px solid {border_color};
            border-radius: {border_radius}px;
            background-color: {bg_color};
            color: {text_color};
        }}
        QLineEdit::placeholder {{
            color: {placeholder_color};
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

    # Tạo và thêm StyledLineEdit vào layout
    input_field = StyledLineEdit("Enter text here"
    )
    input_field2 = StyledLineEdit("Enter text here"
    )
    layout.addWidget(input_field)
    layout.addWidget(input_field2)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Styled LineEdit Example")
    window.resize(400, 150)
    window.show()

    app.exec()

