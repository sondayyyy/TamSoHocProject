from PySide6.QtCore import  QObject, QThread, Signal, Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit
# from PyQt6.QtGui import QDoubleValidator, QIntValidator
import threading
from threading import Thread
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui import Ui_MainWindow

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(CustomLineEdit, self).__init__(parent)
        self.qline_edit = Ui_MainWindow.setupUi(self.le_main_search_time)
        

    def qline_edit_name(self):
        self.qline_edit.le_main_search_name.setMaxLength(50)

    def qline_edit_day(self):
        self.qline_edit.le_main_search_day.setMaxLength(2)

    def qline_edit_month(self):
        # month_regex = QIntValidator(1, 12)  # 1 to 12
        self.qline_edit.le_main_search_month.setMaxLength(2)

    def qline_edit_year(self):
        self.qline_edit.le_main_search_year.setMaxLength(4)

    def qline_edit_time(self):
        # Hour QLineEdit - Allow numbers between 0 and 23
        self.qline_edit.le_main_search_time.setPlaceholderText(0, 23)
