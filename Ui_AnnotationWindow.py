# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnnotationWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_AnnotationWindow(object):
    def setupUi(self, AnnotationWindow):
        if not AnnotationWindow.objectName():
            AnnotationWindow.setObjectName(u"AnnotationWindow")
        AnnotationWindow.resize(192, 186)
        self.labelForUser = QLabel(AnnotationWindow)
        self.labelForUser.setObjectName(u"labelForUser")
        self.labelForUser.setGeometry(QRect(10, 10, 171, 91))
        self.comboBoxDecision = QComboBox(AnnotationWindow)
        self.comboBoxDecision.setObjectName(u"comboBoxDecision")
        self.comboBoxDecision.setGeometry(QRect(10, 110, 171, 22))
        self.pushButtonAccept = QPushButton(AnnotationWindow)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")
        self.pushButtonAccept.setGeometry(QRect(10, 140, 81, 24))
        self.pushButtonCancel = QPushButton(AnnotationWindow)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(100, 140, 81, 24))

        self.retranslateUi(AnnotationWindow)

        QMetaObject.connectSlotsByName(AnnotationWindow)
    # setupUi

    def retranslateUi(self, AnnotationWindow):
        AnnotationWindow.setWindowTitle(QCoreApplication.translate("AnnotationWindow", u"Annotation", None))
        self.labelForUser.setText(QCoreApplication.translate("AnnotationWindow", u"TextLabel", None))
        self.pushButtonAccept.setText(QCoreApplication.translate("AnnotationWindow", u"Accept", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("AnnotationWindow", u"Cancel", None))
    # retranslateUi

