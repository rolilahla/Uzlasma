# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sablonekle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mico
from vtbgln import VbagKur

class Ui_SablonEkle(object):
    def setupUi(self, SablonEkle):
        self.db = VbagKur()
        SablonEkle.setObjectName("SablonEkle")
        SablonEkle.resize(541, 305)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/gnome-contacts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SablonEkle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SablonEkle)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SablonEkle)
        self.label.setMinimumSize(QtCore.QSize(90, 0))
        self.label.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(SablonEkle)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(SablonEkle)
        self.label_2.setMinimumSize(QtCore.QSize(90, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(SablonEkle)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 2, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(393, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(SablonEkle)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)

        self.retranslateUi(SablonEkle)
        self.pushButton.clicked.connect(self.sablon_ekle)
        QtCore.QMetaObject.connectSlotsByName(SablonEkle)

    def retranslateUi(self, SablonEkle):
        _translate = QtCore.QCoreApplication.translate
        SablonEkle.setWindowTitle(_translate("SablonEkle", "Şablon Ekle"))
        self.label.setText(_translate("SablonEkle", "Şablon Adı"))
        self.label_2.setText(_translate("SablonEkle", "Şablon Adı"))
        self.pushButton.setText(_translate("SablonEkle", "Ekle"))

    def sablon_ekle(self):
        isim = self.lineEdit.text()
        sablon_metni = self.textEdit.toPlainText()
        if self.db.yapistir("INSERT INTO sablonlar VALUES(NULL, '{}', '{}')".format(isim, sablon_metni)) == True:
            baslik = "Şablon Ekle"
            mesaj = isim + " isimli şablon metni veritabanına eklendi"
            mico.bilgilendir(mesaj, baslik)
            self.lineEdit.clear()
            self.textEdit.clear()
        else:
            baslik = "Şablon Ekleme Hatası"
            mesaj = isim + " isimli şablon veritabanına eklenemedi"
            mico.bilgilendir(mesaj, baslik)


import icon

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SablonEkle = QtWidgets.QDialog()
    ui = Ui_SablonEkle()
    ui.setupUi(SablonEkle)
    SablonEkle.show()
    sys.exit(app.exec_())

