from PySide6.QtCore import  QObject, QThread, Signal,Qt, QEvent
from PySide6.QtGui import  QColor
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from ui import Ui_setting_popup, Ui_MainWindow
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class SettingPopupCpn(QObject):
    def __init__(self, main):
        super().__init__()
        self.main: TamSoHocApp = main


        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setBlurRadius(15)  # Độ mờ
        self.shadow_effect.setXOffset(0)       # Offset theo trục X
        self.shadow_effect.setYOffset(0)       # Offset theo trục Y
        self.shadow_effect.setColor(QColor(0, 0, 0, 150))  # Màu sắc bóng


        self.start_drag_pos_login = None

        self.main.ui_setting_popup.btn_setting_popup_end.clicked.connect(self.end_setting_popup)
        self.main.ui_setting_popup.btn_setting_popup_restart.clicked.connect(self.restart_setting_popup)


    def end_setting_popup(self):
        self.main.window_setting_popup.close()
        self.main.setting_popup_show_hide = False

    def restart_setting_popup(self):
        print("Khôi phục cài đặt mặc định")

    
    