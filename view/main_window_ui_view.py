from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QRectF, QObject, Qt
from themes import LightTheme
from scr import SwitchButton, ContainedButton, OutlinedButton, TextButton, SoftButton, CustomWidget, CustomFrame, CustomLineEdit, SearchLineEdit
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class MainWindowUiView(QObject):
    def __init__(self, main):
        super(MainWindowUiView, self).__init__(main)
        self.main : TamSoHocApp = main
        
        self.main.ui.frm_center.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0,
                    stop:0 {LightTheme.Third.grey()},
                    stop:1 #EAFBFF
                );
            }}
        """)
        self.main.ui.frm_center.setFrameShape(QFrame.Shape.NoFrame)
        self.main.ui.lb_logo.setStyleSheet("background-color: none;")

        self.main.ui.frm_ma.setStyleSheet(LightTheme.stylesheet_lighter())


        self.main.ui.btn_main_indi_menu.setStyleSheet(
                SoftButton.get_stylesheet(padding= "10",
                                          
                                        hover_color = LightTheme.Third.main_hover(),
                                        pressed_color = LightTheme.Third.main_press()))

        self.main.ui.btn_main_indi_intro.setStyleSheet(
                SoftButton.get_stylesheet(hover_color = LightTheme.Third.main_hover(),
                                        pressed_color = LightTheme.Third.main_press()))
        
        self.main.ui.btn_main_indi_libary.setStyleSheet(
                SoftButton.get_stylesheet(padding= "10",
                                          hover_color = LightTheme.Third.main_hover(),
                                        pressed_color = LightTheme.Third.main_press()))
        
        self.main.ui.btn_main_indi_setting.setStyleSheet(
                SoftButton.get_stylesheet(padding= "10",
                                          hover_color = LightTheme.Third.main_hover(),
                                        pressed_color = LightTheme.Third.main_press()))
        
        self.main.ui.btn_left_indi_sign_out.setStyleSheet(
                SoftButton.get_stylesheet(padding= "10",
                                        bg_color= LightTheme.Four.grey(),
                                        hover_color = LightTheme.Third.main_hover(),
                                        pressed_color = LightTheme.Third.main_press()))
        
        self.main.ui.btn_main_search_tracuu.setStyleSheet(
                SoftButton.get_stylesheet(padding= "7",
                                        bg_color= LightTheme.Secondary.main(),
                                        hover_color = LightTheme.Primary.main_hover(),
                                        pressed_color = LightTheme.Primary.main_press(),
                                        text_color = LightTheme.Text.white()))
        
        
        self.main.ui.btn_main_header_menu.setStyleSheet(OutlinedButton.get_stylesheet(border_color= LightTheme.Secondary.main()))
        self.main.ui.btn_main_header_user.setStyleSheet(OutlinedButton.get_stylesheet())
        self.main.ui.frm_main_header_search_bar.setStyleSheet(
                                                        CustomWidget.get_stylesheet(
                                                                border_color=LightTheme.Secondary.grey(),
                                                                bg_color= LightTheme.Third.grey()))
        self.main.ui.le_main_header_search_bar.setPlaceholderText("Tìm kiếm ngay")
        self.main.ui.btn_main_header_search_bar.setStyleSheet(
                                                        SoftButton.get_stylesheet(
                                                                padding="1",
                                                                 bg_color=LightTheme.Third.grey()))
        


        self.main.ui.le_main_search_name.setStyleSheet(CustomLineEdit.get_stylesheet())
        self.main.ui.le_main_search_time.setStyleSheet(CustomLineEdit.get_stylesheet())
        self.main.ui.le_main_search_year.setStyleSheet(CustomLineEdit.get_stylesheet())
        self.main.ui.le_main_search_month.setStyleSheet(CustomLineEdit.get_stylesheet())
        self.main.ui.le_main_search_day.setStyleSheet(CustomLineEdit.get_stylesheet())

        self.main.ui.le_main_search_name.setPlaceholderText("Nhập họ và tên")
        self.main.ui.le_main_search_time.setPlaceholderText("0-23")
        self.main.ui.le_main_search_year.setPlaceholderText("YYYY")
        self.main.ui.le_main_search_month.setPlaceholderText("MM")
        self.main.ui.le_main_search_day.setPlaceholderText("DD")
