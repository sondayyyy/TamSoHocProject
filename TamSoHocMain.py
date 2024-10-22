import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import threading
from threading import Thread
from components import CustomLineEdit
from ui import Ui_MainWindow, Ui_setting_popup
from components import SettingPopup, CustomLineEdit



class TamSoHocApp(QMainWindow):
    def __init__(self):
        super(TamSoHocApp, self).__init__()
        self.ui = Ui_MainWindow()  # Khởi tạo giao diện
        self.ui.setupUi(self)  # Thiết lập giao diện
        self.ui_setting_popup = SettingPopup(self)
        self.ui_setting_popup.hide()
        self.ui_setting_popup_show_hide = False

        # self.edit_line = CustomLineEdit()

        self.ui.btn_main_header_menu.clicked.connect(self.hide_frm_left_indi)
        self.ui.btn_main_indi_menu.clicked.connect(self.show_main_menu)
        self.ui.btn_main_indi_intro.clicked.connect(self.show_main_intro)
        self.ui.btn_main_indi_libary.clicked.connect(self.show_main_lib)
        self.ui.btn_main_header_user.clicked.connect(self.show_main_account)
        self.ui.btn_main_indi_setting.clicked.connect(self.show_setting_popup)

        

    def show_main_menu(self):
        self.ui.frm_main.setCurrentWidget(self.ui.frm_main_menu)

    def show_main_intro(self):
        self.ui.frm_main.setCurrentWidget(self.ui.frm_main_intro)

    def show_main_lib(self):
        self.ui.frm_main.setCurrentWidget(self.ui.frm_main_lib)

    def show_main_account(self):
        self.ui.frm_main.setCurrentWidget(self.ui.frm_main_account)
    
    def show_setting_popup(self):
        if self.ui_setting_popup_show_hide == False:
            self.ui_setting_popup.show()
            self.ui_setting_popup_show_hide = True
        else:
            self.ui_setting_popup.hide()
            self.ui_setting_popup_show_hide = False


    # def set_up_custom_qline_edit(self):
    #     # self.ui.le_main_search_name = self.edit_line.qline_edit_name
    #     # self.ui.le_main_search_day = self.edit_line.qline_edit_day
    #     # self.ui.le_main_search_month = self.edit_line.qline_edit_month
    #     # self.ui.le_main_search_year = self.edit_line.qline_edit_year
    #     # self.ui.le_main_search_time = self.edit_line.qline_edit_time
    
    #     # Khởi tạo CustomLineEdit cho mỗi QLineEdit và áp dụng kiểm tra hợp lệ
    #     self.edit_line_name = CustomLineEdit(self.ui.le_main_search_name)
    #     self.edit_line_name.qline_edit_name()

    #     self.edit_line_day = CustomLineEdit(self.ui.le_main_search_day)
    #     self.edit_line_day.qline_edit_day()

    #     self.edit_line_month = CustomLineEdit(self.ui.le_main_search_month)
    #     self.edit_line_month.qline_edit_month()

    #     self.edit_line_year = CustomLineEdit(self.ui.le_main_search_year)
    #     self.edit_line_year.qline_edit_year()

    #     self.edit_line_time = CustomLineEdit(self.ui.le_main_search_time)
    #     self.edit_line_time.qline_edit_hour()


    def hide_frm_left_indi(self):
        print(13, "hide_indi")
        if self.ui.frm_left_indi.isVisible():
            self.ui.frm_left_indi.hide()
        else:
            self.ui.frm_left_indi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TamSoHocApp()
    window.show()  # Hiển thị cửa sổ
    sys.exit(app.exec())  # Bắt đầu vòng lặp sự kiện
    