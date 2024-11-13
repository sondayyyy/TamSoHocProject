# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menutGufFW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 672)
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon_svg/calendar-zoom.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_center = QFrame(self.centralwidget)
        self.frm_center.setObjectName(u"frm_center")
        self.frm_center.setStyleSheet(u"background: #999")
        self.frm_center.setFrameShape(QFrame.StyledPanel)
        self.frm_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_center)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frm_title = QWidget(self.frm_center)
        self.frm_title.setObjectName(u"frm_title")
        self.frm_title.setMinimumSize(QSize(0, 40))
        self.frm_title.setMaximumSize(QSize(16777215, 40))
        self.frm_title.setMouseTracking(True)
        self.frm_title.setTabletTracking(True)
        self.frm_title.setFocusPolicy(Qt.StrongFocus)
        self.frm_title.setLayoutDirection(Qt.LeftToRight)
        self.frm_title.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.frm_title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.frame_5 = QFrame(self.frm_title)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(150, 40))
        self.frame_5.setMaximumSize(QSize(150, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize_obj = QPushButton(self.frame_5)
        self.btn_minimize_obj.setObjectName(u"btn_minimize_obj")
        self.btn_minimize_obj.setMinimumSize(QSize(50, 40))
        self.btn_minimize_obj.setMaximumSize(QSize(50, 40))

        self.horizontalLayout_9.addWidget(self.btn_minimize_obj)

        self.btn_resize_obj = QPushButton(self.frame_5)
        self.btn_resize_obj.setObjectName(u"btn_resize_obj")
        self.btn_resize_obj.setMinimumSize(QSize(50, 40))
        self.btn_resize_obj.setMaximumSize(QSize(60, 40))

        self.horizontalLayout_9.addWidget(self.btn_resize_obj)

        self.btn_end_obj = QPushButton(self.frame_5)
        self.btn_end_obj.setObjectName(u"btn_end_obj")
        self.btn_end_obj.setMinimumSize(QSize(50, 40))
        self.btn_end_obj.setMaximumSize(QSize(40, 50))

        self.horizontalLayout_9.addWidget(self.btn_end_obj)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frm_title)

        self.frm_main_ = QWidget(self.frm_center)
        self.frm_main_.setObjectName(u"frm_main_")
        self.horizontalLayout_8 = QHBoxLayout(self.frm_main_)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frm_left_indi = QWidget(self.frm_main_)
        self.frm_left_indi.setObjectName(u"frm_left_indi")
        self.frm_left_indi.setMinimumSize(QSize(170, 0))
        self.frm_left_indi.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.frm_left_indi)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.left_indi_user = QWidget(self.frm_left_indi)
        self.left_indi_user.setObjectName(u"left_indi_user")
        self.horizontalLayout_7 = QHBoxLayout(self.left_indi_user)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 0, 3, 0)
        self.widget = QWidget(self.left_indi_user)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_10 = QHBoxLayout(self.widget)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.left_indi_user_image = QPushButton(self.widget)
        self.left_indi_user_image.setObjectName(u"left_indi_user_image")
        self.left_indi_user_image.setMinimumSize(QSize(40, 40))
        self.left_indi_user_image.setMaximumSize(QSize(40, 40))
        self.left_indi_user_image.setStyleSheet(u"QWidget {\n"
"    border: 2px solid purple; /* \u0110\u1ed9 d\u00e0y vi\u1ec1n l\u00e0 2px, m\u00e0u \u0111en */\n"
"    border-radius: 15px;      /* G\u00f3c vi\u1ec1n bo tr\u00f2n (t\u00f9y ch\u1ecdn) */\n"
"}\n"
"\n"
"")
        self.left_indi_user_image.setIconSize(QSize(35, 35))

        self.horizontalLayout_10.addWidget(self.left_indi_user_image)


        self.horizontalLayout_7.addWidget(self.widget)

        self.frm_left_indi_user = QWidget(self.left_indi_user)
        self.frm_left_indi_user.setObjectName(u"frm_left_indi_user")
        self.verticalLayout_3 = QVBoxLayout(self.frm_left_indi_user)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.btn_left_indi_user = QPushButton(self.frm_left_indi_user)
        self.btn_left_indi_user.setObjectName(u"btn_left_indi_user")

        self.verticalLayout_3.addWidget(self.btn_left_indi_user, 0, Qt.AlignLeft)

        self.left_indi_user_id = QLabel(self.frm_left_indi_user)
        self.left_indi_user_id.setObjectName(u"left_indi_user_id")

        self.verticalLayout_3.addWidget(self.left_indi_user_id)


        self.horizontalLayout_7.addWidget(self.frm_left_indi_user)


        self.verticalLayout_7.addWidget(self.left_indi_user)

        self.btn_main_indi_menu = QPushButton(self.frm_left_indi)
        self.btn_main_indi_menu.setObjectName(u"btn_main_indi_menu")
        self.btn_main_indi_menu.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Purple/icon_svg/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/White/icon_svg/white/home.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_menu.setIcon(icon1)
        self.btn_main_indi_menu.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_main_indi_menu, 0, Qt.AlignLeft)

        self.btn_main_indi_intro = QPushButton(self.frm_left_indi)
        self.btn_main_indi_intro.setObjectName(u"btn_main_indi_intro")
        self.btn_main_indi_intro.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Purple/icon_svg/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/White/icon_svg/white/book (1).svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_intro.setIcon(icon2)
        self.btn_main_indi_intro.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_main_indi_intro, 0, Qt.AlignLeft)

        self.btn_main_indi_libary = QPushButton(self.frm_left_indi)
        self.btn_main_indi_libary.setObjectName(u"btn_main_indi_libary")
        icon3 = QIcon()
        icon3.addFile(u":/Purple/icon_svg/bookbok (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/White/icon_svg/white/book.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_libary.setIcon(icon3)
        self.btn_main_indi_libary.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_main_indi_libary, 0, Qt.AlignLeft)

        self.btn_main_indi_setting = QPushButton(self.frm_left_indi)
        self.btn_main_indi_setting.setObjectName(u"btn_main_indi_setting")
        icon4 = QIcon()
        icon4.addFile(u":/Purple/icon_svg/setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/White/icon_svg/white/adjust.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_setting.setIcon(icon4)
        self.btn_main_indi_setting.setIconSize(QSize(35, 35))

        self.verticalLayout_7.addWidget(self.btn_main_indi_setting, 0, Qt.AlignLeft)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.btn_left_indi_sign_out = QPushButton(self.frm_left_indi)
        self.btn_left_indi_sign_out.setObjectName(u"btn_left_indi_sign_out")
        self.btn_left_indi_sign_out.setMinimumSize(QSize(100, 0))
        self.btn_left_indi_sign_out.setMaximumSize(QSize(100, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/Purple/icon_svg/logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_indi_sign_out.setIcon(icon5)
        self.btn_left_indi_sign_out.setIconSize(QSize(30, 30))
        self.btn_left_indi_sign_out.setCheckable(False)

        self.verticalLayout_7.addWidget(self.btn_left_indi_sign_out, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.frm_left_indi)

        self.frm_ma = QWidget(self.frm_main_)
        self.frm_ma.setObjectName(u"frm_ma")
        self.verticalLayout_24 = QVBoxLayout(self.frm_ma)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frm_ma_top = QFrame(self.frm_ma)
        self.frm_ma_top.setObjectName(u"frm_ma_top")
        self.frm_ma_top.setMinimumSize(QSize(0, 60))
        self.frm_ma_top.setMaximumSize(QSize(16777215, 60))
        self.frm_ma_top.setStyleSheet(u"background: #888")
        self.frm_ma_top.setFrameShape(QFrame.StyledPanel)
        self.frm_ma_top.setFrameShadow(QFrame.Raised)
        self.frm_ma_top.setLineWidth(1)
        self.horizontalLayout_6 = QHBoxLayout(self.frm_ma_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frm_main_header_menu = QWidget(self.frm_ma_top)
        self.frm_main_header_menu.setObjectName(u"frm_main_header_menu")
        self.frm_main_header_menu.setMinimumSize(QSize(0, 0))
        self.frm_main_header_menu.setMaximumSize(QSize(16777215, 60))
        self.frm_main_header_menu.setMouseTracking(True)
        self.frm_main_header_menu.setFocusPolicy(Qt.ClickFocus)
        self.frm_main_header_menu.setAutoFillBackground(False)
        self.frm_main_header_menu.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.frm_main_header_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 5, 20, 5)
        self.btn_main_header_menu = QPushButton(self.frm_main_header_menu)
        self.btn_main_header_menu.setObjectName(u"btn_main_header_menu")
        self.btn_main_header_menu.setMinimumSize(QSize(40, 40))
        self.btn_main_header_menu.setMaximumSize(QSize(40, 40))
        self.btn_main_header_menu.setMouseTracking(True)
        self.btn_main_header_menu.setTabletTracking(True)
        self.btn_main_header_menu.setFocusPolicy(Qt.ClickFocus)
        self.btn_main_header_menu.setContextMenuPolicy(Qt.NoContextMenu)
        self.btn_main_header_menu.setLayoutDirection(Qt.RightToLeft)
        self.btn_main_header_menu.setAutoFillBackground(False)
        self.btn_main_header_menu.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Purple/icon_svg/hamburger-menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_menu.setIcon(icon6)
        self.btn_main_header_menu.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.btn_main_header_menu)

        self.lb_main_header_menu = QLabel(self.frm_main_header_menu)
        self.lb_main_header_menu.setObjectName(u"lb_main_header_menu")
        self.lb_main_header_menu.setMinimumSize(QSize(0, 0))
        self.lb_main_header_menu.setMaximumSize(QSize(16777215, 16777215))
        self.lb_main_header_menu.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.lb_main_header_menu)


        self.horizontalLayout_6.addWidget(self.frm_main_header_menu, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frm_main_header_search_bar = QWidget(self.frm_ma_top)
        self.frm_main_header_search_bar.setObjectName(u"frm_main_header_search_bar")
        self.frm_main_header_search_bar.setMinimumSize(QSize(0, 30))
        self.frm_main_header_search_bar.setMaximumSize(QSize(1000, 30))
        self.frm_main_header_search_bar.setMouseTracking(True)
        self.frm_main_header_search_bar.setFocusPolicy(Qt.ClickFocus)
        self.frm_main_header_search_bar.setAutoFillBackground(False)
        self.frm_main_header_search_bar.setStyleSheet(u"QWidget {\n"
"    border: 2px solid purple; /* \u0110\u1ed9 d\u00e0y vi\u1ec1n l\u00e0 2px, m\u00e0u \u0111en */\n"
"    border-radius: 10px;      /* G\u00f3c vi\u1ec1n bo tr\u00f2n (t\u00f9y ch\u1ecdn) */\n"
"}\n"
"\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.frm_main_header_search_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(10, 0, 5, 0)
        self.btn_main_header_search_bar = QPushButton(self.frm_main_header_search_bar)
        self.btn_main_header_search_bar.setObjectName(u"btn_main_header_search_bar")
        self.btn_main_header_search_bar.setStyleSheet(u"border: none")
        icon7 = QIcon()
        icon7.addFile(u":/Purple/icon_svg/glass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_search_bar.setIcon(icon7)
        self.btn_main_header_search_bar.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btn_main_header_search_bar)

        self.le_main_header_search_bar = QLineEdit(self.frm_main_header_search_bar)
        self.le_main_header_search_bar.setObjectName(u"le_main_header_search_bar")
        self.le_main_header_search_bar.setMinimumSize(QSize(200, 0))
        self.le_main_header_search_bar.setMaximumSize(QSize(1200, 16777215))
        self.le_main_header_search_bar.setStyleSheet(u"QWidget {\n"
"    border: none;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.le_main_header_search_bar)


        self.horizontalLayout_6.addWidget(self.frm_main_header_search_bar, 0, Qt.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.frm_main_header_user = QWidget(self.frm_ma_top)
        self.frm_main_header_user.setObjectName(u"frm_main_header_user")
        self.frm_main_header_user.setMaximumSize(QSize(60, 60))
        self.frm_main_header_user.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.frm_main_header_user)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.btn_main_header_user = QPushButton(self.frm_main_header_user)
        self.btn_main_header_user.setObjectName(u"btn_main_header_user")
        self.btn_main_header_user.setMinimumSize(QSize(40, 40))
        self.btn_main_header_user.setSizeIncrement(QSize(40, 40))
        icon8 = QIcon()
        icon8.addFile(u":/Purple/icon_svg/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_user.setIcon(icon8)
        self.btn_main_header_user.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.btn_main_header_user, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frm_main_header_user)


        self.verticalLayout_24.addWidget(self.frm_ma_top)

        self.frm_main = QStackedWidget(self.frm_ma)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setStyleSheet(u"background: #888")
        self.frm_main.setFrameShape(QFrame.StyledPanel)
        self.frm_main.setFrameShadow(QFrame.Raised)
        self.frm_main_menu = QWidget()
        self.frm_main_menu.setObjectName(u"frm_main_menu")
        self.verticalLayout_2 = QVBoxLayout(self.frm_main_menu)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_main_center = QFrame(self.frm_main_menu)
        self.frm_main_center.setObjectName(u"frm_main_center")
        self.frm_main_center.setMaximumSize(QSize(16777215, 200))
        self.frm_main_center.setStyleSheet(u"background: #777")
        self.frm_main_center.setFrameShape(QFrame.StyledPanel)
        self.frm_main_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_main_center)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(70, 10, 70, 0)
        self.lb_main_content_center_tamsohoc = QLabel(self.frm_main_center)
        self.lb_main_content_center_tamsohoc.setObjectName(u"lb_main_content_center_tamsohoc")
        self.lb_main_content_center_tamsohoc.setMaximumSize(QSize(1500, 30))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lb_main_content_center_tamsohoc.setFont(font)
        self.lb_main_content_center_tamsohoc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_main_content_center_tamsohoc)

        self.glo_main_search = QGridLayout()
        self.glo_main_search.setObjectName(u"glo_main_search")
        self.glo_main_search.setHorizontalSpacing(30)
        self.glo_main_search.setVerticalSpacing(7)
        self.lb_main_search_time = QLabel(self.frm_main_center)
        self.lb_main_search_time.setObjectName(u"lb_main_search_time")

        self.glo_main_search.addWidget(self.lb_main_search_time, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.glo_main_search.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.lb_main_search_day = QLabel(self.frm_main_center)
        self.lb_main_search_day.setObjectName(u"lb_main_search_day")

        self.glo_main_search.addWidget(self.lb_main_search_day, 4, 0, 1, 1)

        self.le_main_search_day = QLineEdit(self.frm_main_center)
        self.le_main_search_day.setObjectName(u"le_main_search_day")

        self.glo_main_search.addWidget(self.le_main_search_day, 5, 0, 1, 1)

        self.le_main_search_name = QLineEdit(self.frm_main_center)
        self.le_main_search_name.setObjectName(u"le_main_search_name")

        self.glo_main_search.addWidget(self.le_main_search_name, 3, 0, 1, 4)

        self.le_main_search_month = QLineEdit(self.frm_main_center)
        self.le_main_search_month.setObjectName(u"le_main_search_month")

        self.glo_main_search.addWidget(self.le_main_search_month, 5, 1, 1, 1)

        self.lb_main_search_year = QLabel(self.frm_main_center)
        self.lb_main_search_year.setObjectName(u"lb_main_search_year")

        self.glo_main_search.addWidget(self.lb_main_search_year, 4, 2, 1, 1)

        self.lb_main_search_name = QLabel(self.frm_main_center)
        self.lb_main_search_name.setObjectName(u"lb_main_search_name")

        self.glo_main_search.addWidget(self.lb_main_search_name, 2, 0, 1, 1)

        self.btn_main_search_tracuu = QPushButton(self.frm_main_center)
        self.btn_main_search_tracuu.setObjectName(u"btn_main_search_tracuu")
        self.btn_main_search_tracuu.setMaximumSize(QSize(16777215, 16777215))

        self.glo_main_search.addWidget(self.btn_main_search_tracuu, 7, 1, 1, 2)

        self.le_main_search_year = QLineEdit(self.frm_main_center)
        self.le_main_search_year.setObjectName(u"le_main_search_year")

        self.glo_main_search.addWidget(self.le_main_search_year, 5, 2, 1, 1)

        self.lb_main_search_month = QLabel(self.frm_main_center)
        self.lb_main_search_month.setObjectName(u"lb_main_search_month")

        self.glo_main_search.addWidget(self.lb_main_search_month, 4, 1, 1, 1)

        self.le_main_search_time = QLineEdit(self.frm_main_center)
        self.le_main_search_time.setObjectName(u"le_main_search_time")

        self.glo_main_search.addWidget(self.le_main_search_time, 5, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.glo_main_search)


        self.verticalLayout_2.addWidget(self.frm_main_center)

        self.frm_main_bot = QTabWidget(self.frm_main_menu)
        self.frm_main_bot.setObjectName(u"frm_main_bot")
        self.frm_main_bot.setStyleSheet(u"background: #777")
        self.frm_main_bot_so_do = QWidget()
        self.frm_main_bot_so_do.setObjectName(u"frm_main_bot_so_do")
        self.verticalLayout_6 = QVBoxLayout(self.frm_main_bot_so_do)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frm_main_bot_content_sodo = QFrame(self.frm_main_bot_so_do)
        self.frm_main_bot_content_sodo.setObjectName(u"frm_main_bot_content_sodo")
        self.frm_main_bot_content_sodo.setStyleSheet(u"background: #666")
        self.frm_main_bot_content_sodo.setFrameShape(QFrame.StyledPanel)
        self.frm_main_bot_content_sodo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frm_main_bot_content_sodo)

        self.frm_main_bot.addTab(self.frm_main_bot_so_do, "")
        self.frm_main_bot_nguhanh = QWidget()
        self.frm_main_bot_nguhanh.setObjectName(u"frm_main_bot_nguhanh")
        self.frm_main_bot.addTab(self.frm_main_bot_nguhanh, "")
        self.frm_main_bot_han = QWidget()
        self.frm_main_bot_han.setObjectName(u"frm_main_bot_han")
        self.frm_main_bot.addTab(self.frm_main_bot_han, "")
        self.frm_main_bot_tamhop = QWidget()
        self.frm_main_bot_tamhop.setObjectName(u"frm_main_bot_tamhop")
        self.frm_main_bot.addTab(self.frm_main_bot_tamhop, "")
        self.frm_main_bot_dokiep = QWidget()
        self.frm_main_bot_dokiep.setObjectName(u"frm_main_bot_dokiep")
        self.frm_main_bot.addTab(self.frm_main_bot_dokiep, "")
        self.frm_main_bot_ten = QWidget()
        self.frm_main_bot_ten.setObjectName(u"frm_main_bot_ten")
        self.frm_main_bot.addTab(self.frm_main_bot_ten, "")

        self.verticalLayout_2.addWidget(self.frm_main_bot)

        self.frm_main.addWidget(self.frm_main_menu)
        self.frm_main_intro = QWidget()
        self.frm_main_intro.setObjectName(u"frm_main_intro")
        self.horizontalLayout_21 = QHBoxLayout(self.frm_main_intro)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame = QFrame(self.frm_main_intro)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: #999")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lb_bot_tamsohoc = QLabel(self.frame)
        self.lb_bot_tamsohoc.setObjectName(u"lb_bot_tamsohoc")
        self.lb_bot_tamsohoc.setMaximumSize(QSize(16777215, 30))
        self.lb_bot_tamsohoc.setFont(font)
        self.lb_bot_tamsohoc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.lb_bot_tamsohoc)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: #888")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.verticalLayout_18.addWidget(self.frame_2)


        self.horizontalLayout_21.addWidget(self.frame)

        self.frm_main.addWidget(self.frm_main_intro)
        self.frm_main_lib = QWidget()
        self.frm_main_lib.setObjectName(u"frm_main_lib")
        self.verticalLayout_23 = QVBoxLayout(self.frm_main_lib)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.lb_bot_tamsohoc_2 = QLabel(self.frm_main_lib)
        self.lb_bot_tamsohoc_2.setObjectName(u"lb_bot_tamsohoc_2")
        self.lb_bot_tamsohoc_2.setMaximumSize(QSize(16777215, 30))
        self.lb_bot_tamsohoc_2.setFont(font)
        self.lb_bot_tamsohoc_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.lb_bot_tamsohoc_2)

        self.frame_3 = QFrame(self.frm_main_lib)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background: #999")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background: #888")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.verticalLayout_21.addWidget(self.frame_4)


        self.verticalLayout_23.addWidget(self.frame_3)

        self.frm_main.addWidget(self.frm_main_lib)
        self.frm_main_account = QWidget()
        self.frm_main_account.setObjectName(u"frm_main_account")
        self.verticalLayout_30 = QVBoxLayout(self.frm_main_account)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frm_setting_bar = QWidget(self.frm_main_account)
        self.frm_setting_bar.setObjectName(u"frm_setting_bar")
        self.frm_setting_bar.setMinimumSize(QSize(0, 40))
        self.frm_setting_bar.setStyleSheet(u"background: rgb(136, 136, 136)")
        self.horizontalLayout_2 = QHBoxLayout(self.frm_setting_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_setting_bar = QLabel(self.frm_setting_bar)
        self.lb_setting_bar.setObjectName(u"lb_setting_bar")

        self.horizontalLayout_2.addWidget(self.lb_setting_bar)


        self.verticalLayout_30.addWidget(self.frm_setting_bar)

        self.frm_main_setting_bar = QWidget(self.frm_main_account)
        self.frm_main_setting_bar.setObjectName(u"frm_main_setting_bar")
        self.frm_main_setting_bar.setMinimumSize(QSize(494, 0))
        self.frm_main_setting_bar.setStyleSheet(u"background: #999")
        self.verticalLayout_25 = QVBoxLayout(self.frm_main_setting_bar)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frm_menu_bar = QFrame(self.frm_main_setting_bar)
        self.frm_menu_bar.setObjectName(u"frm_menu_bar")
        self.frm_menu_bar.setMaximumSize(QSize(16777215, 160))
        self.frm_menu_bar.setLayoutDirection(Qt.LeftToRight)
        self.frm_menu_bar.setStyleSheet(u"background: #888")
        self.frm_menu_bar.setFrameShape(QFrame.StyledPanel)
        self.frm_menu_bar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frm_menu_bar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.lb_menu_bar_id = QLabel(self.frm_menu_bar)
        self.lb_menu_bar_id.setObjectName(u"lb_menu_bar_id")
        self.lb_menu_bar_id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_menu_bar_id, 2, 1, 1, 1)

        self.lb_menu_bar_name = QLabel(self.frm_menu_bar)
        self.lb_menu_bar_name.setObjectName(u"lb_menu_bar_name")
        self.lb_menu_bar_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_menu_bar_name, 1, 1, 1, 1)

        self.widget_menu_bar_image = QWidget(self.frm_menu_bar)
        self.widget_menu_bar_image.setObjectName(u"widget_menu_bar_image")
        self.widget_menu_bar_image.setMinimumSize(QSize(80, 80))

        self.gridLayout.addWidget(self.widget_menu_bar_image, 0, 1, 1, 1)

        self.lb_menu_bar_time_pre = QLabel(self.frm_menu_bar)
        self.lb_menu_bar_time_pre.setObjectName(u"lb_menu_bar_time_pre")
        self.lb_menu_bar_time_pre.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_menu_bar_time_pre, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.frm_menu_bar)

        self.box_main_account = QGroupBox(self.frm_main_setting_bar)
        self.box_main_account.setObjectName(u"box_main_account")
        self.verticalLayout_26 = QVBoxLayout(self.box_main_account)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frm_setting_1 = QFrame(self.box_main_account)
        self.frm_setting_1.setObjectName(u"frm_setting_1")
        self.frm_setting_1.setMaximumSize(QSize(16777215, 75))
        self.frm_setting_1.setStyleSheet(u"background: #777")
        self.frm_setting_1.setFrameShape(QFrame.StyledPanel)
        self.frm_setting_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frm_setting_1)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.btn_setting_1_taikhoan = QPushButton(self.frm_setting_1)
        self.btn_setting_1_taikhoan.setObjectName(u"btn_setting_1_taikhoan")

        self.verticalLayout_27.addWidget(self.btn_setting_1_taikhoan)

        self.btn_setting_1_napthem = QPushButton(self.frm_setting_1)
        self.btn_setting_1_napthem.setObjectName(u"btn_setting_1_napthem")

        self.verticalLayout_27.addWidget(self.btn_setting_1_napthem)


        self.verticalLayout_26.addWidget(self.frm_setting_1)

        self.frm_setting_2 = QFrame(self.box_main_account)
        self.frm_setting_2.setObjectName(u"frm_setting_2")
        self.frm_setting_2.setMaximumSize(QSize(16777215, 75))
        self.frm_setting_2.setStyleSheet(u"background: #777")
        self.frm_setting_2.setFrameShape(QFrame.StyledPanel)
        self.frm_setting_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frm_setting_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.btn_setting_2_hotro = QPushButton(self.frm_setting_2)
        self.btn_setting_2_hotro.setObjectName(u"btn_setting_2_hotro")

        self.verticalLayout_28.addWidget(self.btn_setting_2_hotro)

        self.btn_setting_2_dieukhoan = QPushButton(self.frm_setting_2)
        self.btn_setting_2_dieukhoan.setObjectName(u"btn_setting_2_dieukhoan")

        self.verticalLayout_28.addWidget(self.btn_setting_2_dieukhoan)


        self.verticalLayout_26.addWidget(self.frm_setting_2)

        self.frm_setting_3 = QFrame(self.box_main_account)
        self.frm_setting_3.setObjectName(u"frm_setting_3")
        self.frm_setting_3.setMaximumSize(QSize(16777215, 105))
        self.frm_setting_3.setStyleSheet(u"background: #777")
        self.frm_setting_3.setFrameShape(QFrame.StyledPanel)
        self.frm_setting_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frm_setting_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.btn_setting_3_website = QPushButton(self.frm_setting_3)
        self.btn_setting_3_website.setObjectName(u"btn_setting_3_website")

        self.verticalLayout_29.addWidget(self.btn_setting_3_website)

        self.btn_setting_3_lienhe = QPushButton(self.frm_setting_3)
        self.btn_setting_3_lienhe.setObjectName(u"btn_setting_3_lienhe")

        self.verticalLayout_29.addWidget(self.btn_setting_3_lienhe)

        self.pushButton_12 = QPushButton(self.frm_setting_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_29.addWidget(self.pushButton_12)


        self.verticalLayout_26.addWidget(self.frm_setting_3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_8)


        self.verticalLayout_25.addWidget(self.box_main_account)

        self.lb_info = QLabel(self.frm_main_setting_bar)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setMaximumSize(QSize(16777215, 90))
        self.lb_info.setStyleSheet(u"background: #888")

        self.verticalLayout_25.addWidget(self.lb_info)


        self.verticalLayout_30.addWidget(self.frm_main_setting_bar)

        self.frm_main.addWidget(self.frm_main_account)

        self.verticalLayout_24.addWidget(self.frm_main)


        self.horizontalLayout_8.addWidget(self.frm_ma)


        self.verticalLayout_5.addWidget(self.frm_main_)


        self.verticalLayout.addWidget(self.frm_center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.frm_main.setCurrentIndex(0)
        self.frm_main_bot.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_minimize_obj.setText("")
        self.btn_resize_obj.setText("")
        self.btn_end_obj.setText("")
        self.left_indi_user_image.setText("")
        self.btn_left_indi_user.setText(QCoreApplication.translate("MainWindow", u"T\u00ean:", None))
        self.left_indi_user_id.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.btn_main_indi_menu.setText(QCoreApplication.translate("MainWindow", u"Trang ch\u1ee7", None))
        self.btn_main_indi_intro.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi thi\u1ec7u", None))
        self.btn_main_indi_libary.setText(QCoreApplication.translate("MainWindow", u"Th\u01b0 vi\u1ec7n", None))
        self.btn_main_indi_setting.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.btn_left_indi_sign_out.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.btn_main_header_menu.setText("")
        self.lb_main_header_menu.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        self.btn_main_header_search_bar.setText("")
        self.btn_main_header_user.setText("")
        self.lb_main_content_center_tamsohoc.setText(QCoreApplication.translate("MainWindow", u"T\u00c2M S\u1ed0 H\u1eccC", None))
        self.lb_main_search_time.setText(QCoreApplication.translate("MainWindow", u"* Gi\u1edd sinh", None))
        self.lb_main_search_day.setText(QCoreApplication.translate("MainWindow", u"* Ng\u00e0y sinh", None))
        self.lb_main_search_year.setText(QCoreApplication.translate("MainWindow", u"* N\u0103m sinh", None))
        self.lb_main_search_name.setText(QCoreApplication.translate("MainWindow", u"* H\u1ecd t\u00ean:", None))
        self.btn_main_search_tracuu.setText(QCoreApplication.translate("MainWindow", u"Tra c\u1ee9u ngay", None))
        self.lb_main_search_month.setText(QCoreApplication.translate("MainWindow", u"* Th\u00e1ng sinh ", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_so_do), QCoreApplication.translate("MainWindow", u"S\u01a1 \u0111\u1ed3", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_nguhanh), QCoreApplication.translate("MainWindow", u"Ng\u0169 h\u00e0nh", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_han), QCoreApplication.translate("MainWindow", u"H\u1ea1n", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_tamhop), QCoreApplication.translate("MainWindow", u"Tam h\u1ee3p v\u00e0 C\u00e1nh cung", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_dokiep), QCoreApplication.translate("MainWindow", u"\u0110\u1ed9 ki\u1ebfp", None))
        self.frm_main_bot.setTabText(self.frm_main_bot.indexOf(self.frm_main_bot_ten), QCoreApplication.translate("MainWindow", u"T\u00ean", None))
        self.lb_bot_tamsohoc.setText(QCoreApplication.translate("MainWindow", u"GI\u1edaI THI\u1ec6U", None))
        self.lb_bot_tamsohoc_2.setText(QCoreApplication.translate("MainWindow", u"TH\u01af VI\u1ec6N TRA C\u1ee8U", None))
        self.lb_setting_bar.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin c\u00e1 nh\u00e2n v\u00e0 \u0111i\u1ec1u kho\u1ea3n \u1ee9ng d\u1ee5ng", None))
        self.lb_menu_bar_id.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_menu_bar_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lb_menu_bar_time_pre.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.box_main_account.setTitle(QCoreApplication.translate("MainWindow", u"Ti\u1ec7n \u00edch", None))
        self.btn_setting_1_taikhoan.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin t\u00e0i kho\u1ea3n", None))
        self.btn_setting_1_napthem.setText(QCoreApplication.translate("MainWindow", u"N\u1ea1p th\u00eam", None))
        self.btn_setting_2_hotro.setText(QCoreApplication.translate("MainWindow", u"Trung t\u00e2m tr\u1ee3 gi\u00fap", None))
        self.btn_setting_2_dieukhoan.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec1u kho\u1ea3n \u1ee9ng d\u1ee5ng", None))
        self.btn_setting_3_website.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.btn_setting_3_lienhe.setText(QCoreApplication.translate("MainWindow", u"Li\u00ean h\u1ec7 h\u1ee3p t\u00e1c ho\u1eb7c g\u00f3p \u00fd", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e1nh gi\u00e1 ", None))
        self.lb_info.setText(QCoreApplication.translate("MainWindow", u"Phi\u00ean b\u1ea3n:...........", None))
    # retranslateUi

