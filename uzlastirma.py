# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled-son.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from typing import Any, Callable

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import modul as mdl
import uihazirla as uih
from dosyaolustur import DosyaOlustur
from dosyasil import Ui_DosyaSil
from taraf import TarafEkle
from mico import bilgilendir, kayit_sil_soru, gider_sil_soru, ek_sil_soru, dosya_kapat_soru, dosya_ac_soru
from tarafduzenle import TarafDuzenle
from gider import Gider
from ek import Ekler
from vtbgln import VbagKur
import datetime
import icon

class Ui_MainWindow(object):
    dosya_teslim_tarihi = ...  # type: None

    def gui_dosya_olustur(self):
        self.p = DosyaOlustur()
        self.make_connection(self.p)
        self.p.show()
        self.p.exec_()

    def gui_dosya_sil(self):
        self.ds = Ui_DosyaSil()
        self.dosya_sil_connection(self.ds)
        self.ds.show()
        self.ds.exec_()

    def gui_taraf_ekle(self):
        if self.comboBox.currentIndex() == 0:
            baslik = "Uyari !!!"
            mesaj = "Lütfen Taraf Eklenecek Dosyayı  Seçin"
            bilgilendir(mesaj, baslik)
        else:
            self.ta = TarafEkle()
            self.ta.init_ui(self.comboBox.currentText())
            self.taraf_connection(self.ta)
            self.ta.show()
            self.ta.exec_()

    def gui_taraf_duzenle(self, kisi, nitelik):
        self.tad = TarafDuzenle()
        self.tad.init_ui(self.comboBox.currentText(), kisi, nitelik)
        self.taraf_connection(self.tad)
        self.tad.show()
        self.tad.exec_()

    def gui_gider(self, dosya):
        if self.comboBox.currentIndex() == 0:
            baslik = "Uyari !!!"
            mesaj = "Lütfen Gider Eklenecek Dosyayı  Seçin"
            bilgilendir(mesaj, baslik)
        else:
            self.gid = Gider()
            self.gid.init_ui(dosya)
            self.gider_connection(self.gid)
            self.gid.show()
            self.gid.exec_()

    def gui_ek(self, dosya):
        if self.comboBox.currentIndex() == 0:
            baslik = "Uyari !!!"
            mesaj = "Lütfen Gider Eklenecek Dosyayı  Seçin"
            bilgilendir(mesaj, baslik)
        else:
            self.ek = Ekler()
            self.ek.init_ui(dosya)
            self.ek_connection(self.ek)
            self.ek.show()
            self.ek.exec_()

    def setupUi(self, MainWindow):
        self.veritabani = VbagKur()
        self.dosya_teslim_tarihi = None
        self.dosya_uzatma_tarihi = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/uzlastırma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setMinimumSize(QtCore.QSize(230, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(9, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_11.addWidget(self.radioButton, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_11.addWidget(self.radioButton_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_11.addWidget(self.comboBox, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_11.addWidget(self.label_8, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 4, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_11.addWidget(self.label_10, 5, 1, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(53, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName("label_12")
        self.gridLayout_12.addWidget(self.label_12, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setClearButtonEnabled(True)
        self.gridLayout_12.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_12.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_12.addWidget(self.label_16, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_12.addWidget(self.comboBox_2, 2, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(13, 20, 71, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(90, 20, 120, 20))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(90, 40, 120, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(13, 40, 71, 20))
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_8.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/gtk-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_8.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/gtk-no.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_8.addWidget(self.pushButton_6, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget.setMinimumSize(QtCore.QSize(171, 140))
        self.tableWidget.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(22)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(21)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.gridLayout_8.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_9.addWidget(self.pushButton_9, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_11.setAcceptDrops(False)
        self.pushButton_11.setToolTip("")
        self.pushButton_11.setWhatsThis("")
        self.pushButton_11.setAccessibleName("")
        self.pushButton_11.setAccessibleDescription("")
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_9.addWidget(self.pushButton_11, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 2, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(171, 140))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(87)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(21)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(19)
        self.gridLayout_9.addWidget(self.tableWidget_2, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 0, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_10.addWidget(self.pushButton_14, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 0, 2, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_3.setMinimumSize(QtCore.QSize(263, 140))
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_10.addWidget(self.listWidget_3, 1, 0, 1, 3)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_7.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_7, 0, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(514, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 1, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_14.addWidget(self.textEdit_2, 0, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_14.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_14.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_15.addWidget(self.textEdit_3, 0, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem5, 1, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_15.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_15.addWidget(self.pushButton_13, 1, 1, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_10)
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_17.addWidget(self.textEdit_4, 0, 0, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem6, 1, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_17.addWidget(self.pushButton_15, 1, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_17.addWidget(self.pushButton_16, 1, 1, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        #---------------------------------------------------------------------yeni tab başlangıç
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_4")
        self.gridLayout_68 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.groupBox_60 = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox_60.setObjectName("groupBox_60")
        self.gridLayout_67 = QtWidgets.QGridLayout(self.groupBox_60)
        self.gridLayout_67.setObjectName("gridLayout_67")
        self.textEdit_64 = QtWidgets.QTextEdit(self.groupBox_60)
        self.textEdit_64.setObjectName("textEdit_64")
        self.gridLayout_67.addWidget(self.textEdit_64, 0, 0, 1, 3)
        spacerItem66 = QtWidgets.QSpacerItem(784, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_67.addItem(spacerItem66, 1, 0, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.groupBox_60)
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_65.setText("Ekle")
        self.gridLayout_67.addWidget(self.pushButton_65, 1, 2, 1, 1)
        self.pushButton_66 = QtWidgets.QPushButton(self.groupBox_60)
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_66.setText("Güncelle")
        self.gridLayout_67.addWidget(self.pushButton_66, 1, 1, 1, 1)
        self.gridLayout_68.addWidget(self.groupBox_60, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.frame = QtWidgets.QFrame(self.tab_5)
        self.frame.setMinimumSize(QtCore.QSize(800, 500))
        self.frame.setMaximumSize(QtCore.QSize(11024, 1200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")

        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tableWidgetd_ = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetd_.setMinimumSize(QtCore.QSize(1800, 300))
        self.tableWidgetd_.setMaximumSize(QtCore.QSize(19024, 500))
        self.tableWidgetd_.setObjectName("tableWidgetd_")
        self.tableWidgetd_.setColumnCount(2)
        self.tableWidgetd_.setRowCount(0)
        self.tableWidgetd_.setAlternatingRowColors(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetd_.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetd_.setHorizontalHeaderItem(1, item)
        self.gridLayout_8.addWidget(self.tableWidgetd_, 0, 0, 1, 1)


        self.groupBoxd_1 = QtWidgets.QGroupBox(self.frame)
        self.groupBoxd_1.setMinimumSize(QtCore.QSize(1600, 110))
        self.groupBoxd_1.setMaximumSize(QtCore.QSize(1600, 110))
        self.groupBoxd_1.setObjectName("groupBoxd_1")
        self.pushButtond_1 = QtWidgets.QPushButton(self.groupBoxd_1)
        self.pushButtond_1.setGeometry(QtCore.QRect(10, 20, 64, 64))
        self.pushButtond_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/application-vnd.ms-excel.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtond_1.setIcon(icon4)
        self.pushButtond_1.setIconSize(QtCore.QSize(55, 55))
        self.pushButtond_1.setObjectName("pushButtond_1")
        self.pushButtond_2 = QtWidgets.QPushButton(self.groupBoxd_1)
        self.pushButtond_2.setGeometry(QtCore.QRect(80, 20, 64, 64))
        self.pushButtond_2.setText("")
        self.pushButtond_2.setIcon(icon4)
        self.pushButtond_2.setIconSize(QtCore.QSize(55, 55))
        self.pushButtond_2.setObjectName("pushButtond_2")
        self.pushButtond_3 = QtWidgets.QPushButton(self.groupBoxd_1)
        self.pushButtond_3.setGeometry(QtCore.QRect(150, 20, 64, 64))
        self.pushButtond_3.setText("")
        self.pushButtond_3.setIcon(icon4)
        self.pushButtond_3.setIconSize(QtCore.QSize(55, 55))
        self.pushButtond_3.setObjectName("pushButtond_3")
        self.labeld_1 = QtWidgets.QLabel(self.groupBoxd_1)
        self.labeld_1.setGeometry(QtCore.QRect(30, 90, 41, 16))
        self.labeld_1.setObjectName("labeld_1")
        self.labeld_2 = QtWidgets.QLabel(self.groupBoxd_1)
        self.labeld_2.setGeometry(QtCore.QRect(100, 90, 41, 16))
        self.labeld_2.setObjectName("labeld_2")
        self.labeld_3 = QtWidgets.QLabel(self.groupBoxd_1)
        self.labeld_3.setGeometry(QtCore.QRect(163, 90, 41, 16))
        self.labeld_3.setObjectName("labeld_3")
        self.gridLayout_8.addWidget(self.groupBoxd_1, 1, 0, 1, 1)

        self.groupBoxd_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBoxd_2.setObjectName("groupBoxd_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBoxd_2)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.pushButtond_4 = QtWidgets.QPushButton(self.groupBoxd_2)
        self.pushButtond_4.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButtond_4.setMaximumSize(QtCore.QSize(1200, 300))
        self.pushButtond_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/application-msword.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButtond_4.setIcon(icon2)
        self.pushButtond_4.setIconSize(QtCore.QSize(90, 90))
        self.pushButtond_4.setObjectName("pushButtond_4")
        self.gridLayout_7.addWidget(self.pushButtond_4, 0, 3, 1, 1)
        self.lineEdit_rap = QtWidgets.QLineEdit(self.groupBoxd_2)
        self.lineEdit_rap.setMinimumSize(QtCore.QSize(202, 20))
        self.lineEdit_rap.setMaximumSize(QtCore.QSize(210, 20))
        self.lineEdit_rap.setObjectName("lineEdit_rap")
        self.gridLayout_7.addWidget(self.lineEdit_rap, 0, 1, 1, 1)
        self.label_rap = QtWidgets.QLabel(self.groupBoxd_2)
        self.label_rap.setObjectName("label_rap")
        self.label_rap.setText("Uzlaştırma Raporunun Hazırlandığı Yer")
        self.gridLayout_7.addWidget(self.label_rap, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.groupBoxd_2, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 3)

        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        #-----------------------------Son Tab

        #----------------------------------------------------------------------yeni tab bitiş
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        self.menuUzla_t_rma_Dosyas = QtWidgets.QMenu(self.menubar)
        self.menuUzla_t_rma_Dosyas.setObjectName("menuUzla_t_rma_Dosyas")
        self.menuUzla_mac = QtWidgets.QMenu(self.menubar)
        self.menuUzla_mac.setObjectName("menuUzla_mac")
        self.menu_ablonlar = QtWidgets.QMenu(self.menubar)
        self.menu_ablonlar.setObjectName("menu_ablonlar")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/list-add.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionDosya_ekle = QtWidgets.QAction(MainWindow)
        self.actionDosya_ekle.setObjectName("actionDosya_ekle")
        self.actionDosya_ekle.setIcon(icon)
        self.actionDosya_Sil = QtWidgets.QAction(MainWindow)
        self.actionDosya_Sil.setObjectName("actionDosya_Sil")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/list-remove.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionDosya_Sil.setIcon(icon)
        self.actionUzla_mac_Ekle = QtWidgets.QAction(MainWindow)
        self.actionUzla_mac_Ekle.setObjectName("actionUzla_mac_Ekle")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/credentials-preferences.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionUzla_mac_Ekle.setIcon(icon)
        self.actionUzla_mac_Sil = QtWidgets.QAction(MainWindow)
        self.actionUzla_mac_Sil.setObjectName("actionUzla_mac_Sil")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/user-trash.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionUzla_mac_Sil.setIcon(icon)
        self.actionAblon_Ekle = QtWidgets.QAction(MainWindow)
        self.actionAblon_Ekle.setObjectName("actionAblon_Ekle")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/accessories-text-editor.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionAblon_Ekle.setIcon(icon)
        self.action_ablon_D_zenle = QtWidgets.QAction(MainWindow)
        self.action_ablon_D_zenle.setObjectName("action_ablon_D_zenle")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/logviewer.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.action_ablon_D_zenle.setIcon(icon)
        self.actionProgram_Ayarlar = QtWidgets.QAction(MainWindow)
        self.actionProgram_Ayarlar.setObjectName("actionProgram_Ayarlar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lib/icon/application-default-icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.actionProgram_Ayarlar.setIcon(icon)
        self.menuUzla_t_rma_Dosyas.addAction(self.actionDosya_ekle)
        self.menuUzla_t_rma_Dosyas.addAction(self.actionDosya_Sil)
        self.menuUzla_mac.addAction(self.actionUzla_mac_Ekle)
        self.menuUzla_mac.addAction(self.actionUzla_mac_Sil)
        self.menu_ablonlar.addAction(self.actionAblon_Ekle)
        self.menu_ablonlar.addAction(self.action_ablon_D_zenle)

        self.menuAyarlar.addAction(self.actionProgram_Ayarlar)
        self.menubar.addAction(self.menuUzla_t_rma_Dosyas.menuAction())
        self.menubar.addAction(self.menuUzla_mac.menuAction())
        self.menubar.addAction(self.menu_ablonlar.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())
        #Tablo Sekme Büyüklükleri
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidgetd_.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetd_.horizontalHeader().setStretchLastSection(True)

        self.comboBox_2.setDisabled(True)
        self.triggerfinger()
        self.dosya_tara("1")

        #-----------------------------------------Olay - Görüşme - Edim - Başarısızlık Buton Ayarları

        # Olay Özeti
        #textedit
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)

        #Görüşme
        #textedit_2
        self.pushButton_7.setDisabled(True)
        self.pushButton_8.setDisabled(True)

        #Edim
        #textedit_3
        self.pushButton_10.setDisabled(True)
        self.pushButton_13.setDisabled(True)

        #Başarıszlık
        #TextEdit_4
        self.pushButton_15.setDisabled(True)
        self.pushButton_16.setDisabled(True)

        # Sonuç
        self.pushButton_65.setDisabled(True)
        self.pushButton_66.setDisabled(True)

        self.ayarlar()

        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_14.setDisabled(True)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate  # type: Callable[[Any, Any, Any, int], str]
        MainWindow.setWindowTitle(_translate("MainWindow", "Uzlaştırma"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dosya Bilgileri"))
        self.label.setText(_translate("MainWindow", "Dosya Durumu"))
        self.radioButton.setText(_translate("MainWindow", "Aktif"))
        self.radioButton_2.setText(_translate("MainWindow", "Kapanmış"))
        self.label_2.setText(_translate("MainWindow", "Uzlaşma No"))
        self.label_3.setText(_translate("MainWindow", "Soruşturma No"))
        self.label_4.setText(_translate("MainWindow", "M. Esas No"))
        self.label_5.setText(_translate("MainWindow", "Suç"))
        self.label_6.setText(_translate("MainWindow", "Tevdi Tarihi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Dökümana çevir"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dosya durumu"))
        self.label_11.setText(_translate("MainWindow", "Teslim Tarihine"))
        self.label_12.setText(_translate("MainWindow", "x"))
        self.label_13.setText(_translate("MainWindow", "gün var."))
        self.lineEdit.setText(_translate("MainWindow", "Uzatma Tarihi Ekle"))
        self.pushButton_3.setText(_translate("MainWindow", "Ekle"))
        self.label_16.setText(_translate("MainWindow", "Dosya Durumu"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dosya Seç"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Aktif"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Kapat"))
        self.groupBox.setTitle(_translate("MainWindow", "Uzlaştırmacı"))
        self.label_14.setText(_translate("MainWindow", "Uzlaştırmacı"))

        self.label_18.setText(_translate("MainWindow", "Sicil No"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Taraflar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad Soyad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sıfat"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Dosya Giderleri"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Harcama"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tutar"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Ek Dosyalar"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.groupBox_7.setTitle(_translate("MainWindow", "Dava Konusu Olay"))

        self.pushButton_2.setText(_translate("MainWindow", "Güncelle"))
        self.pushButton.setText(_translate("MainWindow", "Ekle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dosya Bilgileri"))
        self.groupBox_8.setTitle(_translate("MainWindow", "GroupBox"))

        self.pushButton_7.setText(_translate("MainWindow", "Ekle"))
        self.pushButton_8.setText(_translate("MainWindow", "Güncelle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Uzlaşma Görüşmeleri"))
        self.groupBox_9.setTitle(_translate("MainWindow", "GroupBox"))
        
        #Edim butonları
        self.pushButton_10.setText(_translate("MainWindow", "Ekle"))
        self.pushButton_13.setText(_translate("MainWindow", "Güncelle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Edim"))
        self.groupBox_10.setTitle(_translate("MainWindow", "GroupBox"))
        
        #başarısızlık butonları
        self.pushButton_15.setText(_translate("MainWindow", "Ekle"))
        self.pushButton_16.setText(_translate("MainWindow", "Güncelle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Uzlaşma Başarısızlık Sebebleri"))
        self.menuUzla_t_rma_Dosyas.setTitle(_translate("MainWindow", "Uzlaştırma Dosyası"))
        self.menuUzla_mac.setTitle(_translate("MainWindow", "Uzlaşmacı"))
        self.menu_ablonlar.setTitle(_translate("MainWindow", "Şablonlar"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.actionDosya_ekle.setText(_translate("MainWindow", "Dosya Ekle"))
        self.actionDosya_Sil.setText(_translate("MainWindow", "Dosya Sil"))
        self.actionUzla_mac_Ekle.setText(_translate("MainWindow", "Uzlaşmacı Ekle"))
        self.actionUzla_mac_Sil.setText(_translate("MainWindow", "Uzlaşmacı Sil"))
        self.actionAblon_Ekle.setText(_translate("MainWindow", "Şablon Ekle"))
        self.action_ablon_D_zenle.setText(_translate("MainWindow", "Şablon Düzenle"))
        self.actionProgram_Ayarlar.setText(_translate("MainWindow", "Program Ayarları"))

        item = self.tableWidgetd_.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "AD"))
        item = self.tableWidgetd_.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NİTELİK"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Uzlaştırma Sonuçları"))

        self.labeld_1.setText(_translate("MainWindow", "Davet"))
        self.labeld_2.setText(_translate("MainWindow", "Teklif"))
        self.labeld_3.setText(_translate("MainWindow", "Tebligat"))
        self.groupBoxd_2.setTitle(_translate("MainWindow", "Rapor hazırla"))
        self.groupBoxd_1.hide()

    def triggerfinger(self):
        self.actionUzla_mac_Ekle.triggered.connect(uih.gui_uzlastirmaci_ekle)
        self.actionUzla_mac_Sil.triggered.connect(uih.gui_uzlastirmaci_sil)
        self.actionDosya_ekle.triggered.connect(self.gui_dosya_olustur)
        self.comboBox.currentIndexChanged.connect(self.dosya_bilgisi_cek)
        self.pushButton_4.clicked.connect(self.gui_taraf_ekle)
        self.tableWidget.cellClicked.connect(self.tablodan_parametre_olustur)
        self.tableWidget_2.cellClicked.connect(self.gider_tablosundan_parametre_olustur)
        self.pushButton_5.clicked.connect(self.taraf_duzenlemeyi_bagla)
        self.pushButton_6.clicked.connect(self.taraf_sil)
        self.pushButton_9.clicked.connect(self.gui_gider_bagla)
        self.pushButton_11.clicked.connect(self.gider_sil)
        self.pushButton_12.clicked.connect(self.gui_ek_bagla)
        self.listWidget_3.clicked.connect(self.ek_listesinden_parametre_olustur)
        self.pushButton_14.clicked.connect(self.ek_sil)
        self.radioButton.clicked.connect(self.dosya_kimlik)
        self.radioButton_2.clicked.connect(self.dosya_kimlik)
        self.pushButton_3.clicked.connect(self.uzatmaEkle)
        self.comboBox_2.activated.connect(self.dosya_kapat)
        self.pushButton.clicked.connect(self.olay_ekle)
        self.pushButton_2.clicked.connect(self.olay_guncelle)
        self.pushButton_7.clicked.connect(self.gorusme_ekle)
        self.pushButton_8.clicked.connect(self.gorusme_guncelle)
        self.pushButton_10.clicked.connect(self.edim_ekle)
        self.pushButton_13.clicked.connect(self.edim_guncelle)
        self.pushButton_15.clicked.connect(self.uzbas_ekle)
        self.pushButton_16.clicked.connect(self.uzbas_guncelle)
        self.pushButton_65.clicked.connect(self.sonuc_ekle)
        self.pushButton_66.clicked.connect(self.sonuc_guncelle)
        self.actionDosya_Sil.triggered.connect(self.gui_dosya_sil)
        self.tableWidgetd_.cellClicked.connect(self.dosya_icin_parametre_olustur)
        self.actionProgram_Ayarlar.triggered.connect(uih.gui_settings)
        #dosya oluşturma tetiklemeleri
        self.pushButtond_1.clicked.connect(self.davet)
        self.pushButtond_2.clicked.connect(self.teklif)
        self.pushButtond_3.clicked.connect(self.tebligat)
        self.pushButtond_4.clicked.connect(self.raporla)
        #Sablon Gui bağlantıları
        self.actionAblon_Ekle.triggered.connect(uih.gui_sablonekle)
        self.action_ablon_D_zenle.triggered.connect(uih.gui_sablonsil)

    def uzlasmaci(self, arg):
        sor = mdl.tek_satirlik_demet_coz(self.veritabani.komut("select isim, sicil from uzlasmaci where isim = '{}'".format(arg)))
        self.label_15.setText(sor[0])
        self.label_17.setText(sor[1])

    def ayarlar(self):
        sonuc = mdl.tek_satirlik_demet_coz(self.veritabani.komut("select * from ayarlar"))
        self.dosya_teslim_tarihi = sonuc[0]
        self.dosya_uzatma_tarihi = sonuc[1]

    def dosya_kimlik(self):
        if self.radioButton.isChecked():
            say = self.comboBox.count()
            sayac = say
            for i in range(1, say + 1):
                self.comboBox.removeItem(sayac)
                sayac -= 1
            self.comboBox.setCurrentIndex(0)
            self.comboBox_2.setCurrentIndex(0)
            self.dosya_tara("1")
        else:
            say = self.comboBox.count()
            sayac = say
            for i in range(1, say + 1):
                self.comboBox.removeItem(sayac)
                sayac -= 1
            self.comboBox.setCurrentIndex(0)
            self.dosya_tara("0")
            self.comboBox_2.setCurrentIndex(1)

    def dosya_tara(self, nit):
        sor = mdl.tekli_demet_coz(mdl.kmt("select uzno from dosyalar where durum = '{}'".format(nit)))
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i])

    #Dosya Bilgilerini listele
    def dosya_bilgisi_cek(self):
        #Eğer Dosya seçilmezse heryeri temizle
        if self.comboBox.currentIndex() == 0:
            self.comboBox_2.setDisabled(True)
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.textEdit_3.clear()
            self.textEdit_4.clear()
            self.textEdit_64.clear()
            self.label_7.clear()
            self.label_8.clear()
            self.label_9.clear()
            self.label_10.clear()
            self.label_11.hide()
            self.label_12.hide()
            self.label_13.hide()
            self.tableWidget.setRowCount(0)
            self.tableWidget_2.setRowCount(0)
            self.tableWidgetd_.setRowCount(0)

        else:
            dosya = self.comboBox.currentText()
            so = mdl.tek_satirlik_demet_coz(mdl.dosya_cek(dosya))
            self.label_7.setText(so[2])
            self.label_8.setText(so[3])
            self.label_9.setText(so[4])
            self.label_10.setText(so[5])
            self.label_11.show()
            self.label_12.show()
            self.label_13.show()
            self.comboBox_2.setDisabled(False)

            self.dosya_durumu()
            self.taraf_bul(dosya)
            self.taraf_bul_evrak(dosya)
            self.gider_bul(dosya)
            self.ek_bul(dosya)
            #self.dosya_taraf_bul(dosya)
            self.uzlasmaci(so[-1])

            ozet = mdl.olay_ozeti_cek(dosya)
            gorusme = mdl.gorusme_cek(dosya)
            edim = mdl.edim_cek(dosya)
            uzba = mdl.uzbas_cek(dosya)
            sonuc = mdl.sonuc_cek(dosya)
            self.textEdit.clear()
            self.textEdit_2.clear()
            self.textEdit_3.clear()
            self.textEdit_4.clear()
            self.textEdit_64.clear()
            self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
            self.dosya_durumu()

            if len(ozet) == 0:
                self.pushButton.setDisabled(False)
            else:
                self.textEdit.setPlainText(ozet[0][0])
                self.pushButton_2.setDisabled(False)

            if len(gorusme) == 0:
                self.pushButton_7.setDisabled(False)
            else:
                self.pushButton_8.setDisabled(False)
                self.textEdit_2.setPlainText(gorusme[0][0])

            if len(edim) == 0:
                self.pushButton_10.setDisabled(False)
            else:
                self.pushButton_13.setDisabled(False)
                self.textEdit_3.setPlainText(edim[0][0])

            if len(uzba) == 0:
                self.pushButton_15.setDisabled(False)
            else:
                self.pushButton_16.setDisabled(False)
                self.textEdit_4.setPlainText(uzba[0][0])

            if len(sonuc) == 0:
                self.pushButton_65.setDisabled(False)
            else:
                self.pushButton_66.setDisabled(False)
                self.textEdit_64.setPlainText(sonuc[0][0])

    #Uzlaşma dosyasının ne durumda olduğunu göster
    def dosya_durumu(self):
        sonuc = self.veritabani.komut("select uzatmatar from dosyalar where uzno = '{}'"
                                      .format(self.comboBox.currentText()))
        ptr = mdl.tarih_duzenle(sonuc[0][0])
        dtr = ptr.split()
        if ptr == False:
            self.label_11.hide()
            self.label_12.hide()
            self.label_13.hide()
            self.label_7.clear()
            self.label_8.clear()
            self.label_9.clear()
            self.label_10.clear()
        else:
            self.label_12.setText(dtr[0])
            if int(dtr[0]) > 5:
                pass
            else:
                self.label_12.setStyleSheet("color: rgb(255, 0, 0);")

    def taraf_bul(self, ar):
        sql = """SELECT ad, sifat FROM taraflar WHERE dosya == '{0}' 
        union SELECT ad, sifat FROM temsilciler WHERE dosya == '{0}' 
        union SELECT ad, sifat FROM tercuman WHERE dosya == '{0}'""".format(ar)
        sonuc = mdl.kmt(sql)
        self.tableWidget.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

        tablo_satir = self.tableWidget.rowCount()

        for i in range(tablo_satir):
            satir_d = self.tableWidget.item(i, 1)

            if satir_d.text() == "1":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Mağdur / Katılan"))
            elif satir_d.text() == "2":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Mağdur / Katılan'ın Temsilcisi"))
            elif satir_d.text() == "3":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Suçtan Zarar Gören"))
            elif satir_d.text() == "4":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Suçtan Zarar Görenin Temsilcisi"))
            elif satir_d.text() == "5":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Şüpheli / Sanık"))
            elif satir_d.text() == "6":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Şüpheli Sanık Temsilcisi"))
            elif satir_d.text() == "7":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Müşteki Şüpheli"))
            elif satir_d.text() == "8":
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("Müşteki Şüpheli Temsilcisi"))
            else:
                pass
    
    def taraf_bul_evrak(self, ar):
        sql = """SELECT ad, sifat FROM taraflar WHERE dosya == '{0}' 
        union SELECT ad, sifat FROM temsilciler WHERE dosya == '{0}'""".format(ar)
        sonuc = mdl.kmt(sql)
        self.tableWidgetd_.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidgetd_.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1
        tablo_satir = self.tableWidgetd_.rowCount()
        for i in range(tablo_satir):
            satir_d = self.tableWidgetd_.item(i, 1)
            if satir_d.text() == "1":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Mağdur / Katılan"))
            elif satir_d.text() == "2":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Mağdur / Katılan'ın Temsilcisi"))
            elif satir_d.text() == "3":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Suçtan Zarar Gören"))
            elif satir_d.text() == "4":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Suçtan Zarar Görenin Temsilcisi"))
            elif satir_d.text() == "5":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Şüpheli / Sanık"))
            elif satir_d.text() == "6":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Şüpheli Sanık Temsilcisi"))
            elif satir_d.text() == "7":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Müşteki Şüpheli"))
            elif satir_d.text() == "8":
                self.tableWidgetd_.setItem(i, 1, QtWidgets.QTableWidgetItem("Müşteki Şüpheli Temsilcisi"))
            else:
                pass

    def gider_bul(self, dosya):
        sql = """SELECT aciklama, tutar FROM giderler WHERE dosya == '{}'""".format(dosya)
        sonuc = mdl.kmt(sql)
        self.tableWidget_2.setRowCount(len(sonuc))
        satir = 0
        sutun = 0
        for i in range(len(sonuc)):
            for im in range(len(sonuc[i])):
                self.tableWidget_2.setItem(satir, sutun, QtWidgets.QTableWidgetItem("{}".format(sonuc[i][im])))
                sutun += 1
            sutun = 0
            satir += 1

    def ek_bul(self, dosya):
        self.listWidget_3.clear()
        sql = """SELECT ad FROM ek WHERE dosya == '{}'""".format(dosya)
        sonuc = mdl.kmt(sql)
        for i in range(len(sonuc)):
            self.listWidget_3.addItem(sonuc[i][0])

    #Taraflar tablosu tetiklemesi.................................................TABLO CLİCK TETİKLEMELERİ.........
    def tablodan_parametre_olustur(self, row, column):
        oge_ad = self.tableWidget.item(row, 0)
        oge_nitelik = self.tableWidget.item(row, 1)
        if oge_nitelik.text() == "Vekil":
            self.kisi_nitelik_duzenle = "Vekil"
        elif oge_nitelik.text() == "Müdafi":
            self.kisi_nitelik_duzenle = "Vekil"
        elif oge_nitelik.text() == "Tercüman":
            self.kisi_nitelik_duzenle = "Tercüman"
        else:
            self.kisi_nitelik_duzenle = "Şahıs"
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.kisi_duzenle = oge_ad.text()

    def dosya_icin_parametre_olustur(self, row, column):
        oge_ad = self.tableWidgetd_.item(row, 0)
        oge_nitelik = self.tableWidgetd_.item(row, 1)
        self.dosya_kisi_ad = oge_ad.text()
        self.dosya_kisi_nitelik = oge_nitelik.text()
        self.groupBoxd_1.show()
        self.groupBoxd_1.setTitle(self.dosya_kisi_ad)
        if oge_nitelik.text() == "Vekil":
            pass
        else:
            pass

    def gider_tablosundan_parametre_olustur(self, row, column):
        gider_ad = self.tableWidget_2.item(row, column)
        self.pushButton_11.setDisabled(False)
        self.secilen_gider = gider_ad.text()

    def ek_listesinden_parametre_olustur(self):
        self.ek_dosya = self.listWidget_3.currentItem().text()
        self.pushButton_14.setDisabled(False)

    #..........................................................................................DİALOGLARI BAĞLA
    def taraf_duzenlemeyi_bagla(self):
        self.gui_taraf_duzenle(self.kisi_duzenle, self.kisi_nitelik_duzenle)

    # Dosya no sunu Gui oluşturma fonksiyonuna parametre olarak gönder
    def gui_gider_bagla(self):
        self.gui_gider(self.comboBox.currentText())

    def gui_ek_bagla(self):
        self.gui_ek(self.comboBox.currentText())
    #................................................................................SİLME FONKSİYONLARI...........
    def taraf_sil(self):
        if self.kisi_nitelik_duzenle == "Şahıs":
            if kayit_sil_soru(self.kisi_duzenle) == True:
                sql = "select id from taraflar where dosya = '{}' and ad = '{}'".format(self.comboBox.currentText(), self.kisi_duzenle)
                mdl.silinecek_veri_bul(sql, "taraflar")
                baslik = "Bilgi Silme Uyarısı"
                mesaj = self.kisi_duzenle + " kişisinin bilgileri veritabanından silindi"
                bilgilendir(mesaj, baslik)
                self.taraf_bul(self.comboBox.currentText())
                self.taraf_bul_evrak(self.comboBox.currentText())
            else:
                baslik = "Bilgi Silme İptali"
                mesaj = self.kisi_duzenle + " Veri silme işlemi iptal edildi"
                bilgilendir(mesaj, baslik)
        elif self.kisi_nitelik_duzenle == "Vekil":
            if kayit_sil_soru(self.kisi_duzenle) == True:
                sql = "select id from temsilciler where dosya = '{}' and ad = '{}'".format(self.comboBox.currentText(), self.kisi_duzenle)
                mdl.silinecek_veri_bul(sql, "temsilciler")
                baslik = "Bilgi Silme Uyarısı"
                mesaj = self.kisi_duzenle + " kişisinin bilgileri veritabanından silindi"
                bilgilendir(mesaj, baslik)
                self.taraf_bul(self.comboBox.currentText())
                self.taraf_bul_evrak(self.comboBox.currentText())
            else:
                baslik = "Bilgi Silme İptali"
                mesaj = self.kisi_duzenle + " Veri silme işlemi iptal edildi"
                bilgilendir(mesaj, baslik)
        else:
            if kayit_sil_soru(self.kisi_duzenle) == True:
                sql = "select id from tercuman where dosya = '{}' and ad = '{}'".format(self.comboBox.currentText(), self.kisi_duzenle)
                mdl.silinecek_veri_bul(sql, "tercuman")
                baslik = "Bilgi Silme Uyarısı"
                mesaj = self.kisi_duzenle + " kişisinin bilgileri veritabanından silindi"
                bilgilendir(mesaj, baslik)
                self.taraf_bul(self.comboBox.currentText())
            else:
                baslik = "Bilgi Silme İptali"
                mesaj = self.kisi_duzenle + " Veri silme işlemi iptal edildi"
                bilgilendir(mesaj, baslik)

    def gider_sil(self):
        if gider_sil_soru(self.secilen_gider) == True:
            sql = "select id from giderler where dosya = '{}' and aciklama = '{}'".format(self.comboBox.currentText(),
                                                                                    self.secilen_gider)
            mdl.silinecek_gider_bul(sql)
            baslik = "Bilgi Silme Uyarısı"
            mesaj = self.secilen_gider + " harcamasının bilgileri veritabanından silindi"
            bilgilendir(mesaj, baslik)
            self.gider_bul(self.comboBox.currentText())
        else:
            baslik = "Bilgi Silme İptali"
            mesaj = self.secilen_gider + " harcamasının silme işlemi iptal edildi"
            bilgilendir(mesaj, baslik)

    def ek_sil(self):
        if ek_sil_soru(self.ek_dosya) == True:
            sql = "select id from ek where dosya = '{}' and ad = '{}'".format(self.comboBox.currentText(),
                                                                                    self.ek_dosya)
            mdl.silinecek_ek_bul(sql)
            baslik = "Bilgi Silme Uyarısı"
            mesaj = self.ek_dosya + " Ek adı veritabanından silindi"
            bilgilendir(mesaj, baslik)
            self.listWidget_3.clear()
            self.ek_bul(self.comboBox.currentText())
        else:
            baslik = "Bilgi Silme İptali"
            mesaj = self.ek_dosya + "Ek adının silme işlemi iptal edildi"
            bilgilendir(mesaj, baslik)

    def uzatmaEkle(self):
        dosya = self.comboBox.currentText()
        uzatma_kontrol = self.veritabani.komut("select * from uzatma where dosya = '{}'".format(dosya))
        if len(uzatma_kontrol) == 0:
            yeni_tarih = self.lineEdit.text()
            yaz = self.veritabani.yapistir("Insert Into uzatma Values(Null, '{}', '{}')".format(yeni_tarih, dosya))
            if yaz == True:
                baslik = "Ek Süre Ekleme"
                mesaj = "Dosya Bilgilerine {} tarihi eklendi.".format(yeni_tarih)
                bilgilendir(mesaj, baslik)
                self.lineEdit.clear()
            else:
                baslik = "Ek Süre Ekleme Hatası"
                mesaj = "Dosya Bilgilerine ek süre tarihi eklenemedi"
                bilgilendir(mesaj, baslik)

            sure = self.veritabani.komut("select uzatma_suresi from ayarlar")
            t = yeni_tarih.replace(".", "/")
            formatstr = '%d/%m/%Y'
            t3 = datetime.datetime.strptime(t, formatstr)

            fark = datetime.timedelta(days=int(sure[0][0]))
            gelecek = t3 + fark
            uzatmatar = gelecek.date()

            self.veritabani.yapistir("UPDATE dosyalar SET uzatmatar = "
                                     "'{}' where uzno = '{}'".format(uzatmatar, self.comboBox.currentText()))
            self.dosya_durumu()
        else:
            baslik = "Ek Süre Tanımlama Hatası"
            mesaj = "Bu dosyaya daha önceden ek süre alınmıştır."
            bilgilendir(mesaj, baslik)

    def olay_ekle(self):
        yazi = self.textEdit.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle olay eklenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Olayı özetleyen bir yazı yazmanız gerekmektedir."
                baslik = "Olay Özet Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("insert into olaylar values(NULL, '{}', '{}')"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Olayı özeti dosya bilgilerine eklendi"
                baslik = "Olay Özet'i Eklemesi"
                bilgilendir(mesaj, baslik)
                self.pushButton.setDisabled(True)
                self.pushButton_2.setDisabled(False)

    def olay_guncelle(self):
        yazi = self.textEdit.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle olay eklenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Veritabanı yazma hatasından kaynaklı olay özeti güncellenemedi."
                baslik = "Özet Güncelleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("update olaylar set ozet='{}' where uzno = '{}'"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Olayı özeti başarıyla güncellendi"
                baslik = "Özet Güncellemesi"
                bilgilendir(mesaj, baslik)

    def gorusme_ekle(self):
        yazi = self.textEdit_2.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Lütfen görüşme eklemeke istediğiniz dosyayı seçiniz.Herhangi bir dosya seçilmemiş"
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Yazı editörünü boş bırakamazsınız."
                baslik = "Görüşme Ekleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("insert into uzgor values(NULL, '{}', '{}')"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Görüşme durumu dosya bilgilerine eklendi"
                baslik = "Uzlaşma Görüşmeleri"
                bilgilendir(mesaj, baslik)
                self.pushButton_7.setDisabled(True)
                self.pushButton_8.setDisabled(False)

    def gorusme_guncelle(self):
        yazi = self.textEdit_2.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle güncellenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Veritabanı yazma hatasından kaynaklı olay özeti güncellenemedi."
                baslik = "Özet Güncelleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("update uzgor set gorusme='{}' where dosya = '{}'"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Olayı özeti başarıyla güncellendi"
                baslik = "Özet Güncellemesi"
                bilgilendir(mesaj, baslik)

    def edim_ekle(self):
        yazi = self.textEdit_3.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Lütfen Edim eklemek istediğiniz dosyayı seçiniz.Herhangi bir dosya seçilmemiş"
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Yazı editörünü boş bırakamazsınız."
                baslik = "Edim Ekleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("insert into edim values(NULL, '{}', '{}')"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Dosya Edim'i bilgilerine eklendi"
                baslik = "Edim Ekleme"
                bilgilendir(mesaj, baslik)
                self.pushButton_10.setDisabled(True)
                self.pushButton_13.setDisabled(False)

    def edim_guncelle(self):
        yazi = self.textEdit_3.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle güncellenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Veritabanı yazma hatasından kaynaklı edim güncellenemedi."
                baslik = "Edim Güncelleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("update edim set edi='{}' where dosya = '{}'"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Edim başarıyla güncellendi"
                baslik = "Edim Güncellemesi"
                bilgilendir(mesaj, baslik)

    def uzbas_ekle(self):
        yazi = self.textEdit_4.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Lütfen Olumsuzluk  sebebi eklemek istediğiniz dosyayı seçiniz.Herhangi bir dosya seçilmemiş"
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Yazı editörünü boş bırakamazsınız."
                baslik = "Ekleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("insert into uzbas values(NULL, '{}', '{}')"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Uzlaşma Başarısızlıkları dosya bilgilerine eklendi"
                baslik = "Uzlaşma Başarısızlık Ekleme"
                bilgilendir(mesaj, baslik)
                self.pushButton_15.setDisabled(True)
                self.pushButton_16.setDisabled(False)

    def uzbas_guncelle(self):
        yazi = self.textEdit_4.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle güncellenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Veritabanı yazma hatasından kaynaklı yazı güncellenemedi."
                baslik = "Veri Güncelleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("update uzbas set sebeb='{}' where dosya = '{}'"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Veri başarıyla güncellendi"
                baslik = "Veri Güncellemesi"
                bilgilendir(mesaj, baslik)
    def sonuc_ekle(self):
        yazi = self.textEdit_64.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Lütfen uzlaştırma sonucu eklemek istediğiniz dosyayı seçiniz.Herhangi bir dosya seçilmemiş"
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Yazı editörünü boş bırakamazsınız."
                baslik = "Ekleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("insert into sonuc values(NULL, '{}', '{}')"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Uzlaşma sonuçları dosya bilgilerine eklendi"
                baslik = "Uzlaşma Sonuç Ekleme"
                bilgilendir(mesaj, baslik)
                self.pushButton_65.setDisabled(True)
                self.pushButton_66.setDisabled(False)
    def sonuc_guncelle(self):
        yazi = self.textEdit_64.toPlainText()
        if self.comboBox.currentIndex() == 0:
            mesaj = "Öncelikle güncellenecek bir uzlaştırma dosyası seçmeniz gerekmektedir."
            baslik = "Dosya Seçim Hatası"
            bilgilendir(mesaj, baslik)
        else:
            if len(yazi) == 0:
                mesaj = "Veritabanı yazma hatasından kaynaklı yazı güncellenemedi."
                baslik = "Veri Güncelleme Hatası"
                bilgilendir(mesaj, baslik)
            else:
                self.veritabani.yapistir("update sonuc set metin='{}' where dosya = '{}'"
                                         .format(yazi, self.comboBox.currentText()))
                mesaj = "Veri başarıyla güncellendi"
                baslik = "Veri Güncellemesi"
                bilgilendir(mesaj, baslik)

    def dosya_kapat(self):
        if self.radioButton.isChecked() and self.comboBox_2.currentIndex() == 1:
            if dosya_kapat_soru(self.comboBox.currentText()) == True:
                if self.veritabani.yapistir("update dosyalar set durum='{}' where uzno='{}'"
                                               .format(0, self.comboBox.currentText())) == True:
                    bilgilendir("Dosya başarı ile kapatıldı", "Dosya Kapatma Uyarısı")
                    self.dosya_kimlik()
                else:
                    pass
            else:
                bilgilendir("Dosya Kapatma işlemi iptal edildi", "Dosya Kapatma Uyarısı")
                self.comboBox_2.setCurrentIndex(0)
        elif self.radioButton_2.isChecked() and self.comboBox_2.currentIndex() == 0:
            if dosya_ac_soru(self.comboBox.currentText()) == True:
                if self.veritabani.yapistir("update dosyalar set durum='{}' where uzno='{}'"
                                               .format(1, self.comboBox.currentText())) == True:
                    bilgilendir("Dosya başarı ile açıldı", "Dosya Açma Uyarısı")
                    self.dosya_kimlik()
                else:
                    pass
            else:
                bilgilendir("Dosya Açma işlemi iptal edildi", "Dosya Açma Uyarısı")
                self.comboBox_2.setCurrentIndex(1)
        else:
            pass
    #----------------------------------------------------------------------Dosya oluşturma fonksiyonları
    def davet(self):
        sorno = self.comboBox.currentText()
        ad = self.groupBoxd_1.title()
        durum = None
        veksicil = None
        tc = None
        if self.dosya_kisi_nitelik == "Vekil":
            sonuc = self.veritabani.komut("select ttarihi, sicil from temsilciler where ad = '{}' and dosya = '{}'".format(ad,
                                                                                                                     sorno))
            veksicil = sonuc[0][1]
            durum = 0
        else:
            sonuc = self.veritabani.komut("select ttarihi, tc from taraflar where ad = '{}' and dosya = '{}'".format(ad,
                                                                                                                     sorno))
            tc = sonuc[0][1]
            durum = 1

        ttarihi = sonuc[0][0]
        tc = sonuc[0][1]
        uz = self.label_15.text()
        uzsicil = self.label_17.text()
        uztel = self.veritabani.komut("select tel from uzlasmaci where isim='{}' and sicil='{}'".format(uz, uzsicil))
        uzte = uztel[0][0]
        if mdl.davet_yaz(durum, ad, tc, veksicil, sorno, ttarihi, uz, uzsicil, uzte) == True:
            baslik = "Davet Mektubu"
            mesaj = ad + " kişisine ait davet mektubu başarıyla oluşturuldu"
            bilgilendir(mesaj, baslik)
        else:
            baslik = "Dosya Oluşturma Hatası"
            mesaj = ad + " kişisine ait Davet Mektubu oluşturulamadı"
            bilgilendir(mesaj, baslik)

    def teklif(self):
        sorno = self.comboBox.currentText()
        ad = self.groupBoxd_1.title()
        uz = self.label_15.text()
        uzsicil = self.label_17.text()

        if mdl.teklif_yaz(sorno, ad, uz, uzsicil) == True:
            baslik = "Teklif Formu"
            mesaj = ad + " kişisine ait Teklif Formu başarıyla oluşturuldu"
            bilgilendir(mesaj, baslik)
        else:
            baslik = "Dosya Oluşturma Hatası"
            mesaj = ad + " kişisine ait Teklif Formu oluşturulamadı"
            bilgilendir(mesaj, baslik)

    def tebligat(self):
        sorno = self.comboBox.currentText()
        ad = self.groupBoxd_1.title()

        if mdl.tebligat_yaz(sorno, ad) == True:
            baslik = "Teklif Formu"
            mesaj = ad + " kişisine ait Tebligat başarıyla oluşturuldu"
            bilgilendir(mesaj, baslik)
        else:
            baslik = "Dosya Oluşturma Hatası"
            mesaj = ad + " kişisine ait Tebligat oluşturulamadı"
            bilgilendir(mesaj, baslik)

    def raporla(self):
        if self.comboBox.currentIndex() == 0:
            baslik = "Dosya Seçme Hatası"
            mesaj ="Rapor hazırlayabilmek için öncelikle bir dosya seçmeniz gerekli"
            bilgilendir(mesaj, baslik)
            return
        else:
            pass
        
        dosya = self.comboBox.currentText()
        rapor_yeri = self.lineEdit_rap.text()
        if rapor_yeri == "":
            baslik = "Yer Hatası"
            mesaj = dosya + " No'lu dosya için lütfen Rapor Hazırlama yeri giriniz"
            bilgilendir(mesaj, baslik)
            return
        else:
            pass

        uz = self.label_15.text()
        uz_sicil = self.label_17.text()
        if mdl.rapor_yaz(dosya, uz, uz_sicil, rapor_yeri) == True:
            baslik = "Rapor Oluşturma"
            mesaj = dosya + " No'lu Uzlaşma dosyasının uzlaşma raporu oluşturuldu"
            bilgilendir(mesaj, baslik)
        else:
            baslik = "Rapor Oluşturma Hatası"
            mesaj = dosya + " No'lu Uzlaşma dosyasının uzlaşma raporu oluşturulamadı"
            bilgilendir(mesaj, baslik)

    #Dosya Eklemesinden sonra liste yenilemek için sinyal yakalama.....................SİNYAL YAKALAMA.............
    def make_connection(self, dosyaolustur_object):
        dosyaolustur_object.clicked.connect(self.get_signal_dosya)

    #Dosya'ya taraf ekleme sinyali yakalama
    def taraf_connection(self, dosyaolustur_object):
        dosyaolustur_object.clicked.connect(self.get_signal_taraf)

    # Dosya'ya Gider ekleme sinyali yakalama
    def gider_connection(self, gider_object):
        gider_object.clicked.connect(self.get_signal_gider)

    def ek_connection(self, ek_object):
        ek_object.clicked.connect(self.get_signal_ek)

    def dosya_sil_connection(self, dosyasil_object):
        dosyasil_object.clicked.connect(self.get_signal_sil)

    @pyqtSlot(bool)

    def get_signal_dosya(self, val):
        if val == False:
            say = self.comboBox.count()
            sayac = say
            for i in range(1, say + 1):
                self.comboBox.removeItem(sayac)
                sayac -= 1
            self.dosya_kimlik()
        else:
            print("Sinyal gelmedi")

    @pyqtSlot(bool)
    def get_signal_taraf(self, val):
        if val == False:
            self.taraf_bul(self.comboBox.currentText())
            self.taraf_bul_evrak(self.comboBox.currentText())
        else:
            print("Taraf Sinyali Gelmedi")

    @pyqtSlot(bool)
    def get_signal_gider(self, val):
        if val == False:
            self.gider_bul(self.comboBox.currentText())
        else:
            print("Taraf Sinyali Gelmedi")

    @pyqtSlot(bool)
    def get_signal_ek(self, val):
        if val == False:
            self.ek_bul(self.comboBox.currentText())
        else:
            print("Taraf Sinyali Gelmedi")

    @pyqtSlot(bool)
    def get_signal_sil(self, val):
        if val == False:
            self.comboBox.setCurrentIndex(0)
            self.dosya_kimlik()
        else:
            print("Sinyal Gelmedi")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

