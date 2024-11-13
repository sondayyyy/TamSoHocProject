from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

style = '''
    QPushButton {
        font-weight: bold;
        font-size: 14px;
        font-family: "Nunito Sans", sans-serif;
        color: inherit;
        background-color: transparent;
        padding: 5px 12px;
        border-radius: 8px;
        border: 2px solid rgba(128, 128, 128, 0.32); /* Màu viền */
        text-align: center;  /* Căn giữa văn bản */
    }

    QPushButton:hover {
        background-color: rgba(128, 128, 128, 0.1); /* Hiệu ứng nền khi hover */
        color: inherit;  /* Thay đổi màu chữ khi hover */
        border-color: rgba(128, 128, 128, 0.5);  /* Thay đổi màu viền khi hover */
    }
    
    QPushButton:pressed {
        background-color: rgba(76, 175, 80, 0.2);  /* Background on press */
        color: #2E7D32;  /* Text color on press */
    }
'''


class OutlinedButton(QPushButton): 
    def __init__(self, text="Outline Button"):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(style)
        self.setCursor(Qt.PointingHandCursor)

# Khởi động ứng dụng
if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính
    window = QWidget()
    layout = QVBoxLayout(window)

    # Thêm nút vào layout
    button = OutlinedButton("Click Me")
    layout.addWidget(button)

    # Thiết lập và hiển thị cửa sổ
    window.setLayout(layout)
    window.setWindowTitle("Outline Button Example")
    window.resize(300, 200)
    window.show()

    app.exec()
