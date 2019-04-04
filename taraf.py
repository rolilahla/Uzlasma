# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarafsticked.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
from mico import bilgilendir

class TarafEkle(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(TarafEkle, self).__init__()
        self.db = VbagKur()

    def init_ui(self, uno):
        self.dosya_uzlasma_no = uno
        self.setWindowTitle("Taraf Ekle")
        self.resize(272, 502)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 301, 21))
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

        self.lineEdit_28 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_28.setGeometry(QtCore.QRect(70, 40, 182, 20))
        self.lineEdit_28.setObjectName("lineEdit_28")

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
        self.comboBox_3.setGeometry(QtCore.QRect(100, 20, 150, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_45 = QtWidgets.QLabel(self.page_2)
        self.label_45.setGeometry(QtCore.QRect(0, 50, 90, 20))
        self.label_45.setObjectName("label_45")

        self.comboBox_11 = QtWidgets.QComboBox(self.page_2)
        self.comboBox_11.setGeometry(QtCore.QRect(100, 50, 150, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.label_46 = QtWidgets.QLabel(self.page_2)
        self.label_46.setGeometry(QtCore.QRect(0, 80, 90, 20))
        self.label_46.setObjectName("label_46")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_29.setGeometry(QtCore.QRect(100, 80, 150, 20))
        self.lineEdit_29.setText("")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.stackedWidget.addWidget(self.page_2)
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(0, 110, 90, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 110, 150, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(0, 140, 101, 20))
        self.label_22.setObjectName("label_22")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(100, 140, 150, 20))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(0, 170, 90, 20))
        self.label_14.setObjectName("label_14")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 170, 150, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(0, 200, 90, 20))
        self.label_21.setObjectName("label_21")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 200, 150, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")

        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(0, 230, 90, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 230, 150, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(0, 260, 90, 20))
        self.label_16.setObjectName("label_16")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_2.setGeometry(QtCore.QRect(101, 260, 150, 101))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 370, 75, 23))
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
        self.lineEdit_11.setObjectName("lineEdit_11")

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



        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(0, 110, 90, 20))
        self.label_19.setObjectName("label_19")

        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.radioButton.clicked.connect(self.sahis)
        self.radioButton_2.clicked.connect(self.vekil)
        self.radioButton_3.clicked.connect(self.tercuman)
        self.pushButton.clicked.connect(self.sahis_ekle)
        self.pushButton_2.clicked.connect(self.vekil_ekle)
        self.pushButton_3.clicked.connect(self.tercuman_ekle)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        self.radioButton_2.setText(_translate("Dialog", "Vekil"))
        self.radioButton.setText(_translate("Dialog", "Şahıs"))
        self.radioButton_3.setText(_translate("Dialog", "Tercüman"))
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
        self.label_14.setText(_translate("Dialog", "T.C No"))
        self.label_16.setText(_translate("Dialog", "Adres"))
        self.label_13.setText(_translate("Dialog", "Kayıtlı Olduğu Baro"))
        self.pushButton_2.setText(_translate("Dialog", "Ekle"))
        self.label_11.setText(_translate("Dialog", "Temsil ettiği"))
        self.label_17.setText(_translate("Dialog", "Ad Soyad"))
        self.label_18.setText(_translate("Dialog", "TC No"))
        self.label_19.setText(_translate("Dialog", "Adres"))
        self.pushButton_3.setText(_translate("Dialog", "Ekle"))
        self.label_21.setText(_translate("Dialog", "Teklif Tarihi"))
        self.label_22.setText(_translate("Dialog", " Sicil No"))
        self.label_45.setText(_translate("Dialog", "Durum"))
        self.comboBox_11.setItemText(0, _translate("Dialog", "Durum Seç"))
        self.comboBox_11.setItemText(1, _translate("Dialog", "Müdafi"))
        self.comboBox_11.setItemText(2, _translate("Dialog", "Vekil"))
        self.label_46.setText(_translate("Dialog", "Ad Soyad"))

    def sahis(self):
        self.stackedWidget.setCurrentIndex(0)

    def vekil(self):
        self.stackedWidget.setCurrentIndex(1)
        self.comboBox_3.clear()
        sonuc = self.db.komut("select ad from taraflar where dosya = '{}'".format(self.dosya_uzlasma_no))
        if sonuc == []:
            self.pushButton_2.setDisabled(True)
            baslik = "İlişkilendirme Hatası"
            mesaj = "Dosya'ya Kanuni Temsilci eklemeden önce tarafları ekleyin." \
                    "Savunulacak bir şey olmazsa avukat olmanın gereği kalmaz"
            bilgilendir(mesaj, baslik)
            self.sahis()
            self.radioButton.setChecked(True)
        else:
            for i in range(len(sonuc)):
                self.comboBox_3.addItem(sonuc[i][0])

    def tercuman(self):
        self.comboBox_4.clear()
        self.stackedWidget.setCurrentIndex(2)
        sonuc = self.db.komut("select ad from taraflar where dosya = '{}'".format(self.dosya_uzlasma_no))
        if sonuc == []:
            self.pushButton_3.setDisabled(True)
            baslik = "İlişkilendirme Hatası"
            mesaj = "Dosya'ya Tercüman eklemeden önce tarafları ekleyin."
            bilgilendir(mesaj, baslik)
            self.sahis()
            self.radioButton.setChecked(True)
        else:
            for i in range(len(sonuc)):
                self.comboBox_4.addItem(sonuc[i][0])

    def sahis_ekle(self):
        ad = self.lineEdit.text()
        ttarihi = self.lineEdit_28.text()
        sifat = self.comboBox.currentIndex()
        tc = self.lineEdit_2.text()
        baba = self.lineEdit_3.text()
        ana = self.lineEdit_4.text()
        dyer = self.lineEdit_5.text()
        dtar = self.lineEdit_6.text()
        cins = self.comboBox_2.currentText()
        tel = self.lineEdit_7.text()
        adresniteligi = self.comboBox_5.currentIndex()
        adres = self.textEdit.toPlainText()

        #Veritabanına Gönder
        if self.db.tarafekle(ad, ttarihi, sifat, tc, baba, ana, dyer, dtar, cins, tel, adresniteligi, adres, self.dosya_uzlasma_no) == True:
            baslik = "Dosya Bilgileri Eklendi"
            mesaj = ad + " isimli kişinin bilgileri veritabanına eklendi."
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_28.clear()
            self.textEdit.clear()
            self.comboBox.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)
            self.on_changed_value(False)
        else:
            baslik = "Veritabanı Yazma Sorunu"
            mesaj = "Hatanın giderilmesi için ivedilikle, Mehmet Eroğlu ile görüşüp kendisine 2 bira ısmarlayınız.(Not: Tuborg Gold Şişe, mümkünse soğuk)"
            bilgilendir(mesaj, baslik)

    def vekil_ekle(self):
        vekalet = self.comboBox_3.currentText()
        nitelik = self.comboBox_11.currentText()
        ad = self.lineEdit_29.text()
        baro = self.lineEdit_8.text()
        sicil = self.lineEdit_14.text()
        tc = self.lineEdit_9.text()
        ttarihi = self.lineEdit_13.text()
        telefon = self.lineEdit_10.text()
        adres = self.textEdit_2.toPlainText()
        sifat = nitelik

        # Veritabanına Gönder
        if self.db.temsilci_ekle(ttarihi,ad, sicil, telefon, adres, self.dosya_uzlasma_no, vekalet, sifat, nitelik, baro, tc) == True:
            baslik = "Temsilci Bilgileri Eklendi"
            mesaj = ad + " isimli kişinin bilgileri" + vekalet + " kişisinin kanuni temsilcisiolarak  veritabanına eklendi."
            bilgilendir(mesaj, baslik)
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_11.setCurrentIndex(0)
            self.lineEdit_29.clear()
            self.lineEdit_13.clear()
            self.lineEdit_14.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.textEdit_2.clear()
            self.on_changed_value(False)
        else:
            baslik = "Veritabanı Yazma Sorunu"
            mesaj = "Hatanın giderilmesi için ivedilikle, Mehmet Eroğlu ile görüşüp kendisine 2 bira ısmarlayınız.(Not: Tuborg Gold Şişe, mümkünse soğuk)"
            bilgilendir(mesaj, baslik)

    def tercuman_ekle(self):
        vekalet = self.comboBox_4.currentText()
        ad = self.lineEdit_11.text()
        tc = self.lineEdit_12.text()
        adres = self.textEdit_3.toPlainText()
        sifat = "Tercüman"

        # Veritabanına Gönder
        if self.db.tercuman_ekle(ad, tc, adres, self.dosya_uzlasma_no, vekalet, sifat) == True:
            baslik = "Temsilci Bilgileri Eklendi"
            mesaj = ad + " isimli kişinin bilgileri " + vekalet + " kişisinin tercümanı " \
                                                                  "olarak  veritabanına eklendi."
            bilgilendir(mesaj, baslik)
            self.comboBox_4.setCurrentIndex(0)
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.textEdit_3.clear()
            self.on_changed_value(False)
        else:
            baslik = "Veritabanı Yazma Sorunu"
            mesaj = "Hatanın giderilmesi için ivedilikle, Mehmet Eroğlu ile görüşüp kendisine 2 bira ısmarlayınız." \
                    "(Not: Tuborg Gold Şişe, mümkünse soğuk)"
            bilgilendir(mesaj, baslik)

    #Sinyali Gönder
    def on_changed_value(self, value):
        self.clicked.emit(value)