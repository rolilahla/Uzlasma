# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dosyasil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import modul as mdl
from vtbgln import VbagKur

class Ui_DosyaSil(object):
    def setupUi(self, DosyaSil):
        self.db = VbagKur()

        DosyaSil.setObjectName("DosyaSil")
        DosyaSil.resize(353, 114)
        self.label = QtWidgets.QLabel(DosyaSil)
        self.label.setGeometry(QtCore.QRect(160, 20, 90, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(DosyaSil)
        self.comboBox.setGeometry(QtCore.QRect(230, 20, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(DosyaSil)
        self.pushButton.setGeometry(QtCore.QRect(260, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(DosyaSil)
        self.pushButton.clicked.connect(DosyaSil.close)
        QtCore.QMetaObject.connectSlotsByName(DosyaSil)
        self.dosya_tara()

    def dosya_tara(self):
        sor = mdl.tekli_demet_coz(mdl.dosya_tara())
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i])
    def dosya_sil(self):
        self.db.dosya_sil(self.comboBox.currentText)

    def retranslateUi(self, DosyaSil):
        _translate = QtCore.QCoreApplication.translate
        DosyaSil.setWindowTitle(_translate("DosyaSil", "Dosya Sil"))
        self.label.setText(_translate("DosyaSil", "Uzlaşma No"))
        self.pushButton.setText(_translate("DosyaSil", "Sil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DosyaSil = QtWidgets.QDialog()
    ui = Ui_DosyaSil()
    ui.setupUi(DosyaSil)
    DosyaSil.show()
    sys.exit(app.exec_())

