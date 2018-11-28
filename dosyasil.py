# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyasil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DosyaSil(object):
    def setupUi(self, DosyaSil):
        DosyaSil.setObjectName("DosyaSil")
        DosyaSil.resize(721, 336)
        self.gridLayout = QtWidgets.QGridLayout(DosyaSil)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(DosyaSil)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 4)
        self.label = QtWidgets.QLabel(DosyaSil)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(443, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(DosyaSil)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(3, "")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(DosyaSil)
        self.pushButton.setEnabled(False)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 3, 1, 1)

        self.retranslateUi(DosyaSil)
        QtCore.QMetaObject.connectSlotsByName(DosyaSil)

    def retranslateUi(self, DosyaSil):
        _translate = QtCore.QCoreApplication.translate
        DosyaSil.setWindowTitle(_translate("DosyaSil", "Dialog"))
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
        item.setText(_translate("DosyaSil", "Teklif Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DosyaSil", "Tevdi Tarihi"))
        self.label.setText(_translate("DosyaSil", "Listelenmesini istedğiniz Dosya Türü"))
        self.comboBox.setItemText(0, _translate("DosyaSil", "Dosya Seç"))
        self.comboBox.setItemText(1, _translate("DosyaSil", "Aktif Dosyalar"))
        self.comboBox.setItemText(2, _translate("DosyaSil", "Kapanmış Dosyalar"))
        self.pushButton.setText(_translate("DosyaSil", "Sil"))

