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

class TarafDuzenle(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)
    def __init__(self):
        super(TarafDuzenle, self).__init__()
        self.db = VbagKur()

    def init_ui(self, uno, kisi, nitelik):
        self.setWindowTitle("Taraf Düzenle")
        self.resize(272, 502)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 1, 1, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.radioButton_3.setObjectName("radioButton_3")

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 40, 261, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 10, 90, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 182, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(0, 40, 90, 20))
        self.label_21.setObjectName("label_21")
        self.label_21.setText("Teklif Tarihi")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_13.setGeometry(QtCore.QRect(70, 40, 182, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 90, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(70, 70, 182, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 100, 182, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 130, 90, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 130, 182, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 90, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 160, 182, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(0, 190, 90, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 190, 182, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setGeometry(QtCore.QRect(0, 220, 90, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 220, 182, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(0, 250, 90, 20))
        self.label_12.setObjectName("label_12")
        self.comboBox_2 = QtWidgets.QComboBox(self.page)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 250, 182, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(0, 280, 90, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 280, 182, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(0, 310, 90, 20))
        self.label_20.setObjectName("label_20")
        self.comboBox_5 = QtWidgets.QComboBox(self.page)
        self.comboBox_5.setGeometry(QtCore.QRect(70, 310, 182, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")

        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(0, 340, 90, 20))
        self.label_9.setObjectName("label_9")

        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(70, 340, 181, 91))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(180, 435, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 90, 20))
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 20, 182, 22))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(0, 50, 90, 20))
        self.label_22.setObjectName("label_22")
        self.label_22.setText("Teklif Tarihi")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(70, 50, 182, 20))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")

        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(0, 80, 90, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 80, 182, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(0, 110, 90, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(70, 110, 182, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(0, 140, 90, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 140, 182, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")

        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(0, 170, 90, 20))
        self.label_16.setObjectName("label_16")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 170, 182, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 280, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        self.comboBox_4 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 20, 182, 22))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(0, 20, 90, 20))
        self.label_11.setObjectName("label_11")

        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(70, 50, 182, 20))
        self.lineEdit_11.setText("")

        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(70, 80, 182, 20))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")

        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(0, 50, 90, 20))
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setGeometry(QtCore.QRect(0, 80, 90, 20))
        self.label_18.setObjectName("label_18")

        self.textEdit_3 = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_3.setGeometry(QtCore.QRect(70, 110, 182, 71))
        self.textEdit_3.setObjectName("textEdit_3")


        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(0, 110, 90, 20))
        self.label_19.setObjectName("label_19")

        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)


        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.sahis_guncelle)
        self.pushButton_2.clicked.connect(self.vekil_guncelle)
        self.pushButton_3.clicked.connect(self.tercuman_guncelle)
        QtCore.QMetaObject.connectSlotsByName(self)

        if nitelik == "Şahıs":
            self.radioButton.setChecked(True)
            self.radioButton_2.setDisabled(True)
            self.radioButton_3.setDisabled(True)
            self.stackedWidget.setCurrentIndex(0)
            sql = "select * from taraflar where dosya = '{}' and ad = '{}'".format(uno, kisi)
            self.bilgi_cek(sql)
        elif nitelik == "Vekil":
            self.radioButton_2.setChecked(True)
            self.radioButton.setDisabled(True)
            self.radioButton_3.setDisabled(True)
            self.stackedWidget.setCurrentIndex(1)
            sql = "select * from temsilciler where dosya = '{}' and ad = '{}'".format(uno, kisi)

            sonuc = self.db.komut("select ad from taraflar where dosya = '{}'".format(uno))
            for i in range(len(sonuc)):
                self.comboBox_3.addItem(sonuc[i][0])
            self.bilgi_cek(sql)
        else:
            self.radioButton_3.setChecked(True)
            self.radioButton.setDisabled(True)
            self.radioButton_2.setDisabled(True)
            self.stackedWidget.setCurrentIndex(2)
            sonuc = self.db.komut("select ad from taraflar where dosya = '{}'".format(uno))
            for i in range(len(sonuc)):
                self.comboBox_4.addItem(sonuc[i][0])
            sql = "select * from tercuman where dosya = '{}' and ad = '{}'".format(uno, kisi)
            self.bilgi_cek(sql)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.radioButton_2.setText(_translate("Dialog", "Vekil"))
        self.radioButton.setText(_translate("Dialog", "Şahıs"))
        self.radioButton_3.setText(_translate("Dialog", "Tarcüman"))
        self.label.setText(_translate("Dialog", "Ad Soyad"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Cinsiyet"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Kadın"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Erkek"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Normal Tc Adresi"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "Göstermelik Tc Adresi"))
        self.comboBox_5.setItemText(2, _translate("Dialog", "Yabancı Ülke Adresi"))
        self.label_20.setText(_translate("Dialog", "Adres Türü"))
        self.label_9.setText(_translate("Dialog", "Adres"))
        self.label_7.setText(_translate("Dialog", "Doğum Tarihi"))
        self.label_3.setText(_translate("Dialog", "TC No"))
        self.label_5.setText(_translate("Dialog", "Anne Adı"))
        self.label_4.setText(_translate("Dialog", "Baba Adı"))
        self.label_12.setText(_translate("Dialog", "Cinsiyet"))
        self.label_6.setText(_translate("Dialog", "Doğum Yeri"))
        self.label_2.setText(_translate("Dialog", "Taraf"))
        self.label_8.setText(_translate("Dialog", "Telefon"))
        self.comboBox.setItemText(0, _translate("Dialog", "Taraf Seç"))
        self.comboBox.setItemText(1, _translate("Dialog", "Mağdur / Katılan"))
        self.comboBox.setItemText(2, _translate("Dialog", "Mağdur/Katılan\'ın Kanuni Temsilcisi"))
        self.comboBox.setItemText(3, _translate("Dialog", "Suçtan Zarar Gören"))
        self.comboBox.setItemText(4, _translate("Dialog", "Suçtan Zarar Görenin Kanuni Temsilcisi"))
        self.comboBox.setItemText(5, _translate("Dialog", "Şüpheli / Sanık"))
        self.comboBox.setItemText(6, _translate("Dialog", "Şüpheli Sanığın Kanuni Temsilcisi"))
        self.comboBox.setItemText(7, _translate("Dialog", "Müşteki Şüpheli"))
        self.comboBox.setItemText(8, _translate("Dialog", "Müşteki Şüphelinin Kanuni Temsilcisi"))
        self.pushButton.setText(_translate("Dialog", "Ekle"))
        self.label_10.setText(_translate("Dialog", "Temsil ettiği"))
        self.label_15.setText(_translate("Dialog", "Telefon"))
        self.label_14.setText(_translate("Dialog", "Sicil No"))
        self.label_16.setText(_translate("Dialog", "Adres"))
        self.label_13.setText(_translate("Dialog", "Ad Soyad"))
        self.pushButton_2.setText(_translate("Dialog", "Ekle"))
        self.label_11.setText(_translate("Dialog", "Temsil ettiği"))
        self.label_17.setText(_translate("Dialog", "Ad Soyad"))
        self.label_18.setText(_translate("Dialog", "TC No"))
        self.label_19.setText(_translate("Dialog", "Adres"))
        self.pushButton_3.setText(_translate("Dialog", "Ekle"))

    def bilgi_cek(self, sql):
        sonuc = tek_satirlik_demet_coz(self.db.komut(sql))
        self.veri_doldur(sonuc)

    def veri_doldur(self, bilgi):
        if len(bilgi) == 14:
            self.sahis_id_no = bilgi[0]
            self.lineEdit.setText(bilgi[1])
            self.lineEdit_13.setText(bilgi[2])
            self.comboBox.setCurrentIndex(bilgi[3])
            self.lineEdit_2.setText(bilgi[4])
            self.lineEdit_3.setText(bilgi[5])
            self.lineEdit_4.setText(bilgi[6])
            self.lineEdit_5.setText(bilgi[7])
            self.lineEdit_6.setText(bilgi[8])
            self.comboBox_2.setCurrentText(bilgi[9])
            self.lineEdit_7.setText(bilgi[10])
            self.comboBox_5.setCurrentIndex(bilgi[11])
            self.textEdit.setPlainText(bilgi[12])

        elif len(bilgi) == 9:
            self.vekil_id_no = bilgi[0]
            self.lineEdit_14.setText(bilgi[1])
            self.lineEdit_8.setText(bilgi[2])
            self.lineEdit_9.setText(bilgi[3])
            self.lineEdit_10.setText(bilgi[4])
            self.textEdit_2.setPlainText(bilgi[5])
            self.comboBox_3.setCurrentText(bilgi[7])

        elif len(bilgi) == 7:
            self.tercuman_id_no = bilgi[0]
            self.comboBox_4.setCurrentText(bilgi[5])
            self.lineEdit_11.setText(bilgi[1])
            self.lineEdit_12.setText(bilgi[2])
            self.textEdit_3.setPlainText(bilgi[3])

    def sahis_guncelle(self):
        l = []
        l.append(self.lineEdit.text())
        l.append(self.lineEdit_13.text())
        l.append(self.comboBox.currentText())
        l.append(self.lineEdit_2.text())
        l.append(self.lineEdit_3.text())
        l.append(self.lineEdit_4.text())
        l.append(self.lineEdit_5.text())
        l.append(self.lineEdit_6.text())
        l.append(self.comboBox_2.currentText())
        l.append(self.lineEdit_7.text())
        l.append(self.comboBox_5.currentIndex())
        l.append(self.textEdit.toPlainText())
        l.append(self.sahis_id_no)

        if guncelleme_soru(l[0]) == True:
            # Veritabanına Gönder
            if self.db.sahis_guncelle(l) == True:
                baslik = "Bilgi Güncelleme "
                mesaj = l[0] + " isimli kişinin bilgileri güncellendi"
                bilgilendir(mesaj, baslik)
                self.lineEdit.clear()
                self.lineEdit_13.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.lineEdit_7.clear()
                self.textEdit.clear()
                self.comboBox.setCurrentIndex(0)
                self.comboBox_2.setCurrentIndex(0)
                self.comboBox_5.setCurrentIndex(0)
                self.on_changed_value(False)
            else:
               pass
        else:
            pass

    def vekil_guncelle(self):
        v = []
        v.append(self.lineEdit_14.text())
        v.append(self.lineEdit_8.text())
        v.append(self.lineEdit_9.text())
        v.append(self.lineEdit_10.text())
        v.append(self.textEdit_2.toPlainText())
        v.append(self.comboBox_3.currentText())
        v.append(self.vekil_id_no)

        # Veritabanına Gönder
        if guncelleme_soru(v[1]) == True:
            # Veritabanına Gönder
            if self.db.vekil_guncelle(v) == True:
                baslik = "Bilgi Güncelleme "
                mesaj = v[1] + " isimli kişinin bilgileri güncellendi"
                bilgilendir(mesaj, baslik)
                self.lineEdit_14.clear()
                self.lineEdit_8.clear()
                self.lineEdit_9.clear()
                self.lineEdit_10.clear()
                self.textEdit_2.clear()
                self.comboBox_3.setCurrentIndex(0)
                self.on_changed_value(False)
            else:
                pass
        else:
            pass

    def tercuman_guncelle(self):
        t = []
        t.append(self.lineEdit_11.text())
        t.append(self.lineEdit_12.text())
        t.append(self.textEdit_3.toPlainText())
        t.append(self.comboBox_4.currentText())
        t.append(self.tercuman_id_no)

        # Veritabanına Gönder
        if guncelleme_soru(t[0]) == True:
            # Veritabanına Gönder
            if self.db.tercuman_guncelle(t) == True:
                baslik = "Bilgi Güncelleme "
                mesaj = t[0] + " isimli kişinin bilgileri güncellendi"
                bilgilendir(mesaj, baslik)
                self.lineEdit_11.clear()
                self.lineEdit_12.clear()
                self.textEdit_3.clear()
                self.comboBox_4.setCurrentIndex(0)
                self.on_changed_value(False)
            else:
                pass
        else:
            pass

    # Sinyali Gönder
    def on_changed_value(self, value):
        self.clicked.emit(value)



