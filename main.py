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

app = QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
