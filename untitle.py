# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from b1 import Ui_Uzlasma
from bilgirisi import Ui_Bilgi
from olay import Ui_olay

class Ui_MainWindow(Ui_Bilgi, Ui_Uzlasma,Ui_olay):
    def uekl(self):
        self.b1 = QtWidgets.QMainWindow()
        self.ui_b1 = Ui_Uzlasma()
        self.ui_b1.setupUi(self.b1)
        self.b1.show()

    def bilgigiris(self):
        self.bilgi_tavan = QtWidgets.QMainWindow()
        self.ui_bilgi = Ui_Bilgi()
        self.ui_bilgi.setupUi(self.bilgi_tavan)
        self.bilgi_tavan.show()

    def olay(self):
        self.olay_tavan = QtWidgets.QMainWindow()
        self.ui_ol = Ui_olay()
        self.ui_ol.setupUi(self.olay_tavan)
        self.olay_tavan.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 121, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon("lib/icon/uzlasma.png"))
        self.pushButton.setIconSize(QtCore.QSize(48,48))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 20, 121, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 20, 121, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 20, 121, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 140, 121, 101))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 140, 121, 101))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 140, 121, 101))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(450, 140, 121, 101))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.pushButton.clicked.connect(self.uekl)
        self.pushButton_2.clicked.connect(self.bilgigiris)
        self.pushButton_3.clicked.connect(self.olay)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uzlaş Bakalım"))
        self.pushButton.setText(_translate("MainWindow", "Uzlaşma Ekle"))
        self.pushButton_2.setText(_translate("MainWindow", "Kişi Bilgileri"))
        self.pushButton_3.setText(_translate("MainWindow", "Olay Ekle"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))

