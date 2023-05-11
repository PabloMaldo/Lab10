# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_test_designvLfcHt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(305, 307)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 10, 71, 23))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 10, 81, 22))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 171, 20))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 40, 71, 23))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 70, 261, 192))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 10, 71, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 305, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"COM0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"COM9", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"COM10", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
    # retranslateUi