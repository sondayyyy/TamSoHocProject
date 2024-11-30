import sys
from PySide6.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QPushButton, QDialog
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QFont
from PySide6.QtCore import QRegularExpression, QObject, Qt
from utils import get_tamsohoc_result, generate_main_number_table
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..TamSoHocMain import TamSoHocApp



class MainWindowUiCpn(QObject):
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


        self.main.ui.btn_main_header_menu.clicked.connect(self.hide_frm_left_indi)
        self.main.ui.btn_main_indi_menu.clicked.connect(self.show_main_menu)
        self.main.ui.btn_main_indi_intro.clicked.connect(self.show_main_intro)
        self.main.ui.btn_main_indi_libary.clicked.connect(self.show_main_lib)
        self.main.ui.btn_main_header_user.clicked.connect(self.show_main_account)
        self.main.ui.btn_main_indi_setting.clicked.connect(self.main.show_setting_popup)


        self.main.ui.btn_left_indi_sign_out.clicked.connect(self.main.show_logout_accept_ui)
        
        self.main.ui.btn_main_search_tracuu.clicked.connect(self.handle_search)


    # Kết nối nút với hàm



    def show_main_menu(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_menu)

    def show_main_intro(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_intro)

    def show_main_lib(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_lib)

    def show_main_account(self):
        self.main.ui.frm_main.setCurrentWidget(self.main.ui.frm_main_account)

    def hide_frm_left_indi(self):
        if self.main.ui.frm_left_indi.isVisible():
            self.main.ui.frm_left_indi.hide()
            print(82, "hide_indi")
        else:
            self.main.ui.frm_left_indi.show()
            print(85, "show_indi")
    

        
    def handle_search(self): #xử lý các lệnh khác như vẽ bảng, áp số vào trong này
        try:
            # Lấy giá trị từ giao diện
            name = self.main.ui.le_main_search_name.text()
            day = int(self.main.ui.le_main_search_day.text())
            month = int(self.main.ui.le_main_search_month.text())
            year = int(self.main.ui.le_main_search_year.text())
            hour = int(self.main.ui.le_main_search_time.text())
            

            # Kiểm tra dữ liệu hợp lệ
            if not name or day <= 0 or month <= 0 or year <= 0:
                raise ValueError("Thông tin không hợp lệ. Vui lòng nhập đủ và đúng các trường.")

            # Gọi hàm xử lý kết quả
            result = get_tamsohoc_result(name, day, month, year, hour)
            print("kết quả handle_search 110:", self.result)
            # for key, value in result.items():
            #     if key == "tong_bandau":
            #         print(key)


            # # Chuyển đổi kết quả thành dữ liệu lưới
            # grid_data = generate_main_number_table(self.result, str(day) + str(month) + str(year))
            # print("Dữ liệu hiển thị lưới:", grid_data)

            # # Tạo và hiển thị bảng
            # grid_widget = self.create_grid_board_widget(board_id=1, n=3, data=grid_data)
            # self.main.ui.glo_so_do.layout().addWidget(grid_widget)

        except Exception as e:
            print(f"Lỗi 115: {e}")

    def draw_grid_3x3(self, board_id, n=3):
        pass

    def draw_number(self):
        pass
    


