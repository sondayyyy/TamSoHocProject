# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingwuAXnR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_setting_popup(object):
    def setupUi(self, setting_popup):
        if not setting_popup.objectName():
            setting_popup.setObjectName(u"setting_popup")
        setting_popup.resize(300, 408)
        setting_popup.setMinimumSize(QSize(300, 0))
        setting_popup.setMaximumSize(QSize(300, 16777215))
        setting_popup.setStyleSheet(u"background: rgb(243, 243, 243)")
        self.verticalLayout = QVBoxLayout(setting_popup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_setting_popup = QWidget(setting_popup)
        self.frm_setting_popup.setObjectName(u"frm_setting_popup")
        self.horizontalLayout = QHBoxLayout(self.frm_setting_popup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_setting_popup = QLabel(self.frm_setting_popup)
        self.lb_setting_popup.setObjectName(u"lb_setting_popup")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lb_setting_popup.setFont(font)

        self.horizontalLayout.addWidget(self.lb_setting_popup)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_setting_popup_fullscrean = QPushButton(self.frm_setting_popup)
        self.btn_setting_popup_fullscrean.setObjectName(u"btn_setting_popup_fullscrean")
        icon = QIcon()
        icon.addFile(u":/Purple/icon_svg/full-screen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_popup_fullscrean.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_setting_popup_fullscrean)

        self.btn_setting_popup_restart = QPushButton(self.frm_setting_popup)
        self.btn_setting_popup_restart.setObjectName(u"btn_setting_popup_restart")
        icon1 = QIcon()
        icon1.addFile(u":/Purple/icon_svg/restart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_popup_restart.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_setting_popup_restart)

        self.btn_setting_popup_end = QPushButton(self.frm_setting_popup)
        self.btn_setting_popup_end.setObjectName(u"btn_setting_popup_end")
        icon2 = QIcon()
        icon2.addFile(u":/Purple/icon_svg/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_popup_end.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_setting_popup_end)


        self.verticalLayout.addWidget(self.frm_setting_popup)

        self.frm_indi = QWidget(setting_popup)
        self.frm_indi.setObjectName(u"frm_indi")
        self.verticalLayout_2 = QVBoxLayout(self.frm_indi)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frm_indi_mode = QFrame(self.frm_indi)
        self.frm_indi_mode.setObjectName(u"frm_indi_mode")
        self.frm_indi_mode.setFrameShape(QFrame.StyledPanel)
        self.frm_indi_mode.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_indi_mode)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.indi_mode_image = QLabel(self.frm_indi_mode)
        self.indi_mode_image.setObjectName(u"indi_mode_image")
        self.indi_mode_image.setMaximumSize(QSize(30, 30))
        self.indi_mode_image.setPixmap(QPixmap(u":/Purple/icon_svg/cloudy.svg"))
        self.indi_mode_image.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.indi_mode_image)

        self.indi_mode_text = QLabel(self.frm_indi_mode)
        self.indi_mode_text.setObjectName(u"indi_mode_text")

        self.horizontalLayout_2.addWidget(self.indi_mode_text)

        self.indi_mode_checkbox = QCheckBox(self.frm_indi_mode)
        self.indi_mode_checkbox.setObjectName(u"indi_mode_checkbox")
        self.indi_mode_checkbox.setIconSize(QSize(60, 60))

        self.horizontalLayout_2.addWidget(self.indi_mode_checkbox)


        self.verticalLayout_2.addWidget(self.frm_indi_mode)

        self.frm_indi_contrast = QFrame(self.frm_indi)
        self.frm_indi_contrast.setObjectName(u"frm_indi_contrast")
        self.frm_indi_contrast.setFrameShape(QFrame.StyledPanel)
        self.frm_indi_contrast.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_indi_contrast)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.indi_contrast_image = QLabel(self.frm_indi_contrast)
        self.indi_contrast_image.setObjectName(u"indi_contrast_image")
        self.indi_contrast_image.setMinimumSize(QSize(30, 30))
        self.indi_contrast_image.setMaximumSize(QSize(30, 30))
        self.indi_contrast_image.setPixmap(QPixmap(u":/Purple/icon_svg/sun.svg"))
        self.indi_contrast_image.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.indi_contrast_image)

        self.indi_contrast_text = QLabel(self.frm_indi_contrast)
        self.indi_contrast_text.setObjectName(u"indi_contrast_text")

        self.horizontalLayout_3.addWidget(self.indi_contrast_text)

        self.indi_contrast_checkbox = QCheckBox(self.frm_indi_contrast)
        self.indi_contrast_checkbox.setObjectName(u"indi_contrast_checkbox")
        self.indi_contrast_checkbox.setIconSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.indi_contrast_checkbox)


        self.verticalLayout_2.addWidget(self.frm_indi_contrast)

        self.frm_indi_color = QWidget(self.frm_indi)
        self.frm_indi_color.setObjectName(u"frm_indi_color")
        self.verticalLayout_3 = QVBoxLayout(self.frm_indi_color)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.frm_indi_color_lb = QWidget(self.frm_indi_color)
        self.frm_indi_color_lb.setObjectName(u"frm_indi_color_lb")
        self.horizontalLayout_4 = QHBoxLayout(self.frm_indi_color_lb)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.indi_color_image = QLabel(self.frm_indi_color_lb)
        self.indi_color_image.setObjectName(u"indi_color_image")
        self.indi_color_image.setMinimumSize(QSize(30, 30))
        self.indi_color_image.setMaximumSize(QSize(30, 30))
        self.indi_color_image.setPixmap(QPixmap(u":/Purple/icon_svg/color-picker.svg"))
        self.indi_color_image.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.indi_color_image)

        self.indi_color_text = QLabel(self.frm_indi_color_lb)
        self.indi_color_text.setObjectName(u"indi_color_text")

        self.horizontalLayout_4.addWidget(self.indi_color_text)


        self.verticalLayout_3.addWidget(self.frm_indi_color_lb)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.indi_color_green = QPushButton(self.frm_indi_color)
        self.indi_color_green.setObjectName(u"indi_color_green")
        icon3 = QIcon()
        icon3.addFile(u":/White/icon_svg/white/rows (4).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.indi_color_green.setIcon(icon3)
        self.indi_color_green.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.indi_color_green, 1, 0, 1, 1, Qt.AlignHCenter)

        self.indi_color_purple = QPushButton(self.frm_indi_color)
        self.indi_color_purple.setObjectName(u"indi_color_purple")
        icon4 = QIcon()
        icon4.addFile(u":/White/icon_svg/white/rows (3).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.indi_color_purple.setIcon(icon4)
        self.indi_color_purple.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.indi_color_purple, 0, 0, 1, 1, Qt.AlignHCenter)

        self.indi_color_blue = QPushButton(self.frm_indi_color)
        self.indi_color_blue.setObjectName(u"indi_color_blue")
        icon5 = QIcon()
        icon5.addFile(u":/White/icon_svg/white/rows (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.indi_color_blue.setIcon(icon5)
        self.indi_color_blue.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.indi_color_blue, 0, 1, 1, 1, Qt.AlignHCenter)

        self.indi_color_black = QPushButton(self.frm_indi_color)
        self.indi_color_black.setObjectName(u"indi_color_black")
        icon6 = QIcon()
        icon6.addFile(u":/White/icon_svg/white/rows (5).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.indi_color_black.setIcon(icon6)
        self.indi_color_black.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.indi_color_black, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.frm_indi_color)


        self.verticalLayout.addWidget(self.frm_indi)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(setting_popup)

        QMetaObject.connectSlotsByName(setting_popup)
    # setupUi

    def retranslateUi(self, setting_popup):
        setting_popup.setWindowTitle(QCoreApplication.translate("setting_popup", u"Form", None))
        self.lb_setting_popup.setText(QCoreApplication.translate("setting_popup", u"C\u00e0i \u0111\u1eb7t", None))
        self.btn_setting_popup_fullscrean.setText("")
        self.btn_setting_popup_restart.setText("")
        self.btn_setting_popup_end.setText("")
        self.indi_mode_image.setText("")
        self.indi_mode_text.setText(QCoreApplication.translate("setting_popup", u"Darkmode", None))
        self.indi_mode_checkbox.setText("")
        self.indi_contrast_image.setText("")
        self.indi_contrast_text.setText(QCoreApplication.translate("setting_popup", u"Contrast", None))
        self.indi_contrast_checkbox.setText("")
        self.indi_color_image.setText("")
        self.indi_color_text.setText(QCoreApplication.translate("setting_popup", u"Color", None))
        self.indi_color_green.setText("")
        self.indi_color_purple.setText("")
        self.indi_color_blue.setText("")
        self.indi_color_black.setText("")
    # retranslateUi

