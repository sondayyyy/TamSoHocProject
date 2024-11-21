from PySide6.QtCore import Qt, QPropertyAnimation, Signal, Property, QRect
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QCheckBox, QWidget

class SwitchButton(QCheckBox):
    def __init__(self, size="normal"):
        super().__init__()

        # Thiết lập kích thước cho từng loại size
        if size == "large":
            self.setFixedSize(60, 30)
            self.circle_diameter = 24  # Kích thước hình tròn bằng với ô checkbox
            self.start_pos = 3
            self.end_pos = self.width() - self.circle_diameter - 3
        elif size == "small":
            self.setFixedSize(30, 15)
            self.circle_diameter = 11  # Kích thước hình tròn bằng với ô checkbox
            self.start_pos = 2
            self.end_pos = self.width() - self.circle_diameter - 2
        else:  # normal
            self.setFixedSize(40, 20)
            self.circle_diameter = 16  # Kích thước hình tròn bằng với ô checkbox
            self.start_pos = 2
            self.end_pos = self.width() - self.circle_diameter - 2

        self._circle_position = self.start_pos
        self.animation = QPropertyAnimation(self, b"circle_position", self)
        self.animation.setDuration(150)
        self.animation.setStartValue(self.start_pos)
        self.animation.setEndValue(self.end_pos)

        self.setCursor(Qt.PointingHandCursor)
        self.stateChanged.connect(self.start_animation)

        # Thêm biến lưu vị trí hình tròn
        self.circle_rect = QRect(self.start_pos, (self.height() - self.circle_diameter) // 2, self.circle_diameter, self.circle_diameter)

    # Khai báo Q_PROPERTY cho circle_position
    @Property(int)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.circle_rect.moveLeft(self._circle_position)
        self.update()  # Vẽ lại widget khi thay đổi vị trí vòng tròn

    def start_animation(self):
        """Kích hoạt hoạt ảnh di chuyển vòng tròn đến vị trí cuối."""
        if self.isChecked():
            self.animation.setDirection(QPropertyAnimation.Forward)
        else:
            self.animation.setDirection(QPropertyAnimation.Backward)
        self.animation.start()

    def paintEvent(self, event):
        """Sự kiện vẽ lại tùy chỉnh để render nút chuyển đổi."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Thiết lập màu nền tùy thuộc vào trạng thái của checkbox
        background_color = QColor("#4CAF50") if self.isChecked() else QColor("#BDBDBD")
        painter.setBrush(background_color)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() / 2, self.height() / 2)

        # Thiết lập màu của vòng tròn
        circle_color = QColor("#FFFFFF")
        painter.setBrush(circle_color)
        painter.drawEllipse(self.circle_rect)
        painter.end()

    def mousePressEvent(self, event):
        """Xử lý sự kiện nhấn chuột chỉ khi nhấn vào hình tròn."""
        if self.circle_rect.contains(event.pos()):  # Kiểm tra nếu nhấn vào vùng hình tròn
            self.setChecked(not self.isChecked())  # Chuyển đổi trạng thái khi nhấn vào hình tròn
            self.start_animation()  # Bắt đầu hoạt ảnh khi nhấn

        # Không gọi super().mousePressEvent để tránh thay đổi trạng thái không cần thiết
