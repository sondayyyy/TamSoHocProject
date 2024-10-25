import sys
from PySide6.QtWidgets import QLineEdit, QWidget, QApplication, QMainWindow, QGraphicsOpacityEffect
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, QObject, Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp


class CustomMainWindow(QObject):
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

        # Tuỳ chỉnh title bar
        self.main.ui.frm_title.mousePressEvent = self.mousePressEvent
        self.main.ui.frm_title.mouseMoveEvent = self.mouseMoveEvent
        self.main.ui.frm_title.mouseReleaseEvent = self.mouseReleaseEvent


        
    def transformer(self):
        # Tạo hiệu ứng độ mờ
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0)  # Đặt độ mờ thành 0 (hoàn toàn trong suốt)
        
        # Áp dụng hiệu ứng cho widget trung tâm
        self.main.ui.centralwidget.setGraphicsEffect(self.opacity_effect)
    
    def show_widget(self):
    # Tạo hiệu ứng độ mờ
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(1)  # Đặt độ mờ thành 1 (hoàn toàn không trong suốt)

        # Áp dụng hiệu ứng cho widget trung tâm
        self.main.ui.centralwidget.setGraphicsEffect(self.opacity_effect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_drag_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        # Check if start_drag_pos is defined
        if self.start_drag_pos:
            delta = event.globalPos() - self.start_drag_pos
            self.main.move(self.main.pos() + delta)
            self.start_drag_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.start_drag_pos = None

