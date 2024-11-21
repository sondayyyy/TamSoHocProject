
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QPixmap, QIcon, QPainter
from PySide6.QtCore import QSize, Qt, QObject
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

        #SVGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
        color_whiteblack = "images/color/color_whiteblack.svg"  # Đường dẫn tới file SVG
        color_green = "images/color/color_green.svg"  # Đường dẫn tới file SVG
        color_purple = "images/color/color_purple.svg"  # Đường dẫn tới file SVG
        color_blue = "images/color/color_blue.svg"  # Đường dẫn tới file SVG
        
        icon_size = QSize(20, 20)  # Kích thước icon
        self.main.ui_setting_popup.indi_color_black.setIcon(self.create_svg_icon(color_whiteblack, icon_size))
        self.main.ui_setting_popup.indi_color_black.setIconSize(icon_size)
        
        self.main.ui_setting_popup.indi_color_purple.setIcon(self.create_svg_icon(color_purple, icon_size))
        self.main.ui_setting_popup.indi_color_purple.setIconSize(icon_size)

        self.main.ui_setting_popup.indi_color_blue.setIcon(self.create_svg_icon(color_blue, icon_size))
        self.main.ui_setting_popup.indi_color_blue.setIconSize(icon_size)

        self.main.ui_setting_popup.indi_color_green.setIcon(self.create_svg_icon(color_green, icon_size))
        self.main.ui_setting_popup.indi_color_green.setIconSize(icon_size)



    def create_svg_icon(self, svg_file, size):
        # Tạo pixmap trống
        pixmap = QPixmap(size.width(), size.height())
        pixmap.fill(Qt.transparent)

        # Sử dụng QSvgRenderer để render SVG
        renderer = QSvgRenderer(svg_file)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        # Tạo QIcon từ pixmap
        return QIcon(pixmap)
        






