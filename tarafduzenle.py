# -*- coding:utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from vtbgln import VbagKur
from mico import bilgilendir

class TarafDuzenle(QtWidgets.QDialog):
    # Added a signal
    clicked = pyqtSignal(bool)

    def __init__(self):
        super(TarafDuzenle, self).__init__()

    def init_ui(self, uno, kisi):
        self.dosya_uzlasma_no = uno
        self.resize(277, 475)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("lib/icon/stock_people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 90, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 182, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 90, 20))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(80, 40, 182, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 182, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 90, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 100, 182, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 90, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 130, 182, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 160, 182, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 90, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 90, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 190, 182, 20))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        #cinsiyet
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 220, 182, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 250, 182, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(10, 280, 90, 20))
        self.label_20.setObjectName("label_20")
        self.label_20.setText("Adres Niteliği")

        self.comboBox_3 = QtWidgets.QComboBox(self)
        self.comboBox_3.setGeometry(QtCore.QRect(80, 280, 182, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("TC İkamet Adresi")
        self.comboBox_3.addItem("Yabancı ülkede Oturup Tc Adresi")
        self.comboBox_3.addItem("Yabancı Ülkedeki Adresi")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 90, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 90, 20))
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(80, 310, 181, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 90, 20))
        self.label_10.setObjectName("label_10")

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(100, 410, 70, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 410, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(10, 430, 90, 20))
        self.label_11.setObjectName("label_11")

        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 430, 70, 17))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setGeometry(QtCore.QRect(190, 430, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 450, 75, 23))
        self.pushButton.setObjectName("pushButton")


        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(270, 0, 16, 441))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(280, 10, 281, 431))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 271, 171))
        self.groupBox.setObjectName("groupBox")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 20, 182, 20))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(70, 50, 182, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 80, 182, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(10, 110, 90, 20))
        self.label_16.setObjectName("label_16")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(70, 110, 182, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 190, 271, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_17.setObjectName("label_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(70, 20, 182, 20))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(70, 50, 182, 20))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_19.setObjectName("label_19")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_3.setGeometry(QtCore.QRect(70, 80, 182, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(10, 220, 90, 20))
        self.label_12.setObjectName("label_12")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TarafEkle", "Taraf Ekle"))
        self.label.setText(_translate("TarafEkle", "Ad Soyad"))
        self.label_2.setText(_translate("TarafEkle", "Taraf"))
        self.comboBox.setItemText(0, _translate("TarafEkle", "Taraf Seç"))
        self.comboBox.setItemText(1, _translate("TarafEkle", "Mağdur / Katılan"))
        self.comboBox.setItemText(2, _translate("TarafEkle", "Suçtan Zarar Gören"))
        self.comboBox.setItemText(3, _translate("TarafEkle", "Şüpheli / Sanık"))
        self.comboBox.setItemText(4, _translate("TarafEkle", "Müşteki Şüpheli"))
        self.label_3.setText(_translate("TarafEkle", "TC No"))
        self.label_4.setText(_translate("TarafEkle", "Baba Adı"))
        self.label_5.setText(_translate("TarafEkle", "Anne Adı"))
        self.label_6.setText(_translate("TarafEkle", "Doğum Yeri"))
        self.label_7.setText(_translate("TarafEkle", "Doğum Tarihi"))
        self.label_8.setText(_translate("TarafEkle", "Telefon"))
        self.label_9.setText(_translate("TarafEkle", "Adres"))
        self.label_10.setText(_translate("TarafEkle", "Kanuni Temsilcisi"))
        self.pushButton.setText(_translate("TarafEkle", "Ekle"))
        self.label_11.setText(_translate("TarafEkle", "Tercüman"))
        self.checkBox.setText(_translate("TarafEkle", "Yok"))
        self.checkBox_2.setText(_translate("TarafEkle", "Var"))
        self.checkBox_3.setText(_translate("TarafEkle", "Yok"))
        self.checkBox_4.setText(_translate("TarafEkle", "Var"))
        self.groupBox.setTitle(_translate("TarafEkle", "Kanuni Temsilci Bilgileri"))
        self.label_13.setText(_translate("TarafEkle", "Ad Soyad"))
        self.label_14.setText(_translate("TarafEkle", "Sicil No"))
        self.label_15.setText(_translate("TarafEkle", "Telefon"))
        self.label_16.setText(_translate("TarafEkle", "Adres"))
        self.groupBox_2.setTitle(_translate("TarafEkle", "Tercüman Bilgileri"))
        self.label_17.setText(_translate("TarafEkle", "Ad Soyad"))
        self.label_18.setText(_translate("TarafEkle", "TC No"))
        self.label_19.setText(_translate("TarafEkle", "Adres"))
        self.label_12.setText(_translate("TarafEkle", "Cinsiyet"))
        self.comboBox_2.setItemText(0, _translate("TarafEkle", "Cinsiyet"))
        self.comboBox_2.setItemText(1, _translate("TarafEkle", "Kadın"))
        self.comboBox_2.setItemText(2, _translate("TarafEkle", "Erkek"))
        self.groupBox.hide()
        self.groupBox_2.hide()

        self.db = VbagKur()
        sonuc = self.db.komut(
            "SELECT * FROM taraflar WHERE dosya == '{}' and ad == '{}'".format(self.dosya_uzlasma_no, kisi))
        self.lineEdit.setText(sonuc[0][1])
        self.comboBox.setCurrentText(sonuc[0][2])
        self.lineEdit_2.setText(sonuc[0][3])
        self.lineEdit_3.setText(sonuc[0][4])
        self.lineEdit_4.setText(sonuc[0][5])
        self.lineEdit_5.setText(sonuc[0][6])
        self.lineEdit_6.setText(sonuc[0][7])
        self.comboBox_2.setCurrentText(sonuc[0][8])
        self.lineEdit_7.setText(sonuc[0][9])
        self.comboBox_3.setCurrentIndex(sonuc[0][10])
        self.textEdit.setText(sonuc[0][11])
        if len(sonuc[0][12]) == 4:
            pass
        else:
            self.checkBox_2.setChecked(True)
            self.checkBox_2.setDisabled(True)
            self.checkBox.setChecked(False)
            self.resize(570, 479)
            temsil = self.db.komut(
                "select ad,sicil,tel,adres from temsilciler where ad == '{}' and kisi == '{}'".format(sonuc[0][12],
                                                                                                      kisi))
            self.groupBox.show()
            self.lineEdit_8.setText(temsil[0][0])
            self.lineEdit_9.setText(temsil[0][1])
            self.lineEdit_10.setText(temsil[0][2])
            self.textEdit_2.setText(temsil[0][3])

        if len(sonuc[0][13]) == 4:
            pass
        else:
            tercu = self.db.komut(
                "select ad,tc,adres from tercuman where ad == '{}' and kisi == '{}'".format(sonuc[0][13],
                                                                                                      kisi))
            self.groupBox_2.show()
            self.checkBox_4.setChecked(True)
            self.checkBox_4.setDisabled(True)
            self.checkBox_3.setChecked(False)
            self.resize(570, 479)
            self.lineEdit_11.setText(temsil[0][0])
            self.lineEdit_12.setText(temsil[0][1])
            self.textEdit_3.setText(temsil[0][2])

        self.show()
        # Buradan sonrasına karışma
        self.pushButton.clicked.connect(self.buton_birinci_gorev)

        self.setWindowTitle("Yeni Uzlaşma Dosyası Ekle")
        self.show()

        self.checkBox_2.clicked.connect(self.temsilci_ac)
        self.checkBox.clicked.connect(self.temsilci_kapat)
        self.checkBox_4.clicked.connect(self.tercuman_ac)
        self.checkBox_3.clicked.connect(self.tercuman_kapat)


    def temsilci_ac(self):
        self.checkBox.setChecked(False)
        self.resize(570, 479)
        self.groupBox.show()
        self.checkBox_2.setDisabled(True)
        self.checkBox.setDisabled(False)

    def temsilci_kapat(self):
        self.checkBox_2.setChecked(False)
        self.groupBox.hide()
        self.checkBox.setDisabled(True)
        self.checkBox_2.setDisabled(False)
        if self.checkBox_4.isChecked():
            pass
        else:
            self.resize(277, 475)

    def tercuman_ac(self):
        self.checkBox_3.setChecked(False)
        self.resize(570, 479)
        self.checkBox_4.setDisabled(True)
        self.checkBox_3.setDisabled(False)
        self.groupBox_2.show()

    def tercuman_kapat(self):
        self.checkBox_4.setChecked(False)
        self.groupBox_2.hide()
        self.checkBox_3.setDisabled(True)
        self.checkBox_4.setDisabled(False)
        if self.checkBox_2.isChecked():
            pass
        else:
            self.resize(277, 475)

    def buton_birinci_gorev(self):
        ad = self.lineEdit.text()
        sifat = self.comboBox.currentText()
        tc = self.lineEdit_2.text()
        baba = self.lineEdit_3.text()
        ana = self.lineEdit_4.text()
        dyer = self.lineEdit_5.text()
        dtar = self.lineEdit_6.text()
        cins = self.comboBox_2.currentText()
        tel = self.lineEdit_7.text()
        adresniteligi = self.comboBox_3.currentIndex()
        adres = self.textEdit.toPlainText()

        db = VbagKur()

        if self.checkBox_2.isChecked():
            tad = self.lineEdit_8.text()
            tsic = self.lineEdit_9.text()
            ttel = self.lineEdit_10.text()
            tadres = self.textEdit_2.toPlainText()
            db.temsilci_ekle(tad, tsic, ttel, tadres,self.dosya_uzlasma_no, ad, sifat)
        else:
            tad = None
            tsic = None
            ttel = None
            tadres = None

        if self.checkBox_4.isChecked():
            tead = self.lineEdit_11.text()
            tetc = self.lineEdit_12.text()
            teadres = self.textEdit_3.toPlainText()
            db.tercuman_ekle(tead, tetc, teadres, self.dosya_uzlasma_no, ad)
        else:
            tead = None
            tetc = None
            teadres = None

        if db.tarafekle(ad, sifat, tc, baba, ana, dyer, dtar, cins, tel, adresniteligi, adres, tad, tead, self.dosya_uzlasma_no) == True:
            baslik = "Dosya Bilgileri Eklendi"
            mesaj = ad + " isimli kişinin bilgileri" + sifat + " olarak  veritabanına eklendi."
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.lineEdit_9.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.textEdit_3.clear()
            self.comboBox.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_3.setCurrentIndex(0)
            self.checkBox.setChecked(True)
            self.checkBox_3.setChecked(True)
            self.checkBox_2.setChecked(False)
            self.checkBox_2.setDisabled(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_4.setDisabled(False)
        else:
            pass

        self.on_changed_value(False)

    def on_changed_value(self, value):
        self.clicked.emit(value)
