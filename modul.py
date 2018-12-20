# -*- coding:utf-8 -*-

from vtbgln import VbagKur
import datetime
import math, time, os
from shutil import copy2
import xlwings as xw


db = VbagKur()

def kolon_tara(sutun, tablo):
    sor = db.kolon_oku(sutun, tablo)
    return sor

def dosya_durumu_tara(dosya):
    arg = db.hepsini_oku("durum", "dosyalar", "uzno", dosya)
    if arg[0][0] == 0:
        return ("Dosya Oluşturuldu.")
    elif arg[0][0] == 1:
        return ("Uzlaşma aşamasında")
    elif arg[0][0] == 4:
        return ("Uzlaşma sonlandı")

def tekli_demet_coz(demet):
    dizi = []
    for i in range(len(demet)):
        dizi.append(demet[i][0])
    return dizi

def tek_satirlik_demet_coz(demet):
    dizi = []
    for i in range(len(demet[0])):
        dizi.append(demet[0][i])
    return dizi

def dosya_cek(dosya):
    sor = db.hepsini_oku("*", "dosyalar", "uzno", dosya)
    return sor

def kmt(dosya):
    son = db.komut(dosya)
    return son

def silinecek_veri_bul(arg, tablo):
    sonuc = tek_satirlik_demet_coz(db.komut(arg))
    db.satir_sil("DELETE FROM {} WHERE id = '{}'".format(tablo, sonuc[0]))
    return True

def silinecek_gider_bul(arg):
    sonuc = tek_satirlik_demet_coz(db.komut(arg))
    db.satir_sil("DELETE FROM giderler WHERE id = '{}'".format(sonuc[0]))
    return True

def silinecek_ek_bul(arg):
    sonuc = tek_satirlik_demet_coz(db.komut(arg))
    db.satir_sil("DELETE FROM ek WHERE id = '{}'".format(sonuc[0]))
    return True

def tarih_duzenle(arg=None):
    if arg == None:
        return False
    else:
        t = arg.replace("-","/")
        formatstring = '%Y/%m/%d'
        dosya_bitis = datetime.datetime.strptime(t, formatstring)
        bugun = datetime.datetime.now()
        fark = dosya_bitis - bugun
        return str(fark)

def uzatma_tarihi_ekle(arg, dosya):
    sql = """UPDATE dosyalar SET 
        uzatmatar='{}' WHERE uzno = '{}'""".format(arg, dosya)
    sor = db.komut(sql)

def olay_ozeti_cek(arg):
    return db.komut("select ozet from olaylar where uzno = '{}'".format(arg))

def gorusme_cek(arg):
    return db.komut("select gorusme from uzgor where dosya = '{}'".format(arg))

def edim_cek(arg):
    return db.komut("select edi from edim where dosya = '{}'".format(arg))

def uzbas_cek(arg):
    return db.komut("select sebeb from uzbas where dosya = '{}'".format(arg))

def davet_yaz(durum, sahis, tc, veksicil, no, ttarihi, uz, uzsicil, uzte):
    ana_dizin = os.getcwd()
    ana_dosya_yolu = "\\dosyalar\\uzfile\\Davet Mektubu.xlsx"
    sor = db.komut("select kayit_yeri from ayarlar")
    sorno = no.replace("/", "-")
    hedef_dizin = sor[0][0] + "\\" + sorno
    try:
        os.mkdir(hedef_dizin)
    except FileExistsError:
        pass
    kaynak = ana_dizin + ana_dosya_yolu
    hedef = hedef_dizin +"\\" +sahis + " Davet Mektubu.xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa1']
    sht.range('AT3').value = durum
    sht.range('AT4').value = sahis
    sht.range('AT5').value = tc
    sht.range('AT6').value = no
    sht.range('AT7').value = ttarihi
    sht.range('AT8').value = uz
    sht.range('AT9').value = uzsicil
    sht.range('AT10').value = uzte
    sht.range('AT11').value = veksicil
