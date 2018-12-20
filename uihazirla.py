# -*- coding:utf-8 -*-

from PyQt5 import QtGui, QtCore, QtWidgets
from uzlastirmaciekle import Ui_UzlastirmaciEkle
from uzlasmacisil import Ui_UzlasmaciSil
from dosyasil import Ui_DosyaSil
from settings import Ui_Settings

def gui_uzlastirmaci_ekle(self):
    UzlastirmaciEkle = QtWidgets.QDialog()
    ui = Ui_UzlastirmaciEkle()
    ui.setupUi(UzlastirmaciEkle)
    UzlastirmaciEkle.show()
    UzlastirmaciEkle.exec_()

def gui_uzlastirmaci_sil(self):
    UzlastirmaciSil = QtWidgets.QDialog()
    ui = Ui_UzlasmaciSil()
    ui.setupUi(UzlastirmaciSil)
    UzlastirmaciSil.show()
    UzlastirmaciSil.exec_()

def gui_dosya_sil(self):
    DosyaSil = QtWidgets.QDialog()
    ui = Ui_DosyaSil()
    ui.setupUi(DosyaSil)
    DosyaSil.show()
    DosyaSil.exec_()

def gui_settings(self):
    Sett = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Sett)
    Sett.show()
    Sett.exec_()