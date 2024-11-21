# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingCrSmJp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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

        self.horizontalLayout.addWidget(self.btn_setting_popup_fullscrean)

        self.btn_setting_popup_restart = QPushButton(self.frm_setting_popup)
        self.btn_setting_popup_restart.setObjectName(u"btn_setting_popup_restart")

        self.horizontalLayout.addWidget(self.btn_setting_popup_restart)

        self.btn_setting_popup_end = QPushButton(self.frm_setting_popup)
        self.btn_setting_popup_end.setObjectName(u"btn_setting_popup_end")

        self.horizontalLayout.addWidget(self.btn_setting_popup_end)


        self.verticalLayout.addWidget(self.frm_setting_popup)

        self.frm_indi = QWidget(setting_popup)
        self.frm_indi.setObjectName(u"frm_indi")
        self.verticalLayout_2 = QVBoxLayout(self.frm_indi)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frm_indi_mode = QWidget(self.frm_indi)
        self.frm_indi_mode.setObjectName(u"frm_indi_mode")
        self.horizontalLayout_2 = QHBoxLayout(self.frm_indi_mode)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.indi_mode_text = QLabel(self.frm_indi_mode)
        self.indi_mode_text.setObjectName(u"indi_mode_text")

        self.horizontalLayout_2.addWidget(self.indi_mode_text)

        self.frm_btn_mode = QFrame(self.frm_indi_mode)
        self.frm_btn_mode.setObjectName(u"frm_btn_mode")
        self.horizontalLayout_5 = QHBoxLayout(self.frm_btn_mode)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.frm_btn_mode)

        self.frame = QFrame(self.frm_indi_mode)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frm_indi_mode)

        self.frm_indi_contrast = QFrame(self.frm_indi)
        self.frm_indi_contrast.setObjectName(u"frm_indi_contrast")
        self.frm_indi_contrast.setFrameShape(QFrame.StyledPanel)
        self.frm_indi_contrast.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_indi_contrast)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.indi_contrast_text = QLabel(self.frm_indi_contrast)
        self.indi_contrast_text.setObjectName(u"indi_contrast_text")

        self.horizontalLayout_3.addWidget(self.indi_contrast_text)

        self.frm_btn_contrast = QFrame(self.frm_indi_contrast)
        self.frm_btn_contrast.setObjectName(u"frm_btn_contrast")
        self.horizontalLayout_6 = QHBoxLayout(self.frm_btn_contrast)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frm_btn_contrast)

        self.frame_2 = QFrame(self.frm_indi_contrast)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)


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
        self.indi_color_green.setFlat(False)

        self.gridLayout.addWidget(self.indi_color_green, 1, 0, 1, 1, Qt.AlignHCenter)

        self.indi_color_purple = QPushButton(self.frm_indi_color)
        self.indi_color_purple.setObjectName(u"indi_color_purple")
#if QT_CONFIG(shortcut)
        self.indi_color_purple.setShortcut(u"")
#endif // QT_CONFIG(shortcut)

        self.gridLayout.addWidget(self.indi_color_purple, 0, 0, 1, 1, Qt.AlignHCenter)

        self.indi_color_blue = QPushButton(self.frm_indi_color)
        self.indi_color_blue.setObjectName(u"indi_color_blue")
        self.indi_color_blue.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.indi_color_blue, 0, 1, 1, 1, Qt.AlignHCenter)

        self.indi_color_black = QPushButton(self.frm_indi_color)
        self.indi_color_black.setObjectName(u"indi_color_black")
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
        self.indi_mode_text.setText(QCoreApplication.translate("setting_popup", u"Darkmode", None))
        self.indi_contrast_text.setText(QCoreApplication.translate("setting_popup", u"Contrast", None))
        self.indi_color_image.setText("")
        self.indi_color_text.setText(QCoreApplication.translate("setting_popup", u"Color", None))
        self.indi_color_green.setText("")
        self.indi_color_purple.setText("")
        self.indi_color_blue.setText("")
        self.indi_color_black.setText("")
    # retranslateUi

