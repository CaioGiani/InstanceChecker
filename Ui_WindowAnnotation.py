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
        AnnotationWindow.resize(270, 159)
        self.labelForInstance = QLabel(AnnotationWindow)
        self.labelForInstance.setObjectName(u"labelForInstance")
        self.labelForInstance.setGeometry(QRect(10, 16, 251, 20))
        self.labelForInstance.setStyleSheet(u"font: 10pt \"Arial\";")
        self.labelForInstance.setTextFormat(Qt.PlainText)
        self.comboBoxDecision = QComboBox(AnnotationWindow)
        self.comboBoxDecision.setObjectName(u"comboBoxDecision")
        self.comboBoxDecision.setGeometry(QRect(10, 90, 251, 22))
        self.pushButtonAccept = QPushButton(AnnotationWindow)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")
        self.pushButtonAccept.setGeometry(QRect(10, 120, 121, 24))
        self.pushButtonCancel = QPushButton(AnnotationWindow)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(140, 120, 121, 24))
        self.labelForDecision = QLabel(AnnotationWindow)
        self.labelForDecision.setObjectName(u"labelForDecision")
        self.labelForDecision.setGeometry(QRect(10, 50, 251, 21))
        self.labelForDecision.setStyleSheet(u"font: 700 12pt \"Arial\";")
        self.labelForDecision.setAlignment(Qt.AlignCenter)

        self.retranslateUi(AnnotationWindow)

        QMetaObject.connectSlotsByName(AnnotationWindow)
    # setupUi

    def retranslateUi(self, AnnotationWindow):
        AnnotationWindow.setWindowTitle(QCoreApplication.translate("AnnotationWindow", u"Annotation", None))
        self.labelForInstance.setText(QCoreApplication.translate("AnnotationWindow", u"Annotation Panel", None))
        self.pushButtonAccept.setText(QCoreApplication.translate("AnnotationWindow", u"Accept", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("AnnotationWindow", u"Cancel", None))
        self.labelForDecision.setText(QCoreApplication.translate("AnnotationWindow", u"Subflorescence & Efflorescence", None))
    # retranslateUi

