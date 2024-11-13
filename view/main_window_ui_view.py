import sys
from PySide6.QtWidgets import QLineEdit, QWidget, QApplication, QMainWindow, QGraphicsOpacityEffect
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QPixmap, QIcon, QImage
from PySide6.QtCore import QRegularExpression, QObject, Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp
import requests

class MainWindowUiView(QObject):
    def __init__(self, main):
        super().__init__()
        self.main : TamSoHocApp = main
        

        # self.main.ui.btn_left_indi_user = 
        # self.main.theme_manager.apply_theme()