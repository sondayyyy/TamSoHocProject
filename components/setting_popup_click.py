from PySide6.QtCore import  QObject, QThread, Signal,Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget
from ui import Ui_setting_popup, Ui_MainWindow
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class SettingPopup(QDialog):
    def __init__(self, main):
        super(SettingPopup, self).__init__(main)
        self.main: TamSoHocApp = main
        # self.setWindowTitle("Popup Setting")
        self.setting_popup_ui = Ui_setting_popup()
        self.setting_popup_ui.setupUi(self)


        self.setting_popup_ui.btn_setting_popup_end.clicked.connect(self.end_setting_popup)
        self.setting_popup_ui.btn_setting_popup_fullscrean.clicked.connect(self.fullcrean_setting_popup)
        self.setting_popup_ui.btn_setting_popup_restart.clicked.connect(self.restart_setting_popup)

    def show_setting_popup(self):
        self.show()

    def end_setting_popup(self):
        self.close()

    def restart_setting_popup(self):
        print("Khôi phục cài đặt mặc định")

    def fullcrean_setting_popup(self):
        if self.main.isFullScreen():
            self.main.showNormal()
        else:
            self.main.showFullScreen()