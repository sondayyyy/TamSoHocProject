# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menusEHfEE.ui'
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
import resource_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 750)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(30, 30))
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.centralwidget.setToolTipDuration(0)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_center = QFrame(self.centralwidget)
        self.frm_center.setObjectName(u"frm_center")
        self.frm_center.setStyleSheet(u"")
        self.frm_center.setFrameShape(QFrame.StyledPanel)
        self.frm_center.setFrameShadow(QFrame.Sunken)
        self.frm_center.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frm_center)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 15, 15, 15)
        self.frm_left_indi = QWidget(self.frm_center)
        self.frm_left_indi.setObjectName(u"frm_left_indi")
        self.frm_left_indi.setMinimumSize(QSize(170, 0))
        self.frm_left_indi.setToolTipDuration(0)
        self.frm_left_indi.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.frm_left_indi)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.lb_logo = QLabel(self.frm_left_indi)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMinimumSize(QSize(90, 90))
        self.lb_logo.setMaximumSize(QSize(90, 90))
        self.lb_logo.setPixmap(QPixmap(u":/logo/images/png/logo/logo.png"))
        self.lb_logo.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.lb_logo, 0, Qt.AlignHCenter)

        self.btn_main_indi_menu = QPushButton(self.frm_left_indi)
        self.btn_main_indi_menu.setObjectName(u"btn_main_indi_menu")
        self.btn_main_indi_menu.setMinimumSize(QSize(0, 35))
        self.btn_main_indi_menu.setMaximumSize(QSize(16777215, 35))
        self.btn_main_indi_menu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/grey/images/png/grey/home.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/white/images/png/White/home-white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_menu.setIcon(icon)
        self.btn_main_indi_menu.setIconSize(QSize(26, 26))

        self.verticalLayout_7.addWidget(self.btn_main_indi_menu)

        self.btn_main_indi_intro = QPushButton(self.frm_left_indi)
        self.btn_main_indi_intro.setObjectName(u"btn_main_indi_intro")
        self.btn_main_indi_intro.setMinimumSize(QSize(0, 35))
        self.btn_main_indi_intro.setMaximumSize(QSize(16777215, 35))
        self.btn_main_indi_intro.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_main_indi_intro.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/grey/images/png/grey/heartOnHand-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/white/images/png/White/heartOnHand_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_intro.setIcon(icon1)
        self.btn_main_indi_intro.setIconSize(QSize(26, 26))
        self.btn_main_indi_intro.setCheckable(False)
        self.btn_main_indi_intro.setChecked(False)

        self.verticalLayout_7.addWidget(self.btn_main_indi_intro)

        self.btn_main_indi_libary = QPushButton(self.frm_left_indi)
        self.btn_main_indi_libary.setObjectName(u"btn_main_indi_libary")
        self.btn_main_indi_libary.setMinimumSize(QSize(0, 35))
        self.btn_main_indi_libary.setMaximumSize(QSize(16777215, 35))
        icon2 = QIcon()
        icon2.addFile(u":/grey/images/png/grey/book-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/white/images/png/White/book-white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_libary.setIcon(icon2)
        self.btn_main_indi_libary.setIconSize(QSize(26, 26))

        self.verticalLayout_7.addWidget(self.btn_main_indi_libary)

        self.btn_main_indi_setting = QPushButton(self.frm_left_indi)
        self.btn_main_indi_setting.setObjectName(u"btn_main_indi_setting")
        self.btn_main_indi_setting.setMinimumSize(QSize(0, 35))
        self.btn_main_indi_setting.setMaximumSize(QSize(16777215, 35))
        self.btn_main_indi_setting.setSizeIncrement(QSize(0, 0))
        icon3 = QIcon()
        icon3.addFile(u":/grey/images/png/grey/setting-grey.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/white/images/png/White/setting_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_main_indi_setting.setIcon(icon3)
        self.btn_main_indi_setting.setIconSize(QSize(26, 26))
        self.btn_main_indi_setting.setAutoDefault(False)
        self.btn_main_indi_setting.setFlat(False)

        self.verticalLayout_7.addWidget(self.btn_main_indi_setting)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

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
"    border: 1px solid gray; /* \u0110\u1ed9 d\u00e0y vi\u1ec1n l\u00e0 2px, m\u00e0u \u0111en */\n"
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

        self.btn_left_indi_sign_out = QPushButton(self.frm_left_indi)
        self.btn_left_indi_sign_out.setObjectName(u"btn_left_indi_sign_out")
        self.btn_left_indi_sign_out.setMinimumSize(QSize(100, 0))
        self.btn_left_indi_sign_out.setMaximumSize(QSize(100, 16777215))
        self.btn_left_indi_sign_out.setIconSize(QSize(30, 30))
        self.btn_left_indi_sign_out.setCheckable(False)

        self.verticalLayout_7.addWidget(self.btn_left_indi_sign_out, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frm_left_indi)

        self.frm_ma = QWidget(self.frm_center)
        self.frm_ma.setObjectName(u"frm_ma")
        self.verticalLayout_24 = QVBoxLayout(self.frm_ma)
        self.verticalLayout_24.setSpacing(2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frm_ma_top = QWidget(self.frm_ma)
        self.frm_ma_top.setObjectName(u"frm_ma_top")
        self.frm_ma_top.setMinimumSize(QSize(0, 50))
        self.frm_ma_top.setMaximumSize(QSize(16777215, 50))
        self.frm_ma_top.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.frm_ma_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.btn_main_header_menu = QPushButton(self.frm_ma_top)
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
        icon4 = QIcon()
        icon4.addFile(u":/black/images/png/black/menu-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_menu.setIcon(icon4)
        self.btn_main_header_menu.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.btn_main_header_menu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frm_main_header_search_bar = QWidget(self.frm_ma_top)
        self.frm_main_header_search_bar.setObjectName(u"frm_main_header_search_bar")
        self.frm_main_header_search_bar.setMinimumSize(QSize(0, 35))
        self.frm_main_header_search_bar.setMaximumSize(QSize(1000, 35))
        self.frm_main_header_search_bar.setMouseTracking(True)
        self.frm_main_header_search_bar.setFocusPolicy(Qt.ClickFocus)
        self.frm_main_header_search_bar.setAutoFillBackground(False)
        self.frm_main_header_search_bar.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.frm_main_header_search_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.btn_main_header_search_bar = QPushButton(self.frm_main_header_search_bar)
        self.btn_main_header_search_bar.setObjectName(u"btn_main_header_search_bar")
        self.btn_main_header_search_bar.setStyleSheet(u"border: none")
        icon5 = QIcon()
        icon5.addFile(u":/black/images/png/black/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_search_bar.setIcon(icon5)
        self.btn_main_header_search_bar.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btn_main_header_search_bar)

        self.le_main_header_search_bar = QLineEdit(self.frm_main_header_search_bar)
        self.le_main_header_search_bar.setObjectName(u"le_main_header_search_bar")
        self.le_main_header_search_bar.setMinimumSize(QSize(200, 0))
        self.le_main_header_search_bar.setMaximumSize(QSize(1200, 16777215))
        self.le_main_header_search_bar.setStyleSheet(u"QWidget {\n"
"    border: none;\n"
"}\n"
"")
        self.le_main_header_search_bar.setFrame(True)

        self.horizontalLayout_5.addWidget(self.le_main_header_search_bar)


        self.horizontalLayout_6.addWidget(self.frm_main_header_search_bar, 0, Qt.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.btn_main_header_user = QPushButton(self.frm_ma_top)
        self.btn_main_header_user.setObjectName(u"btn_main_header_user")
        self.btn_main_header_user.setMinimumSize(QSize(40, 40))
        self.btn_main_header_user.setSizeIncrement(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/black/images/png/black/user-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_main_header_user.setIcon(icon6)
        self.btn_main_header_user.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.btn_main_header_user)


        self.verticalLayout_24.addWidget(self.frm_ma_top)

        self.frm_main = QStackedWidget(self.frm_ma)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setStyleSheet(u"")
        self.frm_main.setFrameShape(QFrame.StyledPanel)
        self.frm_main.setFrameShadow(QFrame.Raised)
        self.frm_main_menu = QWidget()
        self.frm_main_menu.setObjectName(u"frm_main_menu")
        self.verticalLayout_2 = QVBoxLayout(self.frm_main_menu)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_main_center = QWidget(self.frm_main_menu)
        self.frm_main_center.setObjectName(u"frm_main_center")
        self.frm_main_center.setMinimumSize(QSize(0, 200))
        self.frm_main_center.setMaximumSize(QSize(16777215, 220))
        self.frm_main_center.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.frm_main_center)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(50, 1, 50, 10)
        self.lb_main_content_center_tamsohoc = QLabel(self.frm_main_center)
        self.lb_main_content_center_tamsohoc.setObjectName(u"lb_main_content_center_tamsohoc")
        self.lb_main_content_center_tamsohoc.setMinimumSize(QSize(0, 30))
        self.lb_main_content_center_tamsohoc.setMaximumSize(QSize(1500, 1500))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lb_main_content_center_tamsohoc.setFont(font)
        self.lb_main_content_center_tamsohoc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_main_content_center_tamsohoc)

        self.glo_main_search = QGridLayout()
        self.glo_main_search.setObjectName(u"glo_main_search")
        self.glo_main_search.setHorizontalSpacing(20)
        self.glo_main_search.setVerticalSpacing(1)
        self.le_main_search_day = QLineEdit(self.frm_main_center)
        self.le_main_search_day.setObjectName(u"le_main_search_day")
        self.le_main_search_day.setMinimumSize(QSize(0, 25))

        self.glo_main_search.addWidget(self.le_main_search_day, 5, 0, 1, 1)

        self.lb_main_search_time = QLabel(self.frm_main_center)
        self.lb_main_search_time.setObjectName(u"lb_main_search_time")

        self.glo_main_search.addWidget(self.lb_main_search_time, 4, 3, 1, 1)

        self.le_main_search_name = QLineEdit(self.frm_main_center)
        self.le_main_search_name.setObjectName(u"le_main_search_name")
        self.le_main_search_name.setMinimumSize(QSize(0, 30))

        self.glo_main_search.addWidget(self.le_main_search_name, 3, 0, 1, 4)

        self.lb_main_search_day = QLabel(self.frm_main_center)
        self.lb_main_search_day.setObjectName(u"lb_main_search_day")

        self.glo_main_search.addWidget(self.lb_main_search_day, 4, 0, 1, 1)

        self.lb_main_search_name = QLabel(self.frm_main_center)
        self.lb_main_search_name.setObjectName(u"lb_main_search_name")

        self.glo_main_search.addWidget(self.lb_main_search_name, 2, 0, 1, 1)

        self.le_main_search_time = QLineEdit(self.frm_main_center)
        self.le_main_search_time.setObjectName(u"le_main_search_time")
        self.le_main_search_time.setMinimumSize(QSize(0, 25))

        self.glo_main_search.addWidget(self.le_main_search_time, 5, 3, 1, 1)

        self.lb_main_search_year = QLabel(self.frm_main_center)
        self.lb_main_search_year.setObjectName(u"lb_main_search_year")

        self.glo_main_search.addWidget(self.lb_main_search_year, 4, 2, 1, 1)

        self.btn_main_search_tracuu = QPushButton(self.frm_main_center)
        self.btn_main_search_tracuu.setObjectName(u"btn_main_search_tracuu")
        self.btn_main_search_tracuu.setMaximumSize(QSize(16777215, 16777215))

        self.glo_main_search.addWidget(self.btn_main_search_tracuu, 8, 1, 1, 2)

        self.le_main_search_month = QLineEdit(self.frm_main_center)
        self.le_main_search_month.setObjectName(u"le_main_search_month")
        self.le_main_search_month.setMinimumSize(QSize(0, 25))

        self.glo_main_search.addWidget(self.le_main_search_month, 5, 1, 1, 1)

        self.frame_9 = QFrame(self.frm_main_center)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 20))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.glo_main_search.addWidget(self.frame_9, 7, 2, 1, 1)

        self.lb_main_search_month = QLabel(self.frm_main_center)
        self.lb_main_search_month.setObjectName(u"lb_main_search_month")

        self.glo_main_search.addWidget(self.lb_main_search_month, 4, 1, 1, 1)

        self.le_main_search_year = QLineEdit(self.frm_main_center)
        self.le_main_search_year.setObjectName(u"le_main_search_year")
        self.le_main_search_year.setMinimumSize(QSize(0, 25))

        self.glo_main_search.addWidget(self.le_main_search_year, 5, 2, 1, 1)

        self.btn_export = QPushButton(self.frm_main_center)
        self.btn_export.setObjectName(u"btn_export")

        self.glo_main_search.addWidget(self.btn_export, 8, 3, 1, 1, Qt.AlignLeft)


        self.verticalLayout_4.addLayout(self.glo_main_search)


        self.verticalLayout_2.addWidget(self.frm_main_center)

        self.frm_main_bot = QTabWidget(self.frm_main_menu)
        self.frm_main_bot.setObjectName(u"frm_main_bot")
        self.frm_main_bot.setStyleSheet(u"")
        self.frm_main_bot_so_do = QWidget()
        self.frm_main_bot_so_do.setObjectName(u"frm_main_bot_so_do")
        self.verticalLayout_6 = QVBoxLayout(self.frm_main_bot_so_do)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.frame.setStyleSheet(u"")
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
        self.frame_2.setStyleSheet(u"")
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
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
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
        self.frm_setting_bar.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.frm_setting_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_setting_bar = QLabel(self.frm_setting_bar)
        self.lb_setting_bar.setObjectName(u"lb_setting_bar")

        self.horizontalLayout_2.addWidget(self.lb_setting_bar)


        self.verticalLayout_30.addWidget(self.frm_setting_bar)

        self.frm_main_setting_bar = QWidget(self.frm_main_account)
        self.frm_main_setting_bar.setObjectName(u"frm_main_setting_bar")
        self.frm_main_setting_bar.setMinimumSize(QSize(494, 0))
        self.frm_main_setting_bar.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.frm_main_setting_bar)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frm_menu_bar = QFrame(self.frm_main_setting_bar)
        self.frm_menu_bar.setObjectName(u"frm_menu_bar")
        self.frm_menu_bar.setMaximumSize(QSize(16777215, 160))
        self.frm_menu_bar.setLayoutDirection(Qt.LeftToRight)
        self.frm_menu_bar.setStyleSheet(u"")
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
        self.frm_setting_1.setStyleSheet(u"")
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
        self.frm_setting_2.setStyleSheet(u"")
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
        self.frm_setting_3.setStyleSheet(u"")
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
        self.lb_info.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.lb_info)


        self.verticalLayout_30.addWidget(self.frm_main_setting_bar)

        self.frm_main.addWidget(self.frm_main_account)

        self.verticalLayout_24.addWidget(self.frm_main)


        self.horizontalLayout.addWidget(self.frm_ma)


        self.verticalLayout.addWidget(self.frm_center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_main_indi_setting.setDefault(False)
        self.frm_main.setCurrentIndex(0)
        self.frm_main_bot.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_logo.setText("")
        self.btn_main_indi_menu.setText(QCoreApplication.translate("MainWindow", u"Trang ch\u1ee7", None))
        self.btn_main_indi_intro.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi thi\u1ec7u", None))
        self.btn_main_indi_libary.setText(QCoreApplication.translate("MainWindow", u"Th\u01b0 vi\u1ec7n", None))
        self.btn_main_indi_setting.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0111\u1eb7t", None))
        self.left_indi_user_image.setText("")
        self.btn_left_indi_user.setText(QCoreApplication.translate("MainWindow", u"T\u00ean:", None))
        self.left_indi_user_id.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.btn_left_indi_sign_out.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.btn_main_header_menu.setText("")
        self.btn_main_header_search_bar.setText("")
        self.btn_main_header_user.setText("")
        self.lb_main_content_center_tamsohoc.setText(QCoreApplication.translate("MainWindow", u"T\u00c2M S\u1ed0 H\u1eccC", None))
        self.lb_main_search_time.setText(QCoreApplication.translate("MainWindow", u"* Gi\u1edd sinh", None))
        self.lb_main_search_day.setText(QCoreApplication.translate("MainWindow", u"* Ng\u00e0y sinh", None))
        self.lb_main_search_name.setText(QCoreApplication.translate("MainWindow", u"* H\u1ecd t\u00ean:", None))
        self.lb_main_search_year.setText(QCoreApplication.translate("MainWindow", u"* N\u0103m sinh", None))
        self.btn_main_search_tracuu.setText(QCoreApplication.translate("MainWindow", u"Tra c\u1ee9u ngay", None))
        self.lb_main_search_month.setText(QCoreApplication.translate("MainWindow", u"* Th\u00e1ng sinh ", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
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

