# -*- coding:utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from uzlastirmaciekle import Ui_UzlastirmaciEkle

def gui_uzlastirmaci_ekle(self):
    UzlastirmaciEkle = QtWidgets.QDialog()
    ui = Ui_UzlastirmaciEkle()
    ui.setupUi(UzlastirmaciEkle)
    UzlastirmaciEkle.show()
    UzlastirmaciEkle.exec_()