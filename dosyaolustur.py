# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyaolustur.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from vtbgln import VbagKur
from mico import bilgilendir
import datetime

class DosyaOlustur(QtWidgets.QDialog):
    # Added a signal
    clicked = pyqtSignal(bool)

    def __init__(self):
        super(DosyaOlustur, self).__init__()
        self.init_ui()


    def init_ui(self):
        self.db = VbagKur()
        self.resize(423, 263)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/ubuntuone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(240, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 10, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 40, 90, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 40, 170, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 70, 170, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 90, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 90, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 100, 170, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 130, 170, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(130, 130, 90, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 160, 170, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(130, 160, 90, 20))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(130, 10, 90, 20))
        self.label_4.setObjectName("label_4")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(130, 190, 90, 20))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(239, 190, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-11, 0, 141, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 50, 121, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/ubuntuone.png"))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(336, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.radioButton.setChecked(True)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.buton_birinci_gorev)

        self.setWindowTitle("Yeni Uzlaşma Dosyası Ekle")
        self.uzlastirmaci_cek()
        self.show()

    def retranslateUi(self, DosyaOlustur):
        _translate = QtCore.QCoreApplication.translate
        DosyaOlustur.setWindowTitle(_translate("DosyaOlustur", "Dosya Oluştur"))
        self.label.setText(_translate("DosyaOlustur", "Uzlaşma No"))
        self.label_2.setText(_translate("DosyaOlustur", "Soruşturma  No"))
        self.label_3.setText(_translate("DosyaOlustur", "Mahkeme Esas No"))
        self.label_5.setText(_translate("DosyaOlustur", "Suç / Suçlar"))
        self.pushButton.setText(_translate("DosyaOlustur", "Oluştur"))
        self.label_7.setText(_translate("DosyaOlustur", "Tevdi Tarihi"))
        self.label_4.setText(_translate("DosyaOlustur", "Dosya Türü"))
        self.radioButton.setText(_translate("DosyaOlustur", "Savcılık"))
        self.radioButton_2.setText(_translate("DosyaOlustur", "Mahkeme"))
        self.label_8.setText(_translate("DosyaOlustur", "Uzlaştırmacı"))

    def buton_birinci_gorev(self):
        if self.radioButton.isChecked() == True:
            uzno = self.lineEdit.text()
            sorno = self.lineEdit_2.text()
            meno = self.lineEdit_3.text()
            suc = self.lineEdit_4.text()
            ttarih = self.lineEdit_5.text()
            uzlastirici = self.comboBox.currentText()
            tevdi = "Savcılık"
            # Dosya teslim tarihini bulmak için
            # teslim alınma süresinin üzerine veritabanından gelen süreyi ekliyoruz
        elif self.radioButton_2.isChecked() == True:
            uzno = self.lineEdit.text()
            sorno = self.lineEdit_2.text()
            meno = self.lineEdit_3.text()
            suc = self.lineEdit_4.text()
            ttarih = self.lineEdit_5.text()
            uzlastirici = self.comboBox.currentText()
            tevdi = "Mahkeme"

        sure = self.db.komut("select teslim_suresi from ayarlar")
        t = ttarih.replace(".", "/")
        formatstr = '%d/%m/%Y'
        t3 = datetime.datetime.strptime(t, formatstr)

        fark = datetime.timedelta(days=int(sure[0][0]))
        gelecek = t3 + fark
        uzatmatar = gelecek.date()
        if self.db.dosya_ekle(uzno, sorno, meno, suc, ttarih, tevdi, 1, uzatmatar, uzlastirici) == True:
            baslik = "Dosya Bilgileri Eklendi"
            mesaj = uzno + " Uzlaşma No'lu dosya bilgileri veritabanına başarıyla eklendi"
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
        else:
            pass

        self.on_changed_value(False)

    def uzlastirmaci_cek(self):
        sor = self.db.komut("select isim from uzlasmaci")
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i][0])

    def on_changed_value(self, value):
        self.clicked.emit(value)