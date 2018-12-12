# -*- coding:utf-8 -*-

from PyQt5 import QtWidgets

def bilgilendir(mesaj, baslik):
    inf = QtWidgets.QMessageBox()
    inf.setIcon(QtWidgets.QMessageBox.Information)
    inf.setWindowTitle(baslik)
    inf.setText(mesaj)
    inf.setStandardButtons(QtWidgets.QMessageBox.Ok)
    inf.exec_()

def guncelleme_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Güncelleme Uyarısı !!!')
    yazi = gemi + ' kişisinin bilgilerini güncellemek istediğinize emin misiniz ?'
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

def kayit_sil_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + ' kişisinin bilgilerini veritabanından silmek istediğinize emin misiniz ?'
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

def gider_sil_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + " harcamasını veritabanından silmek istediğinize emin misiniz ?"
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

def ek_sil_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Kayıt Silme Uyarısı !!!')
    yazi = gemi + " Ek adını veritabanından silmek istediğinize emin misiniz ?"
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

def dosya_kapat_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Dosya Kapatma Uyarısı !!!')
    yazi = gemi + " No'lu dosyayı kapatmak istediğinize emin misiniz ?"
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

def dosya_ac_soru(gemi: object) -> object:
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle('Dosya Açma Uyarısı !!!')
    yazi = gemi + " No'lu dosyayı açmak istediğinize emin misiniz ?"
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

def sorusor(baslik, arg, soru):
    dens_box = QtWidgets.QMessageBox()
    dens_box.setIcon(QtWidgets.QMessageBox.Question)
    dens_box.setWindowTitle(baslik)
    yazi = arg + soru
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