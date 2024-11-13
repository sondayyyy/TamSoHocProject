# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_main_menuAHGaUV.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        if not LoginMainWindow.objectName():
            LoginMainWindow.setObjectName(u"LoginMainWindow")
        LoginMainWindow.resize(374, 455)
        self.centralwidget = QWidget(LoginMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_title = QWidget(self.centralwidget)
        self.frm_title.setObjectName(u"frm_title")
        self.frm_title.setMinimumSize(QSize(0, 40))
        self.frm_title.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.frm_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.lb_title = QLabel(self.frm_title)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lb_title.setFont(font)

        self.horizontalLayout.addWidget(self.lb_title)

        self.spacer = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.btn_minisize = QPushButton(self.frm_title)
        self.btn_minisize.setObjectName(u"btn_minisize")

        self.horizontalLayout.addWidget(self.btn_minisize)

        self.btn_end = QPushButton(self.frm_title)
        self.btn_end.setObjectName(u"btn_end")

        self.horizontalLayout.addWidget(self.btn_end)


        self.verticalLayout.addWidget(self.frm_title)

        self.frm_main = QStackedWidget(self.centralwidget)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setMaximumSize(QSize(16777210, 16777215))
        self.frm_main.setFrameShape(QFrame.StyledPanel)
        self.frm_main.setFrameShadow(QFrame.Raised)
        self.frm_login = QWidget()
        self.frm_login.setObjectName(u"frm_login")
        self.verticalLayout_4 = QVBoxLayout(self.frm_login)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frm_login_top = QWidget(self.frm_login)
        self.frm_login_top.setObjectName(u"frm_login_top")
        self.frm_login_top.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.frm_login_top)
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.frm_login_top_2 = QWidget(self.frm_login_top)
        self.frm_login_top_2.setObjectName(u"frm_login_top_2")
        self.frm_login_top_2.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_9 = QHBoxLayout(self.frm_login_top_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, 5, 0, 5)
        self.lb_login = QLabel(self.frm_login_top_2)
        self.lb_login.setObjectName(u"lb_login")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.lb_login.setFont(font1)

        self.horizontalLayout_9.addWidget(self.lb_login)


        self.verticalLayout_10.addWidget(self.frm_login_top_2)

        self.frm_login_account = QWidget(self.frm_login_top)
        self.frm_login_account.setObjectName(u"frm_login_account")
        self.horizontalLayout_4 = QHBoxLayout(self.frm_login_account)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 9, 15, 9)
        self.lb_login_account = QLabel(self.frm_login_account)
        self.lb_login_account.setObjectName(u"lb_login_account")
        self.lb_login_account.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.lb_login_account)

        self.le_login_account = QLineEdit(self.frm_login_account)
        self.le_login_account.setObjectName(u"le_login_account")
        self.le_login_account.setMinimumSize(QSize(200, 0))
        self.le_login_account.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.le_login_account)

        self.btn_login_account = QPushButton(self.frm_login_account)
        self.btn_login_account.setObjectName(u"btn_login_account")

        self.horizontalLayout_4.addWidget(self.btn_login_account)


        self.verticalLayout_10.addWidget(self.frm_login_account, 0, Qt.AlignLeft)

        self.frm_login_password = QWidget(self.frm_login_top)
        self.frm_login_password.setObjectName(u"frm_login_password")
        self.horizontalLayout_3 = QHBoxLayout(self.frm_login_password)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, -1, 15, -1)
        self.lb_login_password = QLabel(self.frm_login_password)
        self.lb_login_password.setObjectName(u"lb_login_password")
        self.lb_login_password.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.lb_login_password)

        self.le_login_password = QLineEdit(self.frm_login_password)
        self.le_login_password.setObjectName(u"le_login_password")
        self.le_login_password.setMinimumSize(QSize(200, 0))
        self.le_login_password.setMaximumSize(QSize(16777215, 16777215))
        self.le_login_password.setSizeIncrement(QSize(120, 0))

        self.horizontalLayout_3.addWidget(self.le_login_password)

        self.btn_login_password = QPushButton(self.frm_login_password)
        self.btn_login_password.setObjectName(u"btn_login_password")

        self.horizontalLayout_3.addWidget(self.btn_login_password)


        self.verticalLayout_10.addWidget(self.frm_login_password, 0, Qt.AlignLeft)

        self.widget_3 = QWidget(self.frm_login_top)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(190, 0, 15, 0)
        self.btn_login_forget = QPushButton(self.widget_3)
        self.btn_login_forget.setObjectName(u"btn_login_forget")
        self.btn_login_forget.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_login_forget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.btn_login_enter = QPushButton(self.frm_login_top)
        self.btn_login_enter.setObjectName(u"btn_login_enter")
        self.btn_login_enter.setMinimumSize(QSize(300, 35))
        self.btn_login_enter.setMaximumSize(QSize(300, 35))

        self.verticalLayout_10.addWidget(self.btn_login_enter, 0, Qt.AlignHCenter)

        self.btn_login_reges = QPushButton(self.frm_login_top)
        self.btn_login_reges.setObjectName(u"btn_login_reges")
        self.btn_login_reges.setMinimumSize(QSize(0, 0))
        self.btn_login_reges.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_10.addWidget(self.btn_login_reges, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frm_login_top)

        self.widget = QWidget(self.frm_login)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_login_google = QPushButton(self.widget_4)
        self.btn_login_google.setObjectName(u"btn_login_google")

        self.horizontalLayout_10.addWidget(self.btn_login_google)

        self.btn_login_facbook = QPushButton(self.widget_4)
        self.btn_login_facbook.setObjectName(u"btn_login_facbook")

        self.horizontalLayout_10.addWidget(self.btn_login_facbook)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.widget)

        self.frm_main.addWidget(self.frm_login)
        self.frm_regis = QWidget()
        self.frm_regis.setObjectName(u"frm_regis")
        self.verticalLayout_2 = QVBoxLayout(self.frm_regis)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_regis_top_5 = QWidget(self.frm_regis)
        self.frm_regis_top_5.setObjectName(u"frm_regis_top_5")
        self.verticalLayout_11 = QVBoxLayout(self.frm_regis_top_5)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.frm_regis_top = QWidget(self.frm_regis_top_5)
        self.frm_regis_top.setObjectName(u"frm_regis_top")
        self.horizontalLayout_12 = QHBoxLayout(self.frm_regis_top)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, 5, 0, 5)
        self.lb_regis_top = QLabel(self.frm_regis_top)
        self.lb_regis_top.setObjectName(u"lb_regis_top")
        self.lb_regis_top.setFont(font1)

        self.horizontalLayout_12.addWidget(self.lb_regis_top)


        self.verticalLayout_11.addWidget(self.frm_regis_top)

        self.frame = QFrame(self.frm_regis_top_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frm_regis_account_3 = QWidget(self.frame)
        self.frm_regis_account_3.setObjectName(u"frm_regis_account_3")
        self.horizontalLayout_21 = QHBoxLayout(self.frm_regis_account_3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(15, -1, 15, -1)
        self.lb_regis_account_3 = QLabel(self.frm_regis_account_3)
        self.lb_regis_account_3.setObjectName(u"lb_regis_account_3")

        self.horizontalLayout_21.addWidget(self.lb_regis_account_3)

        self.le_regis_account_3 = QLineEdit(self.frm_regis_account_3)
        self.le_regis_account_3.setObjectName(u"le_regis_account_3")
        self.le_regis_account_3.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_21.addWidget(self.le_regis_account_3, 0, Qt.AlignRight)

        self.btn_regis_account_3 = QPushButton(self.frm_regis_account_3)
        self.btn_regis_account_3.setObjectName(u"btn_regis_account_3")

        self.horizontalLayout_21.addWidget(self.btn_regis_account_3)


        self.verticalLayout_16.addWidget(self.frm_regis_account_3)

        self.frm_regis_account = QWidget(self.frame)
        self.frm_regis_account.setObjectName(u"frm_regis_account")
        self.horizontalLayout_5 = QHBoxLayout(self.frm_regis_account)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, -1, 15, -1)
        self.lb_regis_account = QLabel(self.frm_regis_account)
        self.lb_regis_account.setObjectName(u"lb_regis_account")

        self.horizontalLayout_5.addWidget(self.lb_regis_account)

        self.le_regis_account = QLineEdit(self.frm_regis_account)
        self.le_regis_account.setObjectName(u"le_regis_account")
        self.le_regis_account.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.le_regis_account, 0, Qt.AlignRight)

        self.btn_regis_account = QPushButton(self.frm_regis_account)
        self.btn_regis_account.setObjectName(u"btn_regis_account")

        self.horizontalLayout_5.addWidget(self.btn_regis_account)


        self.verticalLayout_16.addWidget(self.frm_regis_account)

        self.frm_regis_password = QWidget(self.frame)
        self.frm_regis_password.setObjectName(u"frm_regis_password")
        self.horizontalLayout_6 = QHBoxLayout(self.frm_regis_password)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, -1, 15, -1)
        self.lb_regis_password = QLabel(self.frm_regis_password)
        self.lb_regis_password.setObjectName(u"lb_regis_password")

        self.horizontalLayout_6.addWidget(self.lb_regis_password)

        self.le_regis_password = QLineEdit(self.frm_regis_password)
        self.le_regis_password.setObjectName(u"le_regis_password")
        self.le_regis_password.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.le_regis_password, 0, Qt.AlignRight)

        self.btn_regis_password = QPushButton(self.frm_regis_password)
        self.btn_regis_password.setObjectName(u"btn_regis_password")

        self.horizontalLayout_6.addWidget(self.btn_regis_password)


        self.verticalLayout_16.addWidget(self.frm_regis_password)


        self.verticalLayout_11.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frm_regis_top_5)

        self.widget_2 = QWidget(self.frm_regis)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_regis_enter = QPushButton(self.widget_2)
        self.btn_regis_enter.setObjectName(u"btn_regis_enter")
        self.btn_regis_enter.setMinimumSize(QSize(300, 35))
        self.btn_regis_enter.setMaximumSize(QSize(300, 35))

        self.verticalLayout_3.addWidget(self.btn_regis_enter, 0, Qt.AlignHCenter)

        self.btn_regis_back = QPushButton(self.widget_2)
        self.btn_regis_back.setObjectName(u"btn_regis_back")

        self.verticalLayout_3.addWidget(self.btn_regis_back, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.frm_main.addWidget(self.frm_regis)
        self.frm_forget = QWidget()
        self.frm_forget.setObjectName(u"frm_forget")
        self.verticalLayout_6 = QVBoxLayout(self.frm_forget)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(25, -1, 25, -1)
        self.lb_forget_password = QLabel(self.frm_forget)
        self.lb_forget_password.setObjectName(u"lb_forget_password")
        self.lb_forget_password.setFont(font1)

        self.verticalLayout_6.addWidget(self.lb_forget_password)

        self.lb_forget_password_un = QLabel(self.frm_forget)
        self.lb_forget_password_un.setObjectName(u"lb_forget_password_un")
        font2 = QFont()
        font2.setPointSize(10)
        self.lb_forget_password_un.setFont(font2)

        self.verticalLayout_6.addWidget(self.lb_forget_password_un)

        self.lb_forget_account = QLabel(self.frm_forget)
        self.lb_forget_account.setObjectName(u"lb_forget_account")

        self.verticalLayout_6.addWidget(self.lb_forget_account)

        self.le_forget_account = QLineEdit(self.frm_forget)
        self.le_forget_account.setObjectName(u"le_forget_account")

        self.verticalLayout_6.addWidget(self.le_forget_account)

        self.lb_forget_email = QLabel(self.frm_forget)
        self.lb_forget_email.setObjectName(u"lb_forget_email")

        self.verticalLayout_6.addWidget(self.lb_forget_email)

        self.le_forget_email = QLineEdit(self.frm_forget)
        self.le_forget_email.setObjectName(u"le_forget_email")

        self.verticalLayout_6.addWidget(self.le_forget_email)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.le_forget_captcha = QLineEdit(self.frm_forget)
        self.le_forget_captcha.setObjectName(u"le_forget_captcha")

        self.horizontalLayout_8.addWidget(self.le_forget_captcha)

        self.lb_forget_captcha = QLabel(self.frm_forget)
        self.lb_forget_captcha.setObjectName(u"lb_forget_captcha")

        self.horizontalLayout_8.addWidget(self.lb_forget_captcha)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.btn_forget_enter = QPushButton(self.frm_forget)
        self.btn_forget_enter.setObjectName(u"btn_forget_enter")
        self.btn_forget_enter.setMinimumSize(QSize(300, 35))
        self.btn_forget_enter.setMaximumSize(QSize(300, 35))

        self.verticalLayout_6.addWidget(self.btn_forget_enter, 0, Qt.AlignHCenter)

        self.btn_forget_back = QPushButton(self.frm_forget)
        self.btn_forget_back.setObjectName(u"btn_forget_back")
        self.btn_forget_back.setMinimumSize(QSize(120, 0))
        self.btn_forget_back.setMaximumSize(QSize(120, 16777215))

        self.verticalLayout_6.addWidget(self.btn_forget_back, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 99, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.frm_main.addWidget(self.frm_forget)

        self.verticalLayout.addWidget(self.frm_main)

        self.bot_frm = QWidget(self.centralwidget)
        self.bot_frm.setObjectName(u"bot_frm")
        self.horizontalLayout_7 = QHBoxLayout(self.bot_frm)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_link_www = QPushButton(self.bot_frm)
        self.btn_link_www.setObjectName(u"btn_link_www")

        self.horizontalLayout_7.addWidget(self.btn_link_www)

        self.lb_version = QLabel(self.bot_frm)
        self.lb_version.setObjectName(u"lb_version")

        self.horizontalLayout_7.addWidget(self.lb_version)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.bot_frm)

        LoginMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginMainWindow)

        self.frm_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginMainWindow)
    # setupUi

    def retranslateUi(self, LoginMainWindow):
        LoginMainWindow.setWindowTitle(QCoreApplication.translate("LoginMainWindow", u"MainWindow", None))
        self.lb_title.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00c2M S\u1ed0 H\u1eccC", None))
        self.btn_minisize.setText("")
        self.btn_end.setText("")
        self.lb_login.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.lb_login_account.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.btn_login_account.setText("")
        self.lb_login_password.setText(QCoreApplication.translate("LoginMainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.btn_login_password.setText("")
        self.btn_login_forget.setText(QCoreApplication.translate("LoginMainWindow", u"B\u1ea1n qu\u00ean m\u1eadt kh\u1ea9u?", None))
        self.btn_login_enter.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.btn_login_reges.setText(QCoreApplication.translate("LoginMainWindow", u"B\u1ea5m v\u00e0o \u0111\u00e2y \u0111\u1ec3 \u0111\u0103ng k\u00fd", None))
        self.label.setText(QCoreApplication.translate("LoginMainWindow", u"Ho\u1eb7c c\u00f3 th\u1ec3 \u0111\u0103ng nh\u1eadp b\u1eb1ng:", None))
        self.btn_login_google.setText(QCoreApplication.translate("LoginMainWindow", u"Google", None))
        self.btn_login_facbook.setText(QCoreApplication.translate("LoginMainWindow", u"Facebook", None))
        self.lb_regis_top.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.lb_regis_account_3.setText(QCoreApplication.translate("LoginMainWindow", u"Email:", None))
        self.btn_regis_account_3.setText("")
        self.lb_regis_account.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.btn_regis_account.setText("")
        self.lb_regis_password.setText(QCoreApplication.translate("LoginMainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.btn_regis_password.setText("")
        self.btn_regis_enter.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.btn_regis_back.setText(QCoreApplication.translate("LoginMainWindow", u"Quay l\u1ea1i \u0111\u0103ng nh\u1eadp", None))
        self.lb_forget_password.setText(QCoreApplication.translate("LoginMainWindow", u"Qu\u00ean m\u1eadt kh\u1ea9u?", None))
        self.lb_forget_password_un.setText(QCoreApplication.translate("LoginMainWindow", u"Nh\u1eadp \u0111\u1ecba ch\u1ec9 email \u0111\u1ec3 l\u1ea5y l\u1ea1i m\u1eadt kh\u1ea9u", None))
        self.lb_forget_account.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00ean \u0111\u0103ng nh\u1eadp:", None))
        self.lb_forget_email.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u1ecba ch\u1ec9 email:", None))
        self.lb_forget_captcha.setText(QCoreApplication.translate("LoginMainWindow", u"Nh\u1eadp m\u00e3 capcha", None))
        self.btn_forget_enter.setText(QCoreApplication.translate("LoginMainWindow", u"L\u1ea5y l\u1ea1i m\u1eadt kh\u1ea9u", None))
        self.btn_forget_back.setText(QCoreApplication.translate("LoginMainWindow", u"Tr\u1edf v\u1ec1", None))
        self.btn_link_www.setText("")
        self.lb_version.setText(QCoreApplication.translate("LoginMainWindow", u"Version: .....", None))
    # retranslateUi

