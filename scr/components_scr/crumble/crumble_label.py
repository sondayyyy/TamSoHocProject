from PySide6.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Breadcrumb(QWidget):
    def __init__(self, paths):
        super().__init__()
        
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)  # `gap` giữa các mục breadcrumb
        self.layout.setAlignment(Qt.AlignLeft)
        
        # Tạo font chung cho các mục breadcrumb
        font = QFont("Arial", 10)
        
        for i, path in enumerate(paths):
            # Tạo QLabel cho từng mục breadcrumb
            label = QLabel(path)
            label.setFont(font)
            label.setStyleSheet("color: #555555; text-decoration: none;")
            
            self.layout.addWidget(label)

            # Thêm ">" giữa các mục breadcrumb, trừ mục cuối cùng
            if i < len(paths) - 1:
                separator = QLabel(">")
                separator.setFont(font)
                separator.setStyleSheet("color: #AAAAAA;")
                self.layout.addWidget(separator)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])

    # Tạo widget chính và thiết lập breadcrumb
    window = QWidget()
    layout = QHBoxLayout(window)

    paths = ["Home", "Products", "Electronics", "Laptops"]
    breadcrumb = Breadcrumb(paths)

    layout.addWidget(breadcrumb)

    window.setLayout(layout)
    window.setWindowTitle("Breadcrumb Example")
    window.resize(400, 100)
    window.show()

    app.exec()
