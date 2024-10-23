import sys
from PySide6.QtWidgets import QLineEdit, QWidget, QApplication, QMainWindow
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QObject
from main_ui import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Tâm Số Học Project")

        # Tạo một đối tượng Ui_MainWindow và gọi setupUi
        self.ui_custom_window = Ui_MainWindow()
        self.ui_custom_window.setupUi(self)


            # self.ui_custom_window.setupUi(self)

        #Tuỳ chỉnh tên nhập vào (giới hạn 40 chữ)
        name_regex = QRegularExpression("[A-Za-zÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơ"
            "Ạ-ỹ ]+")
        name_validator = QRegularExpressionValidator(name_regex)
        self.ui_custom_window.le_main_search_name.setValidator(name_validator)
        self.ui_custom_window.le_main_search_name.setMaxLength(40)

        #Tuỳ chỉnh ngày
        # Tùy chỉnh cho ngày (01 - 31)
        day_validator = QIntValidator(1, 31)
        self.ui_custom_window.le_main_search_day.setValidator(day_validator)
        self.ui_custom_window.le_main_search_day.setMaxLength(2)


        # Tùy chỉnh cho tháng (01 - 12)
        month_validator = QIntValidator(1, 12)
        self.ui_custom_window.le_main_search_month.setValidator(month_validator)
        self.ui_custom_window.le_main_search_month.setMaxLength(2)


        # Tùy chỉnh cho năm (nhập năm có 4 chữ số, ví dụ 1900-2999)
        year_validator = QIntValidator(1900, 2999)
        self.ui_custom_window.le_main_search_year.setValidator(year_validator)
        self.ui_custom_window.le_main_search_year.setMaxLength(4)


        # Tùy chỉnh cho giờ (nhập giờ có 2 chữ số, ví dụ 0-23)
        time_validator = QIntValidator(0, 23)
        self.ui_custom_window.le_main_search_time.setValidator(time_validator)
        self.ui_custom_window.le_main_search_time.setMaxLength(2)  



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()  # Hiển thị cửa sổ
#     sys.exit(app.exec())


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
