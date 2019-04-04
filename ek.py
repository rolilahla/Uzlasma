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

class Ekler(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(Ekler, self).__init__()
        self.db = VbagKur()

    def init_ui(self, dosya):
        self.dosya = dosya
        self.resize(241, 103)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(139, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        self.setWindowTitle("Dosya Ekle")
        self.label.setText("Eklenecek Dosya Adı")
        self.pushButton.setText("Ekle")
        self.pushButton.clicked.connect(self.bilgi_topla)

    def bilgi_topla(self):
        dosya_adi = self.lineEdit.text()
        if dosya_adi == "":
            baslik = "Dosya Eki Ekleme Hatası"
            mesaj = "Dosya Ek'i eklemek için boş alanların tamamını doldurmalısınız"
            bilgilendir(mesaj, baslik)
        else:
            if self.db.ek_ekle(dosya_adi, self.dosya) == True:
                baslik = "Dosya Ekleme"
                mesaj = self.dosya + " No'lu soruşturmanın Ek Dosya bilgilerine " + dosya_adi + " dosyası eklendi "
                bilgilendir(mesaj, baslik)
                self.lineEdit.clear()
                self.on_changed_value(False)
            else:
                baslik = "Ek Ekleme Hatası"
                mesaj = "Veritabanı probleminden kaynaklı veri eklenemedi"
                bilgilendir(mesaj, baslik)

    # Sinyali Gönder
    def on_changed_value(self, value):
        self.clicked.emit(value)



