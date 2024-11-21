from PySide6.QtWidgets import QApplication, QCheckBox, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor, QPaintEvent
# Định nghĩa style cho QCheckBox
style = '''
    QCheckBox::indicator {
        width: 20px; /* Kích thước ô tick */
        height: 20px;
        border: 2px solid #4A4A4A; /* Viền cho ô tick */
        border-radius: 4px;
        background-color: #FFFFFF;
    }

    QCheckBox::indicator:checked {
        background-color: #4A4A4A; /* Màu nền khi checkbox được chọn */
    }
    QCheckBox::indicator:pressed {
        background-color: #B0B0B0; /* Màu nền khi nhấn */
    }
'''

class CustomCheckBox(QCheckBox): 
    def __init__(self, disable = False):
        super().__init__()
        # self._color = color
        self.setStyleSheet(style)
        
        if disable == True:
            self.setEnabled(False)
        else:
            self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, event: QPaintEvent):
        # Vẽ checkbox chuẩn
        super().paintEvent(event)

        if self.isChecked():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            # Cài đặt Pen cho dấu tick
            pen = QPen(QColor(255, 255, 255), 2)
            painter.setPen(pen)

            # Xác định vùng để vẽ tick trong ô checkbox
            indicator_size = 18  # Kích thước của ô tick
            indicator_x = 4
            indicator_y = (self.height() - indicator_size) // 2

            # Tọa độ của dấu tick bên trong ô
            start_x = indicator_x + 3
            start_y = indicator_y + indicator_size // 2
            mid_x = indicator_x + indicator_size // 3
            mid_y = indicator_y + indicator_size - 6
            end_x = indicator_x + indicator_size - 4
            end_y = indicator_y + 4

            # Vẽ dấu tick
            painter.drawLine(start_x, start_y, mid_x, mid_y)  # Đường chéo trái
            painter.drawLine(mid_x, mid_y, end_x, end_y)      # Đường chéo phải

            painter.end()


if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Thêm nút vào layout
    button = CustomCheckBox()
    layout.addWidget(button)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Default Button Example")
    window.resize(300, 200)
    window.show()

    app.exec()