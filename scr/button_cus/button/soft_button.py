from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt


style = '''
    QPushButton {
        font-family: "Nunito Sans", "Segoe UI", Arial, sans-serif;  /* Font */
        font-weight: bold;
        font-size: 14px;
        line-height: 1.7;
        color: #333333;  /* Text color */
        background-color: rgba(128, 128, 128, 0.08);  /* Soft background */
        padding: 6px 12px;
        border: none;  /* No border */
        border-radius: 8px;  /* Rounded corners */
        margin: 0;
        text-align: center;
    }

    QPushButton:hover {
        background-color: rgba(128, 128, 128, 0.15);  /* Darker background on hover */
        color: #222222;  /* Slightly darker text on hover */
    }

    QPushButton:pressed {
        background-color: rgba(128, 128, 128, 0.25);  /* Even darker background on press */
        color: #111111;  /* Darker text on press */
    }
'''

class SoftButton(QPushButton): 
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
#     button = SoftButton("Click Me")
#     layout.addWidget(button)

#     # Thiết lập và hiển thị cửa sổ
#     window.setLayout(layout)
#     window.setWindowTitle("Outline Button Example")
#     window.resize(300, 200)
#     window.show()

#     app.exec()