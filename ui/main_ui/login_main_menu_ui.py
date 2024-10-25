# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_main_menuHRTDQl.ui'
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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget, QDialog)

class Ui_LoginMainWindow(QDialog):
    def setupUi(self, LoginMainWindow):
        if not LoginMainWindow.objectName():
            LoginMainWindow.setObjectName(u"LoginMainWindow")
        LoginMainWindow.resize(715, 593)
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

        self.horizontalLayout.addWidget(self.lb_title)

        self.spacer = QSpacerItem(536, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.spacer)

        self.btn_minisize = QPushButton(self.frm_title)
        self.btn_minisize.setObjectName(u"btn_minisize")

        self.horizontalLayout.addWidget(self.btn_minisize)

        self.btn_fullscreen = QPushButton(self.frm_title)
        self.btn_fullscreen.setObjectName(u"btn_fullscreen")

        self.horizontalLayout.addWidget(self.btn_fullscreen)

        self.btn_end = QPushButton(self.frm_title)
        self.btn_end.setObjectName(u"btn_end")

        self.horizontalLayout.addWidget(self.btn_end)


        self.verticalLayout.addWidget(self.frm_title)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777210, 16777215))
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
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
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frm_login_top_2 = QWidget(self.frm_login_top)
        self.frm_login_top_2.setObjectName(u"frm_login_top_2")
        self.frm_login_top_2.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_9 = QHBoxLayout(self.frm_login_top_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, 5, 0, 5)
        self.lb_login = QLabel(self.frm_login_top_2)
        self.lb_login.setObjectName(u"lb_login")

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

        self.widget_5 = QWidget(self.frm_login_top)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(30, -1, 15, -1)
        self.btn_login_enter = QPushButton(self.widget_5)
        self.btn_login_enter.setObjectName(u"btn_login_enter")

        self.horizontalLayout_10.addWidget(self.btn_login_enter)

        self.btn_login_reges = QPushButton(self.widget_5)
        self.btn_login_reges.setObjectName(u"btn_login_reges")

        self.horizontalLayout_10.addWidget(self.btn_login_reges)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addWidget(self.widget_5)


        self.verticalLayout_4.addWidget(self.frm_login_top)

        self.widget = QWidget(self.frm_login)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.widget)

        self.stackedWidget.addWidget(self.frm_login)
        self.frm_regis = QWidget()
        self.frm_regis.setObjectName(u"frm_regis")
        self.verticalLayout_2 = QVBoxLayout(self.frm_regis)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_regis_top_5 = QWidget(self.frm_regis)
        self.frm_regis_top_5.setObjectName(u"frm_regis_top_5")
        self.verticalLayout_11 = QVBoxLayout(self.frm_regis_top_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frm_regis_top = QWidget(self.frm_regis_top_5)
        self.frm_regis_top.setObjectName(u"frm_regis_top")
        self.horizontalLayout_12 = QHBoxLayout(self.frm_regis_top)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, 5, 0, 5)
        self.lb_regis_top = QLabel(self.frm_regis_top)
        self.lb_regis_top.setObjectName(u"lb_regis_top")

        self.horizontalLayout_12.addWidget(self.lb_regis_top)


        self.verticalLayout_11.addWidget(self.frm_regis_top)

        self.frm_regis_account = QWidget(self.frm_regis_top_5)
        self.frm_regis_account.setObjectName(u"frm_regis_account")
        self.horizontalLayout_5 = QHBoxLayout(self.frm_regis_account)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, -1, 15, -1)
        self.lb_regis_account = QLabel(self.frm_regis_account)
        self.lb_regis_account.setObjectName(u"lb_regis_account")

        self.horizontalLayout_5.addWidget(self.lb_regis_account)

        self.le_regis_account = QLineEdit(self.frm_regis_account)
        self.le_regis_account.setObjectName(u"le_regis_account")
        self.le_regis_account.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.le_regis_account)

        self.btn_regis_account = QPushButton(self.frm_regis_account)
        self.btn_regis_account.setObjectName(u"btn_regis_account")

        self.horizontalLayout_5.addWidget(self.btn_regis_account)


        self.verticalLayout_11.addWidget(self.frm_regis_account, 0, Qt.AlignLeft)

        self.frm_regis_password = QWidget(self.frm_regis_top_5)
        self.frm_regis_password.setObjectName(u"frm_regis_password")
        self.horizontalLayout_6 = QHBoxLayout(self.frm_regis_password)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(30, -1, 15, -1)
        self.lb_regis_password = QLabel(self.frm_regis_password)
        self.lb_regis_password.setObjectName(u"lb_regis_password")

        self.horizontalLayout_6.addWidget(self.lb_regis_password)

        self.le_regis_password = QLineEdit(self.frm_regis_password)
        self.le_regis_password.setObjectName(u"le_regis_password")
        self.le_regis_password.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.le_regis_password)

        self.btn_regis_password = QPushButton(self.frm_regis_password)
        self.btn_regis_password.setObjectName(u"btn_regis_password")

        self.horizontalLayout_6.addWidget(self.btn_regis_password)


        self.verticalLayout_11.addWidget(self.frm_regis_password, 0, Qt.AlignLeft)

        self.frm_btn_log = QWidget(self.frm_regis_top_5)
        self.frm_btn_log.setObjectName(u"frm_btn_log")
        self.horizontalLayout_11 = QHBoxLayout(self.frm_btn_log)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(30, -1, 15, -1)
        self.btn_regis_enter = QPushButton(self.frm_btn_log)
        self.btn_regis_enter.setObjectName(u"btn_regis_enter")

        self.horizontalLayout_11.addWidget(self.btn_regis_enter)

        self.btn_regis_forget = QPushButton(self.frm_btn_log)
        self.btn_regis_forget.setObjectName(u"btn_regis_forget")

        self.horizontalLayout_11.addWidget(self.btn_regis_forget)

        self.btn_regis_back = QPushButton(self.frm_btn_log)
        self.btn_regis_back.setObjectName(u"btn_regis_back")

        self.horizontalLayout_11.addWidget(self.btn_regis_back)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)


        self.verticalLayout_11.addWidget(self.frm_btn_log)


        self.verticalLayout_2.addWidget(self.frm_regis_top_5)

        self.widget_2 = QWidget(self.frm_regis)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.frm_regis)

        self.verticalLayout.addWidget(self.stackedWidget)

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

        # LoginMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginMainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoginMainWindow)
    # setupUi

    def retranslateUi(self, LoginMainWindow):
        LoginMainWindow.setWindowTitle(QCoreApplication.translate("LoginMainWindow", u"MainWindow", None))
        self.lb_title.setText(QCoreApplication.translate("LoginMainWindow", u"Title", None))
        self.btn_minisize.setText("")
        self.btn_fullscreen.setText("")
        self.btn_end.setText("")
        self.lb_login.setText(QCoreApplication.translate("LoginMainWindow", u"Login", None))
        self.lb_login_account.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00e0i kho\u1ea3n", None))
        self.btn_login_account.setText("")
        self.lb_login_password.setText(QCoreApplication.translate("LoginMainWindow", u"M\u1eadt kh\u1ea9u", None))
        self.btn_login_password.setText("")
        self.btn_login_enter.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng nh\u1eadp", None))
        self.btn_login_reges.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng k\u00fd ho\u1eb7c Qu\u00ean m\u1eadt kh\u1ea9u", None))
        self.lb_regis_top.setText(QCoreApplication.translate("LoginMainWindow", u"Register", None))
        self.lb_regis_account.setText(QCoreApplication.translate("LoginMainWindow", u"T\u00e0i kho\u1ea3n:", None))
        self.btn_regis_account.setText("")
        self.lb_regis_password.setText(QCoreApplication.translate("LoginMainWindow", u"M\u1eadt kh\u1ea9u:", None))
        self.btn_regis_password.setText("")
        self.btn_regis_enter.setText(QCoreApplication.translate("LoginMainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.btn_regis_forget.setText(QCoreApplication.translate("LoginMainWindow", u"Qu\u00ean m\u1eadt kh\u1ea9u", None))
        self.btn_regis_back.setText(QCoreApplication.translate("LoginMainWindow", u"Quay l\u1ea1i \u0111\u0103ng nh\u1eadp", None))
        self.btn_link_www.setText("")
        self.lb_version.setText(QCoreApplication.translate("LoginMainWindow", u"Version: .....", None))
    # retranslateUi

