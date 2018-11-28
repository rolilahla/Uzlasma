# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarafsticked.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
from modul import tek_satirlik_demet_coz
from mico import bilgilendir, guncelleme_soru

class Gider(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(Gider, self).__init__()
        self.db = VbagKur()

    def init_ui(self, dosya):
        self.dosya = dosya
        self.resize(241, 143)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(139, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.setWindowTitle("Dosya Gider Ekle")
        self.label.setText("Yapılan Harcama Adı")
        self.label_2.setText("Harcama Tutarı")
        self.pushButton.setText("Ekle")
        self.pushButton.clicked.connect(self.bilgi_topla)

    def bilgi_topla(self):
        harcama = self.lineEdit.text()
        tutar = self.lineEdit_2.text()
        if self.db.gider_ekle(harcama, tutar, self.dosya) == True:
            baslik = "Gider Ekleme"
            mesaj = self.dosya + " No'lu dosya gider bilgilerine " + harcama + " gideri " + tutar + " TL olarak eklendi "
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.on_changed_value(False)
        else:
            pass

    # Sinyali Gönder
    def on_changed_value(self, value):
        self.clicked.emit(value)



