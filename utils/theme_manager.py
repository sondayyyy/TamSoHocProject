# theme_manager.py
from themes.light import LightTheme
from themes.dark import DarkTheme
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp


class ThemeManager():
    def __init__(self, main):
        super().__init__()
        self.main : TamSoHocApp = main
        
        self.current_theme = LightTheme # Giao diện mặc định là Light

    def switch_to_light_theme(self):
        self.current_theme = LightTheme
        self.apply_theme()

    def switch_to_dark_theme(self):
        self.current_theme = DarkTheme
        self.apply_theme()

    def apply_theme(self):
        # Áp dụng stylesheet từ theme hiện tại lên ứng dụng
        app = QApplication.instance()
        app.setStyleSheet(self.current_theme.get_stylesheet())
    
