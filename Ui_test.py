# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 714)
        MainWindow.setAnimated(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setAutoRepeat(False)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUser_Manual = QAction(MainWindow)
        self.actionUser_Manual.setObjectName(u"actionUser_Manual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonAccept = QPushButton(self.centralwidget)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")
        self.pushButtonAccept.setGeometry(QRect(660, 530, 111, 23))
        self.pushButtonAbort = QPushButton(self.centralwidget)
        self.pushButtonAbort.setObjectName(u"pushButtonAbort")
        self.pushButtonAbort.setGeometry(QRect(780, 530, 111, 23))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(660, 70, 231, 451))
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.lbImg = QLabel(self.centralwidget)
        self.lbImg.setObjectName(u"lbImg")
        self.lbImg.setGeometry(QRect(10, 10, 640, 640))
        self.lbImg.setMinimumSize(QSize(640, 640))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(127, 127, 127, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        self.lbImg.setPalette(palette)
        self.lbImg.setMouseTracking(True)
        self.lbImg.setAutoFillBackground(False)
        self.lbImg.setFrameShape(QFrame.Panel)
        self.lbImg.setFrameShadow(QFrame.Plain)
        self.lbImg.setLineWidth(1)
        self.lbImg.setMidLineWidth(0)
        self.lbImg.setTextFormat(Qt.PlainText)
        self.lbImg.setScaledContents(True)
        self.lbImg.setAlignment(Qt.AlignCenter)
        self.lbImg.setIndent(0)
        self.pushButtonAnnotation = QPushButton(self.centralwidget)
        self.pushButtonAnnotation.setObjectName(u"pushButtonAnnotation")
        self.pushButtonAnnotation.setGeometry(QRect(660, 10, 231, 24))
        self.pushButtonPrevious = QPushButton(self.centralwidget)
        self.pushButtonPrevious.setObjectName(u"pushButtonPrevious")
        self.pushButtonPrevious.setGeometry(QRect(660, 40, 111, 24))
        self.pushButtonNext = QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(780, 40, 111, 24))
        self.plainTextEditLog = QPlainTextEdit(self.centralwidget)
        self.plainTextEditLog.setObjectName(u"plainTextEditLog")
        self.plainTextEditLog.setGeometry(QRect(660, 560, 231, 91))
        self.plainTextEditLog.setFrameShape(QFrame.NoFrame)
        self.plainTextEditLog.setFrameShadow(QFrame.Plain)
        self.plainTextEditLog.setLineWidth(0)
        self.pushButtonAddInstance = QPushButton(self.centralwidget)
        self.pushButtonAddInstance.setObjectName(u"pushButtonAddInstance")
        self.pushButtonAddInstance.setGeometry(QRect(860, 491, 20, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(True)
        self.pushButtonAddInstance.setFont(font)
        self.pushButtonAddInstance.setText(u"+")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 905, 22))
        self.menuObjectChecker_Ver_0_01 = QMenu(self.menubar)
        self.menuObjectChecker_Ver_0_01.setObjectName(u"menuObjectChecker_Ver_0_01")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuObjectChecker_Ver_0_01.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuObjectChecker_Ver_0_01.addAction(self.actionOpen)
        self.menuObjectChecker_Ver_0_01.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionUser_Manual)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"InstanceChecker     ver.  0.0.1", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open a folder which contains images files and lable txt files", None))
#endif // QT_CONFIG(tooltip)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionUser_Manual.setText(QCoreApplication.translate("MainWindow", u"User Manual", None))
        self.pushButtonAccept.setText(QCoreApplication.translate("MainWindow", u"Accpet", None))
        self.pushButtonAbort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Greatings!</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thank you for using Instance checker.</p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can click [Help] - [User Manual] to find more instruction.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To start the process you have to click [File] - [Open] to open up a folder that contains the Images and Text Files. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By clicking [Show Annotation], you are able to view and edit the annotation by double clicking the bouding box. You have to save or discard the changes before moving to other images.</p></body></html>", None))
        self.lbImg.setText("")
        self.pushButtonAnnotation.setText(QCoreApplication.translate("MainWindow", u"Show && Edit Annotation", None))
        self.pushButtonPrevious.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.pushButtonNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.plainTextEditLog.setPlainText(QCoreApplication.translate("MainWindow", u"Logging...", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAddInstance.setToolTip(QCoreApplication.translate("MainWindow", u"Add annotation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButtonAddInstance.setWhatsThis(QCoreApplication.translate("MainWindow", u"add annotation", None))
#endif // QT_CONFIG(whatsthis)
        self.menuObjectChecker_Ver_0_01.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

