# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uzlasmacisil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vtbgln import VbagKur

class Ui_UzlasmaciSil(object):
    def setupUi(self, UzlasmaciSil):
        self.db = VbagKur()
        UzlasmaciSil.setObjectName("UzlasmaciSil")
        UzlasmaciSil.resize(525, 389)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/icon/credentials-preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UzlasmaciSil.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(UzlasmaciSil)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(UzlasmaciSil)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(UzlasmaciSil)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setWhatsThis("Etkin olması için listeden bir uzlaştırmacı seçin")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.uzlasmaci_tarama()
        self.tableWidget.cellClicked.connect(self.parametre_olustur)
        self.pushButton.clicked.connect(self.sil)

        self.retranslateUi(UzlasmaciSil)
        QtCore.QMetaObject.connectSlotsByName(UzlasmaciSil)

    def retranslateUi(self, UzlasmaciSil):
        _translate = QtCore.QCoreApplication.translate
        UzlasmaciSil.setWindowTitle(_translate("UzlasmaciSil", "Uzlaşmacı Sil"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("UzlasmaciSil", "İd"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("UzlasmaciSil", "Ad Soyad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("UzlasmaciSil", "Sicil No"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("UzlasmaciSil", "Telefon"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("UzlasmaciSil", "sehir"))
        self.pushButton.setText(_translate("UzlasmaciSil", "Sil"))

    def uzlasmaci_tarama(self):
        sonuc = self.db.komut("select id,isim,sicil,tel,sehir FROM uzlasmaci")
        self.tableWidget.setRowCount(len(sonuc))
        satir = 0
        sutun = 0

        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

    def parametre_olustur(self, row, column):
        secilen = self.tableWidget.item(row, column)
        self.secilen_id = self.tableWidget.item(row, 0)
        self.pushButton.setDisabled(False)

    def sil_soru(self):
        dens_box = QtWidgets.QMessageBox()
        dens_box.setIcon(QtWidgets.QMessageBox.Question)
        dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
        yazi = " Seçilen kayıt bilgilerini veritabanından silmek istediğinize emin misiniz ?"
        dens_box.setText(yazi)
        dens_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        buttonY = dens_box.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText('EVET')
        buttonN = dens_box.button(QtWidgets.QMessageBox.No)
        buttonN.setText('HAYIR')
        dens_box.exec_()
        if dens_box.clickedButton() == buttonY:
            return True
        else:
            return False

    def bilg(self, mesaj, baslik):
        inf = QtWidgets.QMessageBox()
        inf.setIcon(QtWidgets.QMessageBox.Information)
        inf.setWindowTitle(baslik)
        inf.setText(mesaj)
        inf.setStandardButtons(QtWidgets.QMessageBox.Ok)
        inf.exec_()

    def sil(self, id):
        if self.sil_soru() == True:
            if self.db.satir_sil("DELETE FROM uzlasmaci Where id = '{}'".format(self.secilen_id.text())) == True:
                baslik = " Kayıt Silme Uyarısı"
                mesaj = "Kayıt Başarıyla silindi"
                self.bilg(mesaj, baslik)
                self.uzlasmaci_tarama()

            else:
                pass
