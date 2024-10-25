from PySide6.QtCore import  QObject, QThread, Signal, Qt, QEvent
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QWidget
from ui import Ui_LoginMainWindow 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class LoginWindowUiCpn(QDialog):
    def __init__(self, main):
        super(LoginWindowUiCpn, self).__init__(main)
        self.main: TamSoHocApp = main
        # self.login_main_window = Ui_LoginMainWindow()
        # self.login_main_window.setupUi(self)
        # self.start_drag_pos  = None
        self.main.ui_login_window.btn_minisize.clicked.connect(self.main.minimize_ui)
        self.main.ui_login_window.btn_fullscreen.clicked.connect(self.main.resize_ui)
        self.main.ui_login_window.btn_end.clicked.connect(self.main.end_ui)

        # self.login_main_window.frm_title.installEventFilter(self)





    # def is_login_failed(self):
    #     return False
    
    # def is_login_successful(self):
    #     # Thêm logic xác thực đăng nhập ở đây, ví dụ kiểm tra tên đăng nhập và mật khẩu
    #     return True  # Tạm thời giả sử luôn thành công

    # def eventFilter(self, obj, event):
    #     # Check if the event is coming from frm_title and is of type mouse
    #     if obj == self.login_main_window.frm_title:
    #         if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
    #             self.start_drag_pos_login = event.globalPos()
    #             return True
    #         elif event.type() == QEvent.MouseMove and self.start_drag_pos_login:
    #             delta = event.globalPos() - self.start_drag_pos_login
    #             self.move(self.pos() + delta)
    #             self.start_drag_pos_login = event.globalPos()
    #             return True
    #         elif event.type() == QEvent.MouseButtonRelease:
    #             self.start_drag_pos_login = None
    #             return True
    #     return super().eventFilter(obj, event)
