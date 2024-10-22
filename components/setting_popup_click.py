from PySide6.QtCore import  QObject, QThread, Signal
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget
import threading
from threading import Thread
from ui import Ui_setting_popup
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui import Ui_MainWindow


class SettingPopup(QDialog):
    def __init__(self, parent=None):
        super(SettingPopup, self).__init__(parent)
        self.setWindowTitle("Popup Setting")
        self.setting_popup_ui = Ui_setting_popup()
        self.setting_popup_ui.setupUi(self)
        # layout = QVBoxLayout(self)
        # layout.addWidget(self.setting_popup_ui)
        # self.setLayout(layout)


        self.setting_popup_ui.btn_setting_popup_end.clicked.connect(self.end_setting_popup)
        self.setting_popup_ui.btn_setting_popup_fullscrean.clicked.connect(self.fullcrean_setting_popup)
        self.setting_popup_ui.btn_setting_popup_restart.clicked.connect(self.restart_setting_popup)

    def show_setting_popup(self):
        self.reTranslate()
        threading.Thread(target=self.execute).start()

    def end_setting_popup(self):
        self.setting_popup_ui.close()

    def restart_setting_popup(self):
        print("Khôi phục cài đặt mặc định")

    def fullcrean_setting_popup(self):
        if self.setting_popup_ui.isFullScreen():
            self.setting_popup_ui.showNormal()  # Hiển thị bình thường
        else:
            self.setting_popup_ui.showFullScreen()