# -*- coding:utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from uzlastirmaciekle import Ui_UzlastirmaciEkle
from uzlasmacisil import Ui_Dialog
from dosyasil import Ui_DosyaSil

def gui_uzlastirmaci_ekle(self):
    UzlastirmaciEkle = QtWidgets.QDialog()
    ui = Ui_UzlastirmaciEkle()
    ui.setupUi(UzlastirmaciEkle)
    UzlastirmaciEkle.show()
    UzlastirmaciEkle.exec_()

def gui_uzlastirmaci_sil(self):
    UzlastirmaciSil = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(UzlastirmaciSil)
    UzlastirmaciSil.show()
    UzlastirmaciSil.exec_()

def gui_dosya_sil(self):
    DosyaSil = QtWidgets.QDialog()
    ui = Ui_DosyaSil()
    ui.setupUi(DosyaSil)
    DosyaSil.show()
    DosyaSil.exec_()