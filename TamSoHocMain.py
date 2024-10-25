import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt, QEvent
import threading
from threading import Thread
from ui import  Ui_MainWindow, Ui_setting_popup, Ui_LoginMainWindow
from components import SettingPopup, LoginWindowUiCpn, MainWindowUiCpn



class TamSoHocApp(QMainWindow):
    def __init__(self):
        super(TamSoHocApp, self).__init__()
        self.ui = Ui_MainWindow()  # Khởi tạo giao diện 
        self.ui_login_window = Ui_LoginMainWindow()
        self.ui_login_window.setupUi(self)  # Thiết lập giao diện
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.login_window_cpn = LoginWindowUiCpn(self)

        self.ui_login_window.btn_login_enter.clicked.connect(self.login)

        self.account_login_success = True

        self.start_drag_pos = None


        self.ui_setting_popup = SettingPopup(self)
        self.ui_setting_popup.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.ui_setting_popup.hide()
        self.ui_setting_popup_show_hide = False


    def login(self):
        if self.account_login_success == True:
            self.ui.setupUi(self)  # Thiết lập giao diện
            self.main_window_cpn = MainWindowUiCpn(self)
            print("đăng nhập thành công")    

        else:
            self.ui_login_window.setupUi(self)


    def back_to_login(self):
        self.account_login_success = False
        self.ui_login_window.setupUi(self)  # Thiết lập giao diện

    def on_login_fail(self):
        pass

    
    def show_setting_popup(self):
        if self.ui_setting_popup_show_hide == False:
            self.ui_setting_popup.show()
            self.ui_setting_popup_show_hide = True
        else:
            self.ui_setting_popup.hide()
            self.ui_setting_popup_show_hide = False



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
