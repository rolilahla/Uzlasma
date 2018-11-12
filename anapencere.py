# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from b1 import Ui_Uzlasma
from vtbgln import VbagKur
from bilgirisi import Ui_Bilgi

class Ui_MainWindow(object):
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


    def setupUi(self, MainWindow):
        self.db = VbagKur()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(70, 10, 101, 20))
        self.comboBox.setObjectName("comboBox")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 211, 121))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 10, 201, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya_Ekle = QtWidgets.QMenu(self.menubar)
        self.menuDosya_Ekle.setObjectName("menuDosya_Ekle")
        self.menuUzla_mac_Ekle = QtWidgets.QMenu(self.menubar)
        self.menuUzla_mac_Ekle.setObjectName("menuUzla_mac_Ekle")
        self.menu_ablonlar = QtWidgets.QMenu(self.menubar)
        self.menu_ablonlar.setObjectName("menu_ablonlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDosya_Ekle = QtWidgets.QAction(MainWindow)
        self.actionDosya_Ekle.setObjectName("actionDosya_Ekle")
        self.actionUzla_mac_Bilgisi_ekle = QtWidgets.QAction(MainWindow)
        self.actionUzla_mac_Bilgisi_ekle.setObjectName("actionUzla_mac_Bilgisi_ekle")
        self.action_ablonlar_d_zenle = QtWidgets.QAction(MainWindow)
        self.action_ablonlar_d_zenle.setObjectName("action_ablonlar_d_zenle")
        self.menuDosya_Ekle.addAction(self.actionDosya_Ekle)
        self.menuUzla_mac_Ekle.addAction(self.actionUzla_mac_Bilgisi_ekle)
        self.menu_ablonlar.addAction(self.action_ablonlar_d_zenle)
        self.menubar.addAction(self.menuDosya_Ekle.menuAction())
        self.menubar.addAction(self.menuUzla_mac_Ekle.menuAction())
        self.menubar.addAction(self.menu_ablonlar.menuAction())

        self.actionDosya_Ekle.triggered.connect(self.uekl)
        self.dosya_tara()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dosya_tara(self):
        sor = self.db.sorgu_no_bul()
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i][0])

    def taraf_bilgisi_duzenle(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dosya No"))
        self.groupBox.setTitle(_translate("MainWindow", "Taraflar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dosya Bilgileri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dosya Bilgileri"))
        self.menuDosya_Ekle.setTitle(_translate("MainWindow", "Dosya Ekle"))
        self.menuUzla_mac_Ekle.setTitle(_translate("MainWindow", "Uzlaşmacı Ekle"))
        self.menu_ablonlar.setTitle(_translate("MainWindow", "Şablonlar"))
        self.actionDosya_Ekle.setText(_translate("MainWindow", "Dosya Ekle"))
        self.actionUzla_mac_Bilgisi_ekle.setText(_translate("MainWindow", "Uzlaşmacı Bilgisi ekle"))
        self.action_ablonlar_d_zenle.setText(_translate("MainWindow", "Şablonları düzenle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

