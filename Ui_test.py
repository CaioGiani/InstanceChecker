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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QStatusBar,
    QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(908, 705)
        MainWindow.setAnimated(True)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setAutoRepeat(False)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ListInstance = QScrollArea(self.centralwidget)
        self.ListInstance.setObjectName(u"ListInstance")
        self.ListInstance.setGeometry(QRect(660, 20, 231, 441))
        self.ListInstance.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 229, 439))
        self.ListInstance.setWidget(self.scrollAreaWidgetContents)
        self.EditBotton = QPushButton(self.centralwidget)
        self.EditBotton.setObjectName(u"EditBotton")
        self.EditBotton.setGeometry(QRect(740, 640, 75, 23))
        self.AcceptBotton = QPushButton(self.centralwidget)
        self.AcceptBotton.setObjectName(u"AcceptBotton")
        self.AcceptBotton.setGeometry(QRect(660, 640, 75, 23))
        self.AbortBotton = QPushButton(self.centralwidget)
        self.AbortBotton.setObjectName(u"AbortBotton")
        self.AbortBotton.setGeometry(QRect(820, 640, 75, 23))
        self.InfoWidget = QTableView(self.centralwidget)
        self.InfoWidget.setObjectName(u"InfoWidget")
        self.InfoWidget.setGeometry(QRect(660, 580, 231, 51))
        self.InfoWidget.setAutoFillBackground(False)
        self.InfoWidget.setFrameShadow(QFrame.Plain)
        self.InfoWidget.setShowGrid(True)
        self.frameImage = QFrame(self.centralwidget)
        self.frameImage.setObjectName(u"frameImage")
        self.frameImage.setGeometry(QRect(10, 20, 640, 640))
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
        self.frameImage.setPalette(palette)
        self.frameImage.setFrameShape(QFrame.StyledPanel)
        self.frameImage.setFrameShadow(QFrame.Raised)
        self.horizontalScrollBar = QScrollBar(self.frameImage)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(0, 620, 641, 20))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.verticalScrollBar = QScrollBar(self.frameImage)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(620, 0, 21, 621))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.LabelViewCheck = QCheckBox(self.frameImage)
        self.LabelViewCheck.setObjectName(u"LabelViewCheck")
        self.LabelViewCheck.setEnabled(True)
        self.LabelViewCheck.setGeometry(QRect(10, 10, 70, 17))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 908, 21))
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
        self.EditBotton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.AcceptBotton.setText(QCoreApplication.translate("MainWindow", u"Accpet", None))
        self.AbortBotton.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.LabelViewCheck.setText(QCoreApplication.translate("MainWindow", u"View Labels", None))
        self.menuObjectChecker_Ver_0_01.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

