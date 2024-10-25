import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt, QEvent
import threading
from threading import Thread
from ui import  Ui_MainWindow, Ui_setting_popup, Ui_LoginMainWindow
from components import SettingPopup, LoginPopupWindow
from view import CustomMainWindow



class TamSoHocApp(QMainWindow):
    def __init__(self):
        super(TamSoHocApp, self).__init__()
        self.ui = Ui_MainWindow()  # Khởi tạo giao diện 
        self.ui.setupUi(self)  # Thiết lập giao diện
        self.custom_ui = CustomMainWindow(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.custom_ui.transformer() 

        self.start_drag_pos = None

        
        self.ui_login_popup = LoginPopupWindow(self)
        self.ui_login_popup.setWindowFlags(Qt.FramelessWindowHint)
        self.ui_login_popup.show()


        self.ui_setting_popup = SettingPopup(self)
        self.ui_setting_popup.hide()
        self.ui_setting_popup_show_hide = False


        self.ui.btn_minimize_obj.clicked.connect(self.minimize_ui)
        self.ui.btn_resize_obj.clicked.connect(self.resize_ui)
        self.ui.btn_end_obj.clicked.connect(self.end_ui)


        self.ui.btn_main_header_menu.clicked.connect(self.hide_frm_left_indi)
        self.ui.btn_main_indi_menu.clicked.connect(self.show_main_menu)
        self.ui.btn_main_indi_intro.clicked.connect(self.show_main_intro)
        self.ui.btn_main_indi_libary.clicked.connect(self.show_main_lib)
        self.ui.btn_main_header_user.clicked.connect(self.show_main_account)
        self.ui.btn_main_indi_setting.clicked.connect(self.show_setting_popup)
        
        self.ui.btn_left_indi_sign_out.clicked.connect(self.back_to_login)

    def on_login_success(self):
        # Sau khi đăng nhập thành công, ẩn cửa sổ popup đăng nhập và hiển thị giao diện chính
        self.ui_login_popup.close()  # Đóng cửa sổ đăng nhập
        self.custom_ui.show_widget()

    def on_login_fail(self):
        # Sau khi đăng nhập thành công, ẩn cửa sổ popup đăng nhập và hiển thị giao diện chính
        pass



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

    def back_to_login(self):
        self.ui_login_popup.open()  # Mở cửa sổ đăng nhập
        self.custom_ui.transformer()

    def hide_frm_left_indi(self):
        if self.ui.frm_left_indi.isVisible():
            self.ui.frm_left_indi.hide()
            print(82, "hide_indi")
        else:
            self.ui.frm_left_indi.show()
            print(85, "show_indi")

    def resize_ui(self):
        if self.isMaximized(): 
            self.showNormal()
        else:
            self.showMaximized() 

    def end_ui(self):
        self.close()

    def minimize_ui(self):
        self.showMinimized()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TamSoHocApp()
    window.show()  # Hiển thị cửa sổ
    sys.exit(app.exec())  # Bắt đầu vòng lặp sự kiện
