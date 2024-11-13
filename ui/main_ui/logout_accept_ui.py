# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logout_acceptLbPaAP.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LogoutAccept(object):
    def setupUi(self, LogoutAccept):
        if not LogoutAccept.objectName():
            LogoutAccept.setObjectName(u"LogoutAccept")
        LogoutAccept.resize(269, 125)
        LogoutAccept.setMinimumSize(QSize(0, 0))
        LogoutAccept.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(LogoutAccept)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LogoutAccept)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1, 50))
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_continue = QPushButton(self.widget)
        self.btn_continue.setObjectName(u"btn_continue")

        self.horizontalLayout.addWidget(self.btn_continue)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(LogoutAccept)

        QMetaObject.connectSlotsByName(LogoutAccept)
    # setupUi

    def retranslateUi(self, LogoutAccept):
        LogoutAccept.setWindowTitle(QCoreApplication.translate("LogoutAccept", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("LogoutAccept", u"Ti\u1ebfp t\u1ee5c \u0111\u0103ng xu\u1ea5t?", None))
        self.btn_cancel.setText(QCoreApplication.translate("LogoutAccept", u"Hu\u1ef7 b\u1ecf", None))
        self.btn_continue.setText(QCoreApplication.translate("LogoutAccept", u"Ti\u1ebfp t\u1ee5c", None))
    # retranslateUi

