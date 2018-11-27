# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import modul as mdl
import uihazirla as uih
from dosyaolustur import DosyaOlustur
from taraf import TarafEkle
from mico import bilgilendir, kayit_sil_soru
from tarafduzenle import TarafDuzenle

class Ui_MainWindow(object):
    def gui_dosya_olustur(self):
        self.p = DosyaOlustur()
        self.make_connection(self.p)
        self.p.show()
        self.p.exec_()

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

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 490)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/icon/uzlastırma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(210, 20, 191, 201))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 23, 34, 30))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lib/icon/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 23, 34, 30))
        self.pushButton_5.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("lib/icon/gtk-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 24, 34, 28))
        self.pushButton_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("lib/icon/gtk-no.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 59, 171, 132))
        self.tableWidget.setMaximumSize(QtCore.QSize(171, 140))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(77)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidget.verticalHeader().setDefaultSectionSize(21)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 191, 141))
        self.groupBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 91, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 191, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 71, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(100, 60, 71, 20))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(100, 80, 71, 20))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(100, 100, 71, 20))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(100, 120, 71, 20))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(100, 140, 71, 20))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 230, 191, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(420, 20, 191, 201))
        self.groupBox_9.setObjectName("groupBox_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 23, 34, 30))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_10.setGeometry(QtCore.QRect(50, 23, 34, 30))
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_11.setGeometry(QtCore.QRect(90, 24, 34, 28))
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_11.setObjectName("pushButton_11")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_9)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 171, 131))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_10.setGeometry(QtCore.QRect(620, 20, 241, 201))
        self.groupBox_10.setObjectName("groupBox_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 23, 34, 30))
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 23, 34, 30))
        self.pushButton_13.setText("")
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_14.setGeometry(QtCore.QRect(90, 24, 34, 28))
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QtCore.QSize(22, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 221, 131))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(220, 240, 641, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 18, 621, 91))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 110, 73, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 881, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 881, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_4.addWidget(self.textEdit_2, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 881, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_5.addWidget(self.textEdit_3, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya_Ekle = QtWidgets.QMenu(self.menubar)
        self.menuDosya_Ekle.setObjectName("menuDosya_Ekle")
        self.menuUzla_mac_Ekle = QtWidgets.QMenu(self.menubar)
        self.menuUzla_mac_Ekle.setObjectName("menuUzla_mac_Ekle")
        self.menu_ablonlar = QtWidgets.QMenu(self.menubar)
        self.menu_ablonlar.setObjectName("menu_ablonlar")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDosya_Ekle = QtWidgets.QAction(MainWindow)
        self.actionDosya_Ekle.setObjectName("actionDosya_Ekle")
        self.actionUzla_mac_Bilgisi_ekle = QtWidgets.QAction(MainWindow)
        self.actionUzla_mac_Bilgisi_ekle.setObjectName("actionUzla_mac_Bilgisi_ekle")
        self.action_ablonlar_d_zenle = QtWidgets.QAction(MainWindow)
        self.action_ablonlar_d_zenle.setObjectName("action_ablonlar_d_zenle")
        self.actionDosya_Sil = QtWidgets.QAction(MainWindow)
        self.actionDosya_Sil.setObjectName("actionDosya_Sil")
        self.actionFont_Ayarla = QtWidgets.QAction(MainWindow)
        self.actionFont_Ayarla.setObjectName("actionFont_Ayarla")
        self.action_ablon_Metni_Ayarla = QtWidgets.QAction(MainWindow)
        self.action_ablon_Metni_Ayarla.setObjectName("action_ablon_Metni_Ayarla")
        self.actionUzla_mac_Sil = QtWidgets.QAction(MainWindow)
        self.actionUzla_mac_Sil.setObjectName("actionUzla_mac_Sil")
        self.menuDosya_Ekle.addAction(self.actionDosya_Ekle)
        self.menuDosya_Ekle.addAction(self.actionDosya_Sil)
        self.menuUzla_mac_Ekle.addAction(self.actionUzla_mac_Bilgisi_ekle)
        self.menuUzla_mac_Ekle.addAction(self.actionUzla_mac_Sil)
        self.menu_ablonlar.addAction(self.action_ablonlar_d_zenle)
        self.menuAyarlar.addAction(self.actionFont_Ayarla)
        self.menubar.addAction(self.menuDosya_Ekle.menuAction())
        self.menubar.addAction(self.menuUzla_mac_Ekle.menuAction())
        self.menubar.addAction(self.menu_ablonlar.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.triggerfinger()
        self.dosya_tara()
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_10.setDisabled(True)
        self.pushButton_11.setDisabled(True)
        self.pushButton_13.setDisabled(True)
        self.pushButton_14.setDisabled(True)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def triggerfinger(self):
        self.actionUzla_mac_Bilgisi_ekle.triggered.connect(uih.gui_uzlastirmaci_ekle)
        self.actionDosya_Ekle.triggered.connect(self.gui_dosya_olustur)
        self.comboBox.currentIndexChanged.connect(self.dosya_bilgisi_cek)
        self.pushButton_4.clicked.connect(self.gui_taraf_ekle)
        self.tableWidget.cellClicked.connect(self.tablodan_parametre_olustur)
        self.pushButton_5.clicked.connect(self.taraf_duzenlemeyi_bagla)
        self.pushButton_6.clicked.connect(self.taraf_sil)
        self.uzlasmaci_tara()


    #Dosya Bilgilerini listele
    def dosya_bilgisi_cek(self):
        if self.comboBox.currentIndex() == 0:
            pass
        else:
            dosya = self.comboBox.currentText()
            sonuc = mdl.tek_satirlik_demet_coz(mdl.dosya_cek(dosya))
            self.label_8.setText(sonuc[2])
            self.label_9.setText(sonuc[3])
            self.label_10.setText(sonuc[4])
            self.label_11.setText(sonuc[5])
            self.label_12.setText(str(sonuc[6]))
            self.dosya_durumu()
            self.taraf_bul(dosya)
    #Uzlaşma dosyasının ne durumda olduğunu göster
    def dosya_durumu(self):
        sonuc = mdl.dosya_durumu_tara(self.comboBox.currentText())
        self.label_7.setText(sonuc)

    def dosya_tara(self):
        sor = mdl.tekli_demet_coz(mdl.kolon_tara("uzno", "dosyalar"))
        for i in range(len(sor)):
            self.comboBox.addItem(sor[i])

    def taraf_bul(self, ar):
        sql = """SELECT ad, sifat FROM taraflar WHERE dosya == '{}' 
        union SELECT ad, sifat FROM temsilciler WHERE dosya == '{}' 
        union SELECT ad, sifat FROM tercuman WHERE dosya == '{}'""".format(ar, ar, ar)
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

    def uzlasmaci_tara(self):
        sor = mdl.tekli_demet_coz(mdl.kolon_tara("isim","uzlasmaci"))
        for i in range(len(sor)):
            self.comboBox_2.addItem(sor[i])

    def tablodan_parametre_olustur(self, row, column):
        oge_ad = self.tableWidget.item(row, column)
        oge_nitelik = self.tableWidget.item(row, column+1)
        if oge_nitelik.text() == "Vekil":
            self.kisi_nitelik_duzenle = "Vekil"
        elif oge_nitelik.text() == "Tercüman":
            self.kisi_nitelik_duzenle = "Tercüman"
        else:
            self.kisi_nitelik_duzenle = "Şahıs"

        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.kisi_duzenle = oge_ad.text()

    def taraf_duzenlemeyi_bagla(self):
        self.gui_taraf_duzenle(self.kisi_duzenle, self.kisi_nitelik_duzenle)

    def taraf_sil(self):
        if self.kisi_nitelik_duzenle == "Şahıs":
            if kayit_sil_soru(self.kisi_duzenle) == True:
                sql = "select id from taraflar where dosya = '{}' and ad = '{}'".format(self.comboBox.currentText(), self.kisi_duzenle)
                mdl.silinecek_veri_bul(sql, "taraflar")
                baslik = "Bilgi Silme Uyarısı"
                mesaj = self.kisi_duzenle + " kişisinin bilgileri veritabanından silindi"
                bilgilendir(mesaj, baslik)
                self.taraf_bul(self.comboBox.currentText())
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

    #Dosya Eklemesinden sonra liste yenilemek için sinyal yakalama
    def make_connection(self, dosyaolustur_object):
        dosyaolustur_object.clicked.connect(self.get_signal_dosya)

    #Dosya'ya taraf ekleme sinyali yakalama
    def taraf_connection(self, dosyaolustur_object):
        dosyaolustur_object.clicked.connect(self.get_signal_taraf)

    @pyqtSlot(bool)
    def get_signal_dosya(self, val):
        if val == False:
            say = self.comboBox.count()
            sayac = say
            for i in range(1, say + 1):
                self.comboBox.removeItem(sayac)
                print(sayac)
                sayac -= 1
            self.dosya_tara()
        else:
            print("Sinyal gelmedi")

    @pyqtSlot(bool)
    def get_signal_taraf(self, val):
        if val == False:
            self.taraf_bul(self.comboBox.currentText())
        else:
            print("Taraf Sinyali Gelmedi")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uzlaş uzlaşabilirsen"))
        self.groupBox.setTitle(_translate("MainWindow", "Taraflar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ad Soyad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sıfat"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dosya Bilgileri"))
        self.label.setText(_translate("MainWindow", "Uzlaşma No"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Dosya Seç"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dosya Durumu"))
        self.label_7.setText(_translate("MainWindow", "Görüşme halinde"))
        self.label_2.setText(_translate("MainWindow", "Soruşturma No"))
        self.label_3.setText(_translate("MainWindow", "M.Esas No"))
        self.label_4.setText(_translate("MainWindow", "Suç"))
        self.label_5.setText(_translate("MainWindow", "Suç Tarihi"))
        self.label_6.setText(_translate("MainWindow", "Dosya No"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Uzlaştırmacı"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Uzlaştırmacı Seç"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Dosya Giderleri"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Adanalı alsdjlaskjd"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.groupBox_10.setTitle(_translate("MainWindow", "Ek Dosyalar"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Mehmet Eroğlu Davet Mektubu"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.groupBox_7.setTitle(_translate("MainWindow", "Olay Özeti"))
        self.pushButton_7.setText(_translate("MainWindow", "Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dosya Bilgileri"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Uzlaşma Görüşmeleri"))
        self.pushButton_2.setText(_translate("MainWindow", "Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Edim"))
        self.pushButton_3.setText(_translate("MainWindow", "Kaydet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Ulaşma Başarsız Olursa Sebebleri"))
        self.menuDosya_Ekle.setTitle(_translate("MainWindow", "Dosya Ekle"))
        self.menuUzla_mac_Ekle.setTitle(_translate("MainWindow", "Uzlaşmacı "))
        self.menu_ablonlar.setTitle(_translate("MainWindow", "Şablonlar"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.actionDosya_Ekle.setText(_translate("MainWindow", "Dosya Ekle"))
        self.actionUzla_mac_Bilgisi_ekle.setText(_translate("MainWindow", "Uzlaşmacı Ekle"))
        self.action_ablonlar_d_zenle.setText(_translate("MainWindow", "Şablonları düzenle"))
        self.actionDosya_Sil.setText(_translate("MainWindow", "Dosya Sil"))
        self.actionFont_Ayarla.setText(_translate("MainWindow", "Font Ayarla"))
        self.action_ablon_Metni_Ayarla.setText(_translate("MainWindow", "Şablon Metni Ayarla"))
        self.actionUzla_mac_Sil.setText(_translate("MainWindow", "Uzlaşmacı Sil"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

