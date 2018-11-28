# -*- coding:utf-8 -*-

from vtbgln import VbagKur

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
