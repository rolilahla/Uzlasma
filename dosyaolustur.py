# -*- coding:utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from vtbgln import VbagKur
from mico import bilgilendir

class DosyaOlustur(QtWidgets.QDialog):
    # Added a signal
    clicked = pyqtSignal(bool)

    def __init__(self):
        super(DosyaOlustur, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(424, 332)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("lib/icon/ubuntuone.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 10, 90, 20))
        self.label.setText("Soruşturma No")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 10, 170, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 40, 170, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 90, 20))
        self.label_2.setText("Uzlaşma No")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 90, 20))
        self.label_3.setText("Mahkeme Esas No")

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 70, 170, 20))

        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 100, 170, 20))

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(130, 100, 90, 20))
        self.label_4.setText("Suç / Suçlar")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(130, 130, 90, 20))
        self.label_5.setText("Teklif / Davet Tarihi")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(340, 290, 75, 23))
        self.pushButton.setText("Oluştur")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 121, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("lib/icon/ubuntuone.png"))

        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 130, 170, 20))

        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 160, 170, 20))

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(130, 160, 90, 20))
        self.label_7.setText("Taraf Sayısı")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(130, 190, 90, 20))
        self.label_8.setText("Adres")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(240, 190, 171, 81))
        self.textEdit.setObjectName("textEdit")
        self.show()

        # Setting a connection between slider position change and on_changed_value function

        # Buradan sonrasına karışma
        self.pushButton.clicked.connect(self.buton_birinci_gorev)

        self.setWindowTitle("Yeni Uzlaşma Dosyası Ekle")
        self.show()

    def buton_birinci_gorev(self):
        sorno = self.lineEdit.text()
        uzno = self.lineEdit_2.text()
        meno = self.lineEdit_3.text()
        suc = self.lineEdit_4.text()
        ttarih = self.lineEdit_5.text()
        taraf = self.lineEdit_6.text()
        ozet = self.textEdit.toPlainText()
        db = VbagKur()
        if db.dosya_ekle(sorno, uzno, meno, suc, ttarih, taraf, ozet) == True:
            baslik = "Dosya Bilgileri Eklendi"
            mesaj = sorno + " Soruşturma No'lu dosya bilgileri veritabanına başarıyla eklendi"
            bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.textEdit.clear()
        else:
            pass

        self.on_changed_value(False)

    def on_changed_value(self, value):
        self.clicked.emit(value)
