# -*- coding:utf-8 -*-

from PyQt5 import QtGui, QtWidgets

def bilgilendir(mesaj, baslik):
    inf = QtWidgets.QMessageBox()
    inf.setIcon(QtWidgets.QMessageBox.Information)
    inf.setWindowTitle(baslik)
    inf.setText(mesaj)
    inf.setStandardButtons(QtWidgets.QMessageBox.Ok)
    inf.exec_()