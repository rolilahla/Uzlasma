# -*- coding:utf-8 -*-

from vtbgln import VbagKur

db = VbagKur()

def dosya_tara():
    sor = db.sorgu_no_bul()
    return sor

def tekli_demet_coz(demet):
    dizi = []
    for i in range(len(demet)):
        dizi.append(demet[i][0])
    return dizi

def taraf_tara():
    pass
