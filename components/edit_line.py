from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        
    def setup_name_edit(self):
        self.setMaxLength(50)  # Giới hạn số ký tự
        # Thiết lập validator cho tên
        name_regex = QRegularExpression("[A-Za-z ]+")
        name_validator = QRegularExpressionValidator(name_regex, self)
        self.setValidator(name_validator)

    def setup_day_edit(self):
        self.setMaxLength(2)  # Giới hạn 2 ký tự
        # Thiết lập validator cho ngày
        day_validator = QIntValidator(1, 31, self)
        self.setValidator(day_validator)

    def setup_month_edit(self):
        self.setMaxLength(2)  # Giới hạn 2 ký tự
        # Thiết lập validator cho tháng
        month_validator = QIntValidator(1, 12, self)
        self.setValidator(month_validator)

    def setup_year_edit(self):
        self.setMaxLength(4)  # Giới hạn 4 ký tự
        # Thiết lập validator cho năm
        year_validator = QIntValidator(1900, 2100, self)
        self.setValidator(year_validator)

    def setup_time_edit(self):
        self.setMaxLength(2)  # Giới hạn 2 ký tự
        # Thiết lập validator cho giờ
        time_validator = QIntValidator(0, 23, self)
        self.setValidator(time_validator)
