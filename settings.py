# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sett.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mico

class Ui_Settings(object):
    def setupUi(self, Settings):
        self.db = VbagKur()
        Settings.setObjectName("Settings")
        Settings.resize(578, 220)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/application-default-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Settings)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Settings)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Settings)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Settings)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Settings)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 411, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Settings)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 141, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Settings)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 70, 411, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Settings)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 100, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit.setReadOnly(True)
        self.veritabani_bilgisi_cek()

        self.retranslateUi(Settings)
        self.pushButton.clicked.connect(self.dosya_kayit_yeri)
        self.pushButton_2.clicked.connect(self.bilgi_guncelle)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Ayarlar"))
        self.label.setText(_translate("Settings", "Uzlaştırma Dosya Kayıt Yeri"))
        self.pushButton.setText(_translate("Settings", "Seç"))
        self.label_2.setText(_translate("Settings", "Dosya Teslim Süresi"))
        self.label_3.setText(_translate("Settings", "Dosya Uzatma Süresi"))
        self.pushButton_2.setText(_translate("Settings", "Güncelle"))

    def veritabani_bilgisi_cek(self):
        sql_yer = "select * from ayarlar"
        sonuc = self.db.komut(sql_yer)
        self.lineEdit.setText(sonuc[0][2])
        self.lineEdit_2.setText(sonuc[0][0])
        self.lineEdit_3.setText(sonuc[0][1])

    def dosya_kayit_yeri(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory()
        if directory:
            self.lineEdit.setText(directory)

    def bilgi_guncelle(self):
        yer = self.lineEdit.text()
        ts = self.lineEdit_2.text()
        us = self.lineEdit_3.text()
        sql = "update ayarlar set teslim_suresi = '{}'," \
              "uzatma_suresi = '{}'," \
              "kayit_yeri = '{}'".format(ts, us, yer)
        if self.db.yapistir(sql) == True:
            baslik = "Veritabanı Güncellendi"
            mesaj = "Yapılan değişiklikler veritabanına başarıyla kaydedildi"
            mico.bilgilendir(mesaj, baslik)
        else:
            baslik = "Veritabanı Bağlantı Hatası"
            mesaj = "Veritabanı bağlantı sorunu nedeniyle değişiklikler kaydedilemedi."
            mico.bilgilendir(mesaj, baslik)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

