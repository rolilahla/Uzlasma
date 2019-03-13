# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sablonsil.ui'
#
# Created by: Mehmet Eroğlu <rolilahla@gmail.com>
#
#

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mico
import icon

class Ui_SablonDuzenle(object):
    def setupUi(self, SablonDuzenle):
        self.sablon_id = None
        self.db = VbagKur()
        SablonDuzenle.setObjectName("SablonDuzenle")
        SablonDuzenle.resize(561, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/gnome-contacts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SablonDuzenle.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(SablonDuzenle)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SablonDuzenle)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(SablonDuzenle)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(SablonDuzenle)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 3, 1)
        self.lineEdit = QtWidgets.QLineEdit(SablonDuzenle)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(SablonDuzenle)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(SablonDuzenle)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(509, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(SablonDuzenle)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(SablonDuzenle)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 3, 1, 1)

        self.retranslateUi(SablonDuzenle)
        self.pushButton.clicked.connect(self.sablon_sil)
        self.pushButton_2.clicked.connect(self.sablon_guncelle)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.hazirlik_bitir)
        self.hazirlik()
        QtCore.QMetaObject.connectSlotsByName(SablonDuzenle)

    def retranslateUi(self, SablonDuzenle):
        _translate = QtCore.QCoreApplication.translate
        SablonDuzenle.setWindowTitle(_translate("SablonDuzenle", "Şablon Düzenle & Sil"))
        self.label.setText(_translate("SablonDuzenle", "Şablonlar"))
        self.label_3.setText(_translate("SablonDuzenle", "Şablon Adı"))
        self.label_2.setText(_translate("SablonDuzenle", "Şablon Metni"))
        self.pushButton.setText(_translate("SablonDuzenle", "Sil"))
        self.pushButton_2.setText(_translate("SablonDuzenle", "Güncelle"))

    def hazirlik(self):
        sor = self.db.komut("select ad from sablonlar ")
        if len(sor) == 0:
            baslik = "Şablon Düzenleme & Silme Hatası"
            mesaj = "Veritabanında Düzenlenecek veya silinecek herhangi bir şablon kaydı bulunmamakta"
        else:
            for i in range(len(sor)):
                self.listWidget.addItem(sor[i][0])

    def hazirlik_bitir(self):
        sor  = self.db.komut("select * from sablonlar where ad = '{}'".format(self.listWidget.currentItem().text()))
        self.sablon_id = sor[0][0]
        self.lineEdit.setText(sor[0][1])
        self.textEdit.setPlainText(sor[0][2])

    def sablon_sil(self):
        if mico.sorusor("Şablon Sil",self.lineEdit.text(),
                        " Kaydını veritabanından silmek istediğinize emin misiniz ?") == True:
            self.db.satir_sil("Delete From sablonlar where id = '{}'".format(self.sablon_id))
            baslik = "Şablon Kaydı Sil"
            mesaj = self.lineEdit.text() + " kaydı veritabanından başarıyla silindi"
            mico.bilgilendir(mesaj, baslik)
            self.listWidget.clear()
            self.hazirlik()
            self.lineEdit.clear()
            self.textEdit.clear()
        else:
            baslik = "Şablon Kaydı Silme"
            mesaj = "Kayıt Silme İşleminden vazgeçildi"
            mico.bilgilendir(mesaj, baslik)

    def sablon_guncelle(self):
        if mico.sorusor("Şablon Güncelle",self.lineEdit.text(),
                        "Şablon bilgilerini güncellemek istediğinize emin misiniz ?") == True:
            self.db.yapistir("UPDATE sablonlar SET ad='{}', icerik='{}' where id = '{}'".format(self.lineEdit.text(),
                                                                                         self.textEdit.toPlainText(),
                                                                                         self.sablon_id))
            baslik = "Şablon Güncelle"
            mesaj = self.lineEdit.text() + " şablonu başarıyla güncellendi"
            mico.bilgilendir(mesaj, baslik)
            self.listWidget.clear()
            self.hazirlik()
            self.lineEdit.clear()
            self.textEdit.clear()
        else:
            baslik = "Şablon Kaydı Güncelleme"
            mesaj = "Kayıt güncelleme işleminden vazgeçildi"
            mico.bilgilendir(mesaj, baslik)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SablonDuzenle = QtWidgets.QDialog()
    ui = Ui_SablonDuzenle()
    ui.setupUi(SablonDuzenle)
    SablonDuzenle.show()
    sys.exit(app.exec_())

