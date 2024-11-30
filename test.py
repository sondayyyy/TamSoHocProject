from PyQt6.QtWidgets import QApplication, QVBoxLayout, QDialog, QPushButton, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QFrame, QLabel, QGridLayout
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt
import sys

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-sized magic squares are supported.")
    
    # Create an empty n x n matrix filled with 0
    magic_square = [[0] * n for _ in range(n)]
    
    # Start position (middle of the top row)
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        # Move diagonally up-right
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j] != 0:  # If the new cell is already filled, move down
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square

class GridBoardWidget(QPushButton):
    def __init__(self, board_id, n, parent=None):
        super().__init__(parent)
        self.board_id = board_id
        self.n = n  # Kích thước của Magic Square (n x n)

        # Tạo layout chính cho widget
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Tạo QLabel cho tiêu đề bảng
        board_label = QLabel(f"Bảng {self.board_id}")
        board_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        board_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(board_label)

        # Tạo layout lưới n x n cho ô
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        layout.addLayout(self.grid_layout)

        # Danh sách các QLabel để hiển thị số
        self.labels = []  # Khởi tạo danh sách rỗng

        # Font và kích thước ô
        font = QFont("Arial", 10, QFont.Weight.Bold)
        self.square_size = 45  # Kích thước mỗi ô

        # Tạo các QLabel cho từng ô trong Magic Square
        for i in range(self.n):
            for j in range(self.n):
                label = QLabel("")
                label.setFont(font)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setFixedSize(self.square_size, self.square_size)
                label.setStyleSheet("border: 1px solid black;")
                self.grid_layout.addWidget(label, i, j)
                self.labels.append(label)  # Thêm QLabel vào danh sách

        self.magic_square = generate_magic_square(self.n)  # Tạo Magic Square

        self.update_labels()  # Cập nhật giao diện ngay sau khi tạo bảng

        # Kích thước nút bao gồm tiêu đề và lưới
        total_height = self.square_size * self.n + 30
        total_width = self.square_size * self.n
        self.setFixedSize(total_width, total_height)

        # Kết nối sự kiện nhấn nút với popup
        self.clicked.connect(self.show_popup)

    def update_labels(self):
        """Cập nhật lại các giá trị trong giao diện."""
        for i in range(self.n * self.n):
            self.labels[i].setText(str(self.magic_square[i // self.n][i % self.n]))

    def set_magic_square_values(self, new_values):
        """Cập nhật giá trị cho Magic Square."""
        if len(new_values) != self.n * self.n:
            raise ValueError(f"Số lượng giá trị phải là {self.n * self.n} để cập nhật Magic Square.")

        # Chuyển các giá trị mới vào magic_square
        for i in range(self.n):
            for j in range(self.n):
                self.magic_square[i][j] = new_values[i * self.n + j]

        # Cập nhật lại giao diện sau khi thay đổi giá trị
        self.update_labels()

    def update_numbers(self, new_numbers):
        # Cập nhật các số trong bảng ô
        for i, number in enumerate(new_numbers):
            if i < len(self.labels):
                self.labels[i].setText(str(number))
            if i < len(self.rect_items):
                self.rect_items[i].setBrush(QColor("white"))  # Cập nhật màu sắc nếu cần


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

        # Tạo layout lưới 3x4 (3 hàng, 4 cột)
        main_layout = QGridLayout(self)
        main_layout.setSpacing(15)

        # Tạo 12 bảng ô, mỗi bảng có kích thước Magic Square khác nhau
        self.boards = []
        n = 3  # Kích thước Magic Square (3x3)
        for i in range(12):
            board = GridBoardWidget(board_id=i + 1, n=n)
            row = i // 4
            col = i % 4
            main_layout.addWidget(board, row, col)
            self.boards.append(board)

        # Đặt layout chính
        self.setLayout(main_layout)

        # Đảm bảo cửa sổ có đủ không gian
        # self.setFixedSize(800, 600)  # Cập nhật kích thước cửa sổ chính nếu cần

    def update_board_numbers(self, board_id, new_numbers):
        """Cập nhật số cho một bảng ô cụ thể."""  
        if 1 <= board_id <= len(self.boards):
            self.boards[board_id - 1].update_numbers(new_numbers)

    def set_magic_square_for_board(self, board_id, new_values):
        """Cập nhật giá trị cho Magic Square của một bảng cụ thể."""
        if 1 <= board_id <= len(self.boards):
            self.boards[board_id - 1].set_magic_square_values(new_values)

# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Tạo widget chính
    frame = MainWidget()
    frame.setWindowTitle("12 Magic Squares với Popup")
    frame.resize(800, 600)
    frame.show()

    # Cập nhật giá trị cho bảng 1
    frame.set_magic_square_for_board(1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    sys.exit(app.exec())
