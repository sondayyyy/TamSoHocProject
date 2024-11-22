import sys
from PySide6.QtWidgets import QLineEdit, QWidget, QApplication, QMainWindow, QGraphicsOpacityEffect
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QPixmap, QImage, QIcon
from PySide6.QtCore import QRegularExpression, QObject, Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp

import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import credentials
from google.auth.transport.requests import Request


class MainWindowUiCpn(QObject):
    def __init__(self, main):
        super().__init__()
        self.main : TamSoHocApp = main
        month_validator = QIntValidator(1, 12)
        self.main.ui.le_main_search_month.setValidator(month_validator)
        self.start_drag_pos  = None
            # self.ui_custom_window.setupUi(self)

        #Tuỳ chỉnh tên nhập vào (giới hạn 40 chữ)
        name_regex = QRegularExpression("[A-Za-zÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơ"
            "Ạ-ỹ ]+")
        name_validator = QRegularExpressionValidator(name_regex)
        self.main.ui.le_main_search_name.setValidator(name_validator)
        self.main.ui.le_main_search_name.setMaxLength(40)

        #Tuỳ chỉnh ngày
        # Tùy chỉnh cho ngày (01 - 31)
        day_validator = QIntValidator(1, 31)
        self.main.ui.le_main_search_day.setValidator(day_validator)
        self.main.ui.le_main_search_day.setMaxLength(2)


        # Tùy chỉnh cho tháng (01 - 12)
        month_validator = QIntValidator(1, 12)
        self.main.ui.le_main_search_month.setValidator(month_validator)
        self.main.ui.le_main_search_month.setMaxLength(2)



        # Tùy chỉnh cho năm (nhập năm có 4 chữ số, ví dụ 1900-2999)
        year_validator = QIntValidator(1900, 2999)
        self.main.ui.le_main_search_year.setValidator(year_validator)
        self.main.ui.le_main_search_year.setMaxLength(4)



        # Tùy chỉnh cho giờ (nhập giờ có 2 chữ số, ví dụ 0-23)
        time_validator = QIntValidator(0, 23)
        self.main.ui.le_main_search_time.setValidator(time_validator)
        self.main.ui.le_main_search_time.setMaxLength(2)  


        self.main.ui.btn_main_header_menu.clicked.connect(self.hide_frm_left_indi)
        self.main.ui.btn_main_indi_menu.clicked.connect(self.show_main_menu)
        self.main.ui.btn_main_indi_intro.clicked.connect(self.show_main_intro)
        self.main.ui.btn_main_indi_libary.clicked.connect(self.show_main_lib)
        self.main.ui.btn_main_header_user.clicked.connect(self.show_main_account)
        self.main.ui.btn_main_indi_setting.clicked.connect(self.main.show_setting_popup)


        self.main.ui.btn_left_indi_sign_out.clicked.connect(self.main.show_logout_accept_ui)

        



    def show_main_menu(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_menu)

    def show_main_intro(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_intro)

    def show_main_lib(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_lib)

    def show_main_account(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_account)

    def hide_frm_left_indi(self):
        if self.main.ui.frm_left_indi.isVisible():
            self.main.ui.frm_left_indi.hide()
            print(82, "hide_indi")
        else:
            self.main.ui.frm_left_indi.show()
            print(85, "show_indi")
    




