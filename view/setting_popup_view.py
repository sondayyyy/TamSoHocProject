from PySide6.QtCore import  QObject, QThread, Signal,Qt, QEvent,  QSize
from PySide6.QtGui import  QColor, QIcon
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from scr import SwitchButton
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class SettingPopupView(QObject):
    def __init__(self, main):
        super(SettingPopupView, self).__init__(main)
        self.main: TamSoHocApp = main

        self.indi_contrast_cb = SwitchButton("small")
        self.indi_mode_cb = SwitchButton("small")

        self.main.ui_setting_popup.frm_btn_mode.layout().addWidget(self.indi_mode_cb)
        self.main.ui_setting_popup.frm_btn_contrast.layout().addWidget(self.indi_contrast_cb)

        # Kết nối hàm apply_shadow_effect
        self.main.apply_shadow_effect(self.main.window_setting_popup)

        icon_color_blue =  QIcon("D:\TamSoHocProject\scr\icons\color_blue.svg")
        icon_color_purple =  QIcon("D:\TamSoHocProject\scr\icons/color_purple.svg")
        icon_color_whiteblack =  QIcon("D:/TamSoHocProject/scr/icons/color_whiteblack.svg")
        icon_color_green =  QIcon("D:/TamSoHocProject/scr/icons/color_green.svg")

        self.main.ui_setting_popup.indi_color_purple.setIcon(icon_color_purple)




