from PySide6.QtCore import  QObject, QThread, Signal, Qt, QEvent
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget
from ui import Ui_LoginMainWindow 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class LoginWindowUiCpn(QDialog):
    def __init__(self, main):
        super(LoginWindowUiCpn, self).__init__(main)
        self.main: TamSoHocApp = main


        self.main.ui_login_window.btn_minisize.clicked.connect(self.main.minimize_ui)
        self.main.ui_login_window.btn_end.clicked.connect(self.main.end_ui)

        self.main.ui_login_window.btn_login_reges.clicked.connect(self.show_register)
        self.main.ui_login_window.btn_login_forget.clicked.connect(self.show_forget_password)
        self.main.ui_login_window.btn_regis_back.clicked.connect(self.show_login_menu)
        self.main.ui_login_window.btn_forget_back.clicked.connect(self.show_login_menu)



    def show_register(self):
        self.main.ui_login_window.frm_main.setCurrentWidget(self.main.ui_login_window.frm_regis)

    def show_forget_password(self):
        self.main.ui_login_window.frm_main.setCurrentWidget(self.main.ui_login_window.frm_forget)

    def show_login_menu(self):
        self.main.ui_login_window.frm_main.setCurrentWidget(self.main.ui_login_window.frm_login)

