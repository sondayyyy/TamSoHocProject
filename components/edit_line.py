from PySide6.QtWidgets import QLineEdit, QWidget
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression
from ui import Ui_MainWindow

class CustomLineEdit(QWidget):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        self.ui_customline = Ui_MainWindow()
        self.ui_customline.setupUi(self)
        self.ui_customline.le_main_search_name.setMaxLength(40)
        self.ui_customline.le_main_search_day.setMaxLength(2)
        self.ui_customline.le_main_search_month.setMaxLength(2)
        self.ui_customline.le_main_search_year.setMaxLength(4)
        self.ui_customline.le_main_search_time.setMaxLength(2)  


    # def setup_name_edit(self):
    #     self.setMaxLength(50)  # Giới hạn số ký tự
    #     # Thiết lập validator cho tên
    #     name_regex = QRegularExpression("[A-Za-z ]+")
    #     name_validator = QRegularExpressionValidator(name_regex, self)
    #     self.setValidator(name_validator)

    # def setup_day_edit(self):
    #     self.setMaxLength(2)  # Giới hạn 2 ký tự
    #     # Thiết lập validator cho ngày
    #     day_validator = QIntValidator(1, 31, self)
    #     self.setValidator(day_validator)

    # def setup_month_edit(self):
    #     self.setMaxLength(2)  # Giới hạn 2 ký tự
    #     # Thiết lập validator cho tháng
    #     month_validator = QIntValidator(1, 12, self)
    #     self.setValidator(month_validator)

    # def setup_year_edit(self):
    #     self.setMaxLength(4)  # Giới hạn 4 ký tự
    #     # Thiết lập validator cho năm
    #     year_validator = QIntValidator(1900, 2100, self)
    #     self.setValidator(year_validator)

    # def setup_time_edit(self):
    #     self.setMaxLength(2)  # Giới hạn 2 ký tự
    #     # Thiết lập validator cho giờ
    #     time_validator = QIntValidator(0, 23, self)
    #     self.setValidator(time_validator)
