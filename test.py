from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QDialog, QVBoxLayout, QPushButton, QFrame
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class GridBoardWidget(QPushButton):
    def __init__(self, board_id, parent=None):
        super().__init__(parent)
        self.board_id = board_id  # ID của bảng ô

        # Tạo layout chính cho widget
        layout = QVBoxLayout(self)
        
        # Tạo QLabel cho ký hiệu bảng
        board_label = QLabel(f"Bảng {self.board_id}")
        board_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        board_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(board_label)

        # Tạo layout lưới 3x3 cho nút
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Không khoảng cách giữa các ô

        # Font và kích thước ô
        font = QFont("Arial", 14, QFont.Weight.Bold)
        square_size = 50

        # Tạo 9 ô, mỗi ô là một QLabel
        for i in range(9):
            label = QLabel(str(i + 1))  # Hiển thị số từ 1-9
            label.setFont(font)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Tùy chỉnh giao diện: màu nền trắng, viền đen
            label.setStyleSheet("""
                background-color: white;
                border: 1px solid black;
            """)

            # Thêm ô vào layout
            row = i // 3
            col = i % 3
            grid_layout.addWidget(label, row, col)

        # Đảm bảo các ô có kích thước đồng đều trong layout
        for row in range(3):
            grid_layout.setRowStretch(row, 1)
        for col in range(3):
            grid_layout.setColumnStretch(col, 1)

        # Thêm layout lưới vào layout chính
        layout.addLayout(grid_layout)
        self.setLayout(layout)

        # Cộng thêm không gian cho label phía trên bảng
        self.setFixedSize(square_size * 3, square_size * 3 + 40)

        # Kết nối nút với sự kiện nhấn
        self.clicked.connect(self.show_popup)

    def show_popup(self):
        """Hiển thị popup khi nhấn vào bảng ô."""
        popup = QDialog(self)
        popup.setWindowTitle(f"Popup for Board {self.board_id}")

        # Tạo nội dung trong popup
        layout = QVBoxLayout(popup)
        label = QLabel(f"Bạn đã nhấn vào Bảng Ô số {self.board_id}")
        label.setFont(QFont("Arial", 12))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Thêm vào layout popup
        layout.addWidget(label)

        popup.setLayout(layout)
        popup.resize(300, 200)
        popup.exec()

class MainWidget(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Tạo layout lưới lớn 4x3
        main_layout = QGridLayout(self)
        main_layout.setSpacing(15)  # Khoảng cách giữa các bảng ô

        # Tạo 12 bảng ô
        for i in range(12):
            board = GridBoardWidget(board_id=i + 1)  # Tạo bảng ô với ID
            row = i // 4  # Dòng trong lưới lớn
            col = i % 4  # Cột trong lưới lớn
            main_layout.addWidget(board, row, col)

        # Đặt layout chính
        self.setLayout(main_layout)

# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo widget chính
    frame = MainWidget()
    frame.setWindowTitle("12 Bảng Ô với Popup")
    frame.resize(800, 600)
    frame.show()

    sys.exit(app.exec())
