# -*- coding:utf-8 -*-
# -*- coding:cp1254 -*-

import time, sys, math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSignal
from untitle import Ui_MainWindow


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
    	super().__init__()
    	self.ui = Ui_MainWindow()
    	self.ui.setupUi(self)
    	"""
    	#toolbar yapımı
    	self.toolbar = self.addToolBar("Exit")

    	#uzlaşmacı butonu
    	self.exitAct = QAction(QIcon('lib/icon/w.png'), 'Uzlaşmacı Ayarla', self)
    	self.exitAct.setShortcut('Ctrl + Q')
    	self.exitAct.triggered.connect(self.uzw)
    	self.toolbar.addAction(self.exitAct)

    	#Yeni Uzlaşma Butonu
    	self.yeni_uz = QAction(QIcon('lib/icon/kayit.png'), 'Yeni Uzlaşma', self)
    	self.yeni_uz.setShortcut('Ctrl + N')
    	self.yeni_uz.triggered.connect(self.uekl)
    	self.toolbar.addAction(self.yeni_uz)
    	"""

    

app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
