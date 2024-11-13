from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor


style = '''
    QPushButton {
        font-family: "Nunito Sans", "Segoe UI", Arial, sans-serif;  /* Thay đổi theo nhu cầu */
        font-weight: bold;
        font-size: 14px;
        line-height: 1.7;
        color: #4CAF50;  /* Color of the text */
        background-color: transparent;  /* Transparent background */
        padding: 6px 8px;
        border: none;  /* No border */
        border-radius: 8px;  /* Rounded corners */
        text-align: center;  /* Center-align text */
        margin: 0;
    }

    QPushButton:hover {
        background-color: rgba(76, 175, 80, 0.1);  /* Background on hover */
        color: #388E3C;  /* Text color on hover */
    }

    QPushButton:pressed {
        background-color: rgba(76, 175, 80, 0.2);  /* Background on press */
        color: #2E7D32;  /* Text color on press */
    }
'''

class TextButton(QPushButton): 
    def __init__(self, text="Outline Button"):
        super().__init__()
        self.setText(text)
        self.setStyleSheet(style)
        self.setCursor(Qt.PointingHandCursor)

# # Khởi động ứng dụng
# if __name__ == "__main__":
#     app = QApplication([])

#     # Tạo widget chính
#     window = QWidget()
#     layout = QVBoxLayout(window)

#     # Thêm nút vào layout
#     button = TextButton("Click Me")
#     layout.addWidget(button)

#     # Thiết lập và hiển thị cửa sổ
#     window.setLayout(layout)
#     window.setWindowTitle("Outline Button Example")
#     window.resize(300, 200)
#     window.show()

#     app.exec()
