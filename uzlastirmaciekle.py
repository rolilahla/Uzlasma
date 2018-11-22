# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uzlastirmaciekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
from mico import bilgilendir

class Ui_UzlastirmaciEkle(object):
    def setupUi(self, UzlastirmaciEkle):
        self.db = VbagKur()

        UzlastirmaciEkle.setObjectName("UzlastirmaciEkle")
        UzlastirmaciEkle.resize(441, 257)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/icon/credentials-preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UzlastirmaciEkle.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label.setGeometry(QtCore.QRect(160, 10, 90, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(UzlastirmaciEkle)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(UzlastirmaciEkle)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 40, 211, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 90, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(UzlastirmaciEkle)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 70, 211, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(UzlastirmaciEkle)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 100, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label_4.setGeometry(QtCore.QRect(160, 100, 90, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label_5.setGeometry(QtCore.QRect(160, 130, 90, 20))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(UzlastirmaciEkle)
        self.textEdit.setGeometry(QtCore.QRect(220, 130, 211, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(UzlastirmaciEkle)
        self.pushButton.setGeometry(QtCore.QRect(360, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(UzlastirmaciEkle)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 121, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("lib/icon/credentials-preferences.png"))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(UzlastirmaciEkle)
        self.pushButton.clicked.connect(self.uz_ekle)
        QtCore.QMetaObject.connectSlotsByName(UzlastirmaciEkle)

    def uz_ekle(self):
        ad = self.lineEdit.text()
        sicil = self.lineEdit_2.text()
        telefon = self.lineEdit_3.text()
        sehir = self.lineEdit_4.text()
        adres = self.textEdit.toPlainText()

        #bilgileri veritabbanına gönder
        if self.db.uzlastirmaci_ekle(ad, sicil, telefon, sehir, adres) == True:
            baslik = "Uzlaştırmacı Eklendi"
            mesaj = ad + " İsimli uzlaştırmacı veritabanına başarıyla eklendi"
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.textEdit.clear()
        else:
            baslik = "Uzlaştırmacı Ekleme Hatası"
            mesaj = ad +" İsimli uzlaştırmacı veritabanına eklenemedi"
            bilgilendir(mesaj, baslik)


    def retranslateUi(self, UzlastirmaciEkle):
        _translate = QtCore.QCoreApplication.translate
        UzlastirmaciEkle.setWindowTitle(_translate("UzlastirmaciEkle", "Uzlaştırmacı Ekle"))
        self.label.setText(_translate("UzlastirmaciEkle", "Ad Soyad"))
        self.label_2.setText(_translate("UzlastirmaciEkle", "Sicil No"))
        self.label_3.setText(_translate("UzlastirmaciEkle", "Telefon"))
        self.label_4.setText(_translate("UzlastirmaciEkle", "Şehir"))
        self.label_5.setText(_translate("UzlastirmaciEkle", "Adres"))
        self.textEdit.setHtml(_translate("UzlastirmaciEkle", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("UzlastirmaciEkle", "Kaydet"))

