# -*- coding:utf-8 -*-

from vtbgln import VbagKur
import datetime

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