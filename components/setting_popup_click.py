from PySide6.QtCore import  QObject, QThread, Signal,Qt, QEvent
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget
from ui import Ui_setting_popup, Ui_MainWindow
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class SettingPopup(QDialog):
    def __init__(self, main):
        super(SettingPopup, self).__init__(main)
        self.main: TamSoHocApp = main
        self.setting_popup_ui = Ui_setting_popup()
        self.setting_popup_ui.setupUi(self)

        self.start_drag_pos_login = None

        self.setting_popup_ui.btn_setting_popup_end.clicked.connect(self.end_setting_popup)
        self.setting_popup_ui.btn_setting_popup_fullscrean.clicked.connect(self.fullcrean_setting_popup)
        self.setting_popup_ui.btn_setting_popup_restart.clicked.connect(self.restart_setting_popup)

        self.setting_popup_ui.frm_setting_popup.installEventFilter(self)

    def show_setting_popup(self):
        self.show()

    def end_setting_popup(self):
        self.close()
        self.main.ui_setting_popup_show_hide = False

    def restart_setting_popup(self):
        print("Khôi phục cài đặt mặc định")

    def fullcrean_setting_popup(self):
        if self.main.isFullScreen():
            self.main.showNormal()
        else:
            self.main.showFullScreen()

    def eventFilter(self, obj, event):
        # Kiểm tra nếu sự kiện đến từ frm_setting_popup và là sự kiện chuột
        if obj == self.setting_popup_ui.frm_setting_popup:
            if event.type() == QEvent.Type.MouseButtonPress and event.button() == Qt.MouseButton.LeftButton:
                self.start_drag_pos_login = event.globalPos()
                return True
            elif event.type() == QEvent.Type.MouseMove and self.start_drag_pos_login:
                delta = event.globalPos() - self.start_drag_pos_login
                self.move(self.pos() + delta)
                self.start_drag_pos_login = event.globalPos()
                return True
            elif event.type() == QEvent.Type.MouseButtonRelease:
                self.start_drag_pos_login = None
                return True
        return super().eventFilter(obj, event)