from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QGridLayout, QWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-sized magic squares are supported.")
    
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2  # Bắt đầu từ hàng đầu, cột giữa
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j] != 0:
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square


class MagicSquareWidget(QWidget):
    def __init__(self, n, parent=None):
        super().__init__(parent)

        self.n = n
        self.magic_square = generate_magic_square(self.n)

        # Tạo layout dạng lưới
        layout = QGridLayout(self)
        layout.setSpacing(5)

        # Font cho các số
        font = QFont("Arial", 14, QFont.Weight.Bold)

        for i in range(self.n):
            for j in range(self.n):
                # Tạo label cho mỗi ô
                label = QLabel(str(self.magic_square[i][j]))
                label.setFont(font)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("border: 1px solid black; background-color: #f0f0f0;")
                layout.addWidget(label, i, j)

        self.setLayout(layout)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Magic Square")
        self.resize(400, 400)

        # Kích thước ma trận (n x n)
        n = 3
        magic_square_widget = MagicSquareWidget(n)

        # Tạo layout chính
        layout = QVBoxLayout()
        layout.addWidget(magic_square_widget)

        # Widget chính
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
