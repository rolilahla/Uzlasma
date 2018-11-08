# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bilgirisi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from temsilci import Ui_Temsilci
from vtbgln import VbagKur

class Ui_Bilgi(Ui_Temsilci, VbagKur):
    def temsil(self, ad,soyad):
        self.t = QtWidgets.QMainWindow()
        self.ui_t = Ui_Temsilci()
        self.ui_t.setupUi(self.t)
        self.t.show()

    def setupUi(self, Bilgi):
        Bilgi.setObjectName("Bilgi")
        Bilgi.resize(350, 563)
        self.label_6 = QtWidgets.QLabel(Bilgi)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Bilgi)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 141, 21))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_6 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 70, 141, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(Bilgi)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 38, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_7.setGeometry(QtCore.QRect(100, 100, 141, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Bilgi)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Bilgi)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 160, 141, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 190, 141, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(Bilgi)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 71, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 220, 141, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(Bilgi)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 71, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_11.setGeometry(QtCore.QRect(100, 250, 141, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(Bilgi)
        self.label_12.setGeometry(QtCore.QRect(10, 250, 71, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Bilgi)
        self.label_13.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(Bilgi)
        self.lineEdit_12.setGeometry(QtCore.QRect(100, 280, 141, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_14 = QtWidgets.QLabel(Bilgi)
        self.label_14.setGeometry(QtCore.QRect(10, 310, 71, 16))
        self.label_14.setObjectName("label_14")
        self.textEdit = QtWidgets.QTextEdit(Bilgi)
        self.textEdit.setGeometry(QtCore.QRect(100, 310, 241, 81))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Bilgi)
        self.pushButton.setGeometry(QtCore.QRect(260, 520, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_15 = QtWidgets.QLabel(Bilgi)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(Bilgi)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 40, 141, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(Bilgi)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 130, 141, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_16 = QtWidgets.QLabel(Bilgi)
        self.label_16.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Bilgi)
        self.label_17.setGeometry(QtCore.QRect(10, 400, 71, 16))
        self.label_17.setObjectName("label_17")
        self.textEdit_2 = QtWidgets.QTextEdit(Bilgi)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 400, 241, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.db = VbagKur()
        self.a = self.db.hepsini_oku("sorno","uzlasma")
        self.b = self.db.veri_duzenle(self.a)
        for i in range(len(self.b)):
            self.comboBox.addItem("{}".format(self.b[i]))

        self.retranslateUi(Bilgi)
        self.pushButton.clicked.connect(self.topla)
        self.comboBox_3.currentIndexChanged['int'].connect(self.kayarla)
        QtCore.QMetaObject.connectSlotsByName(Bilgi)

    def retranslateUi(self, Bilgi):
        _translate = QtCore.QCoreApplication.translate
        Bilgi.setWindowTitle(_translate("Bilgi", "Uzlaştırma Teklifi Yapılan"))
        self.label_6.setText(_translate("Bilgi", "Yükümlülüğü"))
        self.label_7.setText(_translate("Bilgi", "Tc No"))
        self.label_8.setText(_translate("Bilgi", "Adı Soyadı"))
        self.label_9.setText(_translate("Bilgi", "Baba Adı"))
        self.label_10.setText(_translate("Bilgi", "Anne Adı"))
        self.label_11.setText(_translate("Bilgi", "Doğum Yeri"))
        self.label_12.setText(_translate("Bilgi", "Doğum Tarihi"))
        self.label_13.setText(_translate("Bilgi", "Telefon No"))
        self.label_14.setText(_translate("Bilgi", "Adres"))
        self.pushButton.setText(_translate("Bilgi", "Ekle"))
        self.label_15.setText(_translate("Bilgi", "Soruşturma No"))
        self.comboBox_2.setItemText(0, _translate("Bilgi", "Mağdur"))
        self.comboBox_2.setItemText(1, _translate("Bilgi", "Suçtan Zarar Gören"))
        self.comboBox_2.setItemText(2, _translate("Bilgi", "Şüpheli"))
        self.comboBox_2.setItemText(3, _translate("Bilgi", "Müşteki"))
        self.comboBox_3.setItemText(0, _translate("Bilgi", "Yok"))
        self.comboBox_3.setItemText(1, _translate("Bilgi", "Var"))
        self.label_16.setText(_translate("Bilgi", "Kanuni Temsilcisi var mı"))
        self.label_17.setText(_translate("Bilgi", "Açıklama"))

    def kayarla(self):
        self.sorno = self.comboBox.currentText()
        self.yukum = self.comboBox_2.currentText()
        self.tc = self.lineEdit_6.text()
        self.ad = self.lineEdit_7.text()
        self.temsil(self.ad, self.tc)

    def topla(self):
        bad = self.lineEdit_8.text()
        anad = self.lineEdit_9.text()
        dyeri = self.lineEdit_10.text()
        dtar = self.lineEdit_11.text()
        tel = self.lineEdit_12.text()
        adre = self.textEdit.toPlainText()
        aci = self.textEdit_2.toPlainText()

        print("""
            {}
            {}
            {}
            {}
            {}
            {}
            {}
            {}
            {}
            {}
            {}
            """.format(self.sorno, self.yukum, self.tc, self.ad, bad,anad, dyeri, dtar, tel, adre, aci))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bilgi = QtWidgets.QDialog()
    ui = Ui_Bilgi()
    ui.setupUi(Bilgi)
    Bilgi.show()
    sys.exit(app.exec_())

