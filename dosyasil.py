# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyasil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur
import mico

class Ui_DosyaSil(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(Ui_DosyaSil, self).__init__()
        self.initui()

    def initui(self):
        self.dosya_id = None
        self.dosya_ad = None
        self.db = VbagKur()
        self.setObjectName("DosyaSil")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/ubuntuone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.resize(721, 336)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(443, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 3, 1, 1)
        self.tableWidget.cellClicked.connect(self.dosya_bul)
        self.comboBox.currentIndexChanged.connect(self.adana)
        self.pushButton.setDisabled(True)
        self.pushButton.clicked.connect(self.sil)
        self.tum_dosyalar()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, DosyaSil):
        _translate = QtCore.QCoreApplication.translate
        DosyaSil.setWindowTitle(_translate("DosyaSil", "Dosya Sil"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DosyaSil", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DosyaSil", "Uzlaşma No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DosyaSil", "Soruşturma No"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DosyaSil", "M. Esas No"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DosyaSil", "Suç"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DosyaSil", "Tevdi Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DosyaSil", "Nitelik"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("DosyaSil", "Durum"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("DosyaSil", "Teslim Tarihi"))
        self.label.setText(_translate("DosyaSil", "Listelenmesini istedğiniz Dosya Türü"))
        self.comboBox.setItemText(0, _translate("DosyaSil", "Tüm Dosyalar"))
        self.comboBox.setItemText(1, _translate("DosyaSil", "Aktif Dosyalar"))
        self.comboBox.setItemText(2, _translate("DosyaSil", "Kapanmış Dosyalar"))
        self.pushButton.setText(_translate("DosyaSil", "Sil"))

    def tum_dosyalar(self):
        sonuc = self.db.komut("select * from dosyalar")
        if len(sonuc) == 0:
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)

        self.tableWidget.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

    def aktif_dosyalar(self):
        sonuc = self.db.komut("select * from dosyalar where durum ='1'")
        if len(sonuc) == 0:
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)
        self.tableWidget.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

    def pasif_dosyalar(self):
        sonuc = self.db.komut("select * from dosyalar where durum ='0'")
        if len(sonuc) == 0:
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)
        self.tableWidget.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

    def adana(self):
        if self.comboBox.currentIndex() == 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount())
            self.tum_dosyalar()
        elif self.comboBox.currentIndex() == 1:
            self.tableWidget.removeRow(self.tableWidget.rowCount())
            self.aktif_dosyalar()
        elif self.comboBox.currentIndex() == 2:
            self.tableWidget.removeRow(self.tableWidget.rowCount())
            self.pasif_dosyalar()
        else:
            pass

    def dosya_bul(self, row, column):
        dosya = self.tableWidget.item(row, 0)
        dosya_2 = self.tableWidget.item(row, 1)
        self.dosya_id = dosya.text()
        self.dosya_ad = dosya_2.text()

    def sil(self):
        if mico.sorusor("Dosya Silme Uarısı",self.dosya_ad," No'lu dosyayı silmek isteiğinize emin misiniz") == True:
            if self.db.yapistir("delete from dosyalar where id='{}'".format(self.dosya_id)) == True:
                self.db.yapistir("delete from taraflar where dosya ='{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from edim where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from ek where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir(" delete from giderler where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from olaylar where uzno = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from temsilciler where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from tercuman where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from uzatma where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from uzbas where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from uzgor where dosya = '{0}'".format(self.dosya_ad))
                self.db.yapistir("delete from sonuc where dosya = '{0}'".format(self.dosya_ad))
                mico.bilgilendir("Dosya başarıyla silindi", "Dosya Silme Uyarısı")
                self.on_changed_value(False)
            else:
                pass
            self.adana()
        else:
            mico.bilgilendir("Dosya silme işlemi iptal edildi", "Dosya Silme İptali")


    def on_changed_value(self, value):
        self.clicked.emit(value)
