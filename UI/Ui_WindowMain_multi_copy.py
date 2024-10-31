# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowMain_multi_copy.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1298, 891)
        MainWindow.setAnimated(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setAutoRepeat(False)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUser_Manual = QAction(MainWindow)
        self.actionUser_Manual.setObjectName(u"actionUser_Manual")
        self.actionMap_annotation = QAction(MainWindow)
        self.actionMap_annotation.setObjectName(u"actionMap_annotation")
        self.actionCategory = QAction(MainWindow)
        self.actionCategory.setObjectName(u"actionCategory")
        self.actionNormal_box = QAction(MainWindow)
        self.actionNormal_box.setObjectName(u"actionNormal_box")
        self.actionNormal_box.setCheckable(True)
        self.actionNormal_box.setChecked(False)
        self.actionOriented_box = QAction(MainWindow)
        self.actionOriented_box.setObjectName(u"actionOriented_box")
        self.actionOriented_box.setCheckable(True)
        self.actionEllipse = QAction(MainWindow)
        self.actionEllipse.setObjectName(u"actionEllipse")
        self.actionEllipse.setCheckable(True)
        self.action4_side_polygon = QAction(MainWindow)
        self.action4_side_polygon.setObjectName(u"action4_side_polygon")
        self.action4_side_polygon.setCheckable(True)
        self.actionMulti_side_polygon = QAction(MainWindow)
        self.actionMulti_side_polygon.setObjectName(u"actionMulti_side_polygon")
        self.actionMulti_side_polygon.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonAccept = QPushButton(self.centralwidget)
        self.pushButtonAccept.setObjectName(u"pushButtonAccept")
        self.pushButtonAccept.setGeometry(QRect(1060, 529, 111, 23))
        self.pushButtonAbort = QPushButton(self.centralwidget)
        self.pushButtonAbort.setObjectName(u"pushButtonAbort")
        self.pushButtonAbort.setGeometry(QRect(1180, 529, 111, 23))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(1060, 69, 231, 451))
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.pushButtonAnnotation = QPushButton(self.centralwidget)
        self.pushButtonAnnotation.setObjectName(u"pushButtonAnnotation")
        self.pushButtonAnnotation.setGeometry(QRect(1060, 10, 231, 24))
        self.pushButtonPrevious = QPushButton(self.centralwidget)
        self.pushButtonPrevious.setObjectName(u"pushButtonPrevious")
        self.pushButtonPrevious.setGeometry(QRect(1060, 40, 111, 24))
        self.pushButtonNext = QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setGeometry(QRect(1180, 40, 111, 24))
        self.plainTextEditLog = QPlainTextEdit(self.centralwidget)
        self.plainTextEditLog.setObjectName(u"plainTextEditLog")
        self.plainTextEditLog.setGeometry(QRect(1060, 560, 231, 281))
        self.plainTextEditLog.setStyleSheet(u"background: transparent")
        self.plainTextEditLog.setFrameShape(QFrame.NoFrame)
        self.plainTextEditLog.setFrameShadow(QFrame.Plain)
        self.plainTextEditLog.setLineWidth(0)
        self.plainTextEditLog.setReadOnly(True)
        self.pushButtonAddInstance = QPushButton(self.centralwidget)
        self.pushButtonAddInstance.setObjectName(u"pushButtonAddInstance")
        self.pushButtonAddInstance.setGeometry(QRect(1070, 490, 101, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(True)
        self.pushButtonAddInstance.setFont(font)
        self.pushButtonAddInstance.setText(u"Add")
        self.pushButtonRemoveInstance = QPushButton(self.centralwidget)
        self.pushButtonRemoveInstance.setObjectName(u"pushButtonRemoveInstance")
        self.pushButtonRemoveInstance.setGeometry(QRect(1180, 490, 101, 20))
        self.pushButtonRemoveInstance.setFont(font)
        self.pushButtonRemoveInstance.setText(u"Remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1298, 22))
        self.menuObjectChecker_Ver_0_01 = QMenu(self.menubar)
        self.menuObjectChecker_Ver_0_01.setObjectName(u"menuObjectChecker_Ver_0_01")
        self.menuProject_Setting = QMenu(self.menuObjectChecker_Ver_0_01)
        self.menuProject_Setting.setObjectName(u"menuProject_Setting")
        self.menuAnnotation_Shape = QMenu(self.menuProject_Setting)
        self.menuAnnotation_Shape.setObjectName(u"menuAnnotation_Shape")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuObjectChecker_Ver_0_01.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuObjectChecker_Ver_0_01.addAction(self.actionOpen)
        self.menuObjectChecker_Ver_0_01.addAction(self.menuProject_Setting.menuAction())
        self.menuObjectChecker_Ver_0_01.addAction(self.actionQuit)
        self.menuProject_Setting.addAction(self.actionCategory)
        self.menuProject_Setting.addAction(self.menuAnnotation_Shape.menuAction())
        self.menuAnnotation_Shape.addAction(self.actionNormal_box)
        self.menuAnnotation_Shape.addAction(self.actionOriented_box)
        self.menuAnnotation_Shape.addAction(self.actionEllipse)
        self.menuAnnotation_Shape.addAction(self.action4_side_polygon)
        self.menuAnnotation_Shape.addAction(self.actionMulti_side_polygon)
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menuEdit.addAction(self.actionMap_annotation)

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
        self.actionMap_annotation.setText(QCoreApplication.translate("MainWindow", u"Map annotation", None))
        self.actionCategory.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.actionNormal_box.setText(QCoreApplication.translate("MainWindow", u"Normal box", None))
        self.actionOriented_box.setText(QCoreApplication.translate("MainWindow", u"Oriented box", None))
        self.actionEllipse.setText(QCoreApplication.translate("MainWindow", u"Ellipse", None))
        self.action4_side_polygon.setText(QCoreApplication.translate("MainWindow", u"4-side polygon", None))
        self.actionMulti_side_polygon.setText(QCoreApplication.translate("MainWindow", u"Multi-side polygon", None))
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
#if QT_CONFIG(tooltip)
        self.pushButtonRemoveInstance.setToolTip(QCoreApplication.translate("MainWindow", u"Add annotation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButtonRemoveInstance.setWhatsThis(QCoreApplication.translate("MainWindow", u"add annotation", None))
#endif // QT_CONFIG(whatsthis)
        self.menuObjectChecker_Ver_0_01.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProject_Setting.setTitle(QCoreApplication.translate("MainWindow", u"Project Setting", None))
        self.menuAnnotation_Shape.setTitle(QCoreApplication.translate("MainWindow", u"Annotation Shape", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

