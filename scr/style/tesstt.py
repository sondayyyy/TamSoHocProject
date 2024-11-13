from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from globalStyle import Palette
from effects import Shadows
from scr.style.typography_ import Typography


def get_button_style(palette, shadows, typography):
    # Lấy màu sắc từ theme
    primary_color = palette.Primary.main()
    disabled_color = palette.Primary.indigo()
    disabled_background = palette.Primary.grey()
    disabled_border = disabled_background
    text_color = palette.Primary.contrastText()
    border_color = primary_color

    # Lấy màu hover và pressed động từ primary_color
    hover_color, pressed_color = palette.Action.get_dynamic_action_colors(primary_color)

    # Lấy thiết lập typography
    font_family = typography.fontFamily_01()
    font_Weight = typography.fontWeightBold()
    font_size = typography.button()["fontSize"]

    # Định nghĩa style cho nút
    style = f'''
        QPushButton {{
            font-style: normal;
            font-weight: {font_Weight};
            font-size: {font_size};
            font-family: {font_family};
            color: {text_color};  /* Màu chữ */
            background-color: {primary_color};  /* Màu nền */
            padding: 8px 16px;
            border: 2px solid {border_color};  /* Màu viền */
            border-radius: 8px;  /* Bo góc */
            text-align: center;
        }}

        QPushButton:hover {{
            background-color: {hover_color};  /* Màu hover */
            border-color: {border_color};  /* Viền khi hover */
            color: {text_color};  /* Giữ màu chữ */
        }}

        QPushButton:pressed {{
            background-color: {pressed_color};  /* Màu khi nhấn */
            border-color: {border_color};  /* Viền khi nhấn */
            color: {text_color};  /* Giữ màu chữ */
        }}

        QPushButton:disabled {{
            background-color: {disabled_background};  /* Màu nền khi vô hiệu hóa */
            color: {disabled_color};  /* Màu chữ khi vô hiệu hóa */
            border-color: {disabled_border};
        }}
    '''
    return style



class ContainedButton(QPushButton):
    def __init__(self, theme, shadows, typography, disable=False):
        super().__init__()
        # Áp dụng style nút động dựa trên theme, shadows và typography
        self.setStyleSheet(get_button_style(theme, shadows, typography))
        if disable:
            self.setEnabled(False)
        else:
            self.setCursor(Qt.PointingHandCursor)


# Khởi tạo shadows, typography và palette
shadows = Shadows()
typography = Typography()
palette = Palette()

# Cấu hình ứng dụng PyQt
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Tạo và thêm ContainedButton vào layout
    button = ContainedButton(palette, shadows, typography)
    button.setText("Click Me")
    layout.addWidget(button)

    # Cấu hình và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Button with Dynamic Theme")
    window.resize(300, 200)
    window.show()

    app.exec()
