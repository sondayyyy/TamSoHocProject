import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QCheckBox, QGraphicsDropShadowEffect, QWidget
from PySide6.QtCore import Qt, QProcess
from PySide6.QtGui import QPixmap, QImage, QIcon, QColor

from ui import  Ui_MainWindow, Ui_setting_popup, Ui_LoginMainWindow, Ui_LogoutAccept
from components import SettingPopupCpn, LoginWindowUiCpn, MainWindowUiCpn
from themes import DarkTheme, LightTheme
from utils import ThemeManager
from view import MainWindowUiView, SettingPopupView
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import requests


class TamSoHocApp(QMainWindow):
    def __init__(self):
        super(TamSoHocApp, self).__init__()
        self.ui = Ui_MainWindow()  # Khởi tạo giao diện chính
        self.ui_login_window = Ui_LoginMainWindow() # Khởi tạo giao diện login
        self.ui_login_window.setupUi(self)  # Thiết lập giao diện login
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Ẩn khung mặc định
        self.setWindowTitle("Tâm Số Học")



        self.theme_manager = ThemeManager(LightTheme)

        self.login_window_cpn = LoginWindowUiCpn(self)


        self.ui_login_window.btn_login_enter.clicked.connect(self.login)
        self.ui_login_window.btn_login_google.clicked.connect(self.login_with_google)

        self.account_login_success = True

        self.start_drag_pos = None

        self.window_setting_popup = QDialog(self)  # Truyền self làm cha của dialog
        self.ui_setting_popup = Ui_setting_popup()  # Khởi tạo Ui_setting_popup
        self.ui_setting_popup.setupUi(self.window_setting_popup)  # Thiết lập giao diện cho dialog
        self.window_setting_popup.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        self.ui_setting_popup_cpn = SettingPopupCpn(self)
        self.ui_setting_popup_view = SettingPopupView(self) 
        self.window_setting_popup.hide()
        self.setting_popup_show_hide = False

        # self.ui_setting_popup.indi_color_purple.setStyleSheet(LightTheme.get_stylesheet())

        # self.logout_accept_ui.hide()
        # self.logout_accept_ui_show_hide = False

    def login(self):
        if self.account_login_success == True:
            self.ui.setupUi(self)  # Thiết lập giao diện
            self.setWindowTitle("Tâm Số Học")
            self.ui_cpn = MainWindowUiCpn(self)
            self.ui_view = MainWindowUiView(self)
            print("đăng nhập thành công")    

        else:
            self.ui_login_window.setupUi(self)


    def restart_app(self):

        QApplication.instance().quit()  # Thoát ứng dụng hiện tại
        status = QProcess.startDetached(sys.executable, sys.argv) 
    


    def on_login_fail(self):
        pass

    
    def show_setting_popup(self):
        if self.setting_popup_show_hide == False:
            self.window_setting_popup.show()
            self.setting_popup_show_hide = True
        else:
            self.window_setting_popup.hide()
            self.setting_popup_show_hide = False

    def show_logout_accept_ui(self):
        self.logout_accept_dialog = QDialog(self)
        self.logout_accept_ui = Ui_LogoutAccept()
        self.logout_accept_ui.setupUi(self.logout_accept_dialog)
        self.logout_accept_dialog.setWindowTitle("Đăng xuất")
        self.logout_accept_ui.btn_cancel.clicked.connect(self.logout_accept_dialog.close)
        self.logout_accept_ui.btn_continue.clicked.connect(self.restart_app)

        self.logout_accept_dialog.exec()

    def resize_ui(self):
        if self.isMaximized(): 
            self.showNormal()

        else:
            self.showMaximized() 

    def end_ui(self):
        self.close()

    def minimize_ui(self):
        self.showMinimized()

    def login_with_google(self):
        credentials_file = 'client_secret.json'

        # Xác định phạm vi API mà bạn cần
        scopes=[
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "openid"
        ]  # Thay đổi theo API bạn sử dụng

        # Khởi tạo luồng OAuth 2.0
        self.flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
        # Mở trình duyệt để xác thực và lấy access token
        self.credentials = self.flow.run_local_server(port=0)
        
        # In ra access token
        print("Access Token:", self.credentials.token)
        self.account_login_success = True
        self.check_user_info(self.credentials.token)
        self.login()
        self.user_login_with_google()

    def check_user_info(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers=headers)
        
        if response.status_code == 200:
            self.user_info = response.json()
        else:
            print("Failed to retrieve user info:", response.text)

    def user_login_with_google(self):
        # Gán thông tin vào các label trong giao diện
        self.ui.btn_left_indi_user.setText(self.user_info.get('name', 'Unknown'))
        self.ui.left_indi_user_id.setText(self.user_info.get('id', 'N/A'))
        profile_pic_url = self.user_info.get('picture', '')

        # Hiển thị hình ảnh người dùng vào label nếu có ảnh
        if profile_pic_url:
            image_data = requests.get(profile_pic_url).content
            image = QImage()
            image.loadFromData(image_data)
            icon = QIcon(QPixmap.fromImage(image))  # Create an icon from the image
            self.ui.left_indi_user_image.setIcon(icon)

    def apply_shadow_effect(self, widget: QWidget, offset=(5, 5), blur_radius=15, color=QColor(0, 0, 0, 160)):
        shadow_effect = QGraphicsDropShadowEffect(widget)
        shadow_effect.setOffset(*offset)  # Thiết lập vị trí bóng đổ
        shadow_effect.setBlurRadius(blur_radius)  # Thiết lập độ mờ
        shadow_effect.setColor(color)  # Thiết lập màu sắc của bóng đổ
        widget.setGraphicsEffect(shadow_effect)        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TamSoHocApp()
    window.show()  # Hiển thị cửa sổ
    sys.exit(app.exec())  # Bắt đầu vòng lặp sự kiện