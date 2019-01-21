# -*- coding:utf-8 -*-

from vtbgln import VbagKur
import datetime
import math, time, os
from shutil import copy2
import xlwings as xw
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt


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
    return True

def teklif_yaz(sorno, ad, uz, uzsicil):
    sor = db.komut("select * from taraflar where dosya='{}' and ad='{}'".format(sorno, ad))
    ttarihi = sor[0][2]
    sifat = sor[0][3]
    tc = sor[0][4]
    badı = sor[0][5]
    aadı = sor[0][6]
    dyeri = sor[0][7]
    dtar = sor[0][8]
    adres = sor[0][12]

    ana_dizin = os.getcwd()
    ana_dosya_yolu = "\\dosyalar\\uzfile\\Teklif Formu.xlsx"
    yersor = db.komut("select kayit_yeri from ayarlar")
    no = sorno.replace("/", "-")
    hedef_dizin = yersor[0][0] + "\\" + no
    try:
        os.mkdir(hedef_dizin)
    except FileExistsError:
        pass
    kaynak = ana_dizin + ana_dosya_yolu
    hedef = hedef_dizin +"\\" +ad + " Teklif Formu.xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa1']
    #sht.range('AU1').value = ttarihi Şimdilik sadece dosyadan bilgi alınacak
    sht.range('AU2').value = ttarihi
    sht.range('AU3').value = uz
    sht.range('AU4').value = uzsicil
    sht.range('AU6').value = tc
    sht.range('AU7').value = ad
    sht.range('AU8').value = badı
    sht.range('AU9').value = aadı
    sht.range('AU10').value = dyeri
    sht.range('AU11').value = dtar
    sht.range('AU12').value = adres
    if sifat == "Mağdur / Katılan":
        sht.range('AU13').value = "( X )"
    elif sifat == "Mağdur / Katılan'ın Kanuni Temsilcisi":
        sht.range('AU13').value = "( X )"
    elif sifat == "Suçtan Zarar Gören":
        sht.range('AU13').value = "( X )"
    elif sifat == "Suçtan Zarar Gören'in Kanuni Temsilcisi":
        sht.range('AU13').value = "( X )"
    elif sifat == "Şüpheli / Sanık":
        sht.range('AU13').value = "( X )"
    elif sifat == "Şüpheli Sanığın Kanuni Temsilcisi":
        sht.range('AU13').value = "( X )"
    else:
        print("Sicil durumu veya nitelik durumunda hata var.")
    return True

def tebligat_yaz(sorno, ad):
    sor = db.komut("select * from taraflar where dosya='{}' and ad='{}'".format(sorno, ad))
    ttarihi = sor[0][2]
    sifat = sor[0][3]
    tc = sor[0][4]
    badı = sor[0][5]
    aadı = sor[0][6]
    dyeri = sor[0][7]
    dtar = sor[0][8]
    cinsiyet = sor[0][9]
    adres = sor[0][12]

    ana_dizin = os.getcwd()
    ana_dosya_yolu = "\\dosyalar\\uzfile\\Tebligat.xlsx"
    yersor = db.komut("select kayit_yeri from ayarlar")
    no = sorno.replace("/", "-")
    hedef_dizin = yersor[0][0] + "\\" + no
    try:
        os.mkdir(hedef_dizin)
    except FileExistsError:
        pass
    kaynak = ana_dizin + ana_dosya_yolu
    hedef = hedef_dizin +"\\" +ad + " Tebligat.xlsx"
    copy2(kaynak, hedef)

    wb = xw.Book(hedef)
    sht = wb.sheets['Sayfa1']
    sht.range('Q1').value = sorno
    sht.range('Q2').value = ad
    sht.range('Q3').value = badı
    sht.range('Q4').value = aadı
    sht.range('Q5').value = cinsiyet
    sht.range('Q6').value = dtar
    sht.range('Q7').value = tc
    sht.range('Q8').value = adres
    sht.range('Q9').value = ttarihi
    sorno_sor = db.komut("select sorno, mahesno from dosyalar where uzno='{}'".format(sorno))
    if sorno_sor[0][0] == "":
        sht.range('Q10').value = "Mahkeme"
    else:
        sht.range('Q10').value = "Soruşturma"
    return True

def eslestir(sa, vek=None):
    if len(sa) == 0:
        pass
    else:
        for i in range(len(sa)):
            s_ad = doc.add_paragraph()
            s_ad.paragraph_format.left_indent = Inches(0.5)
            i_s_ad = s_ad.add_run("Ad Soyad \t\t:{}".format(sa[i][1]))
            i_s_ad.bold = False

            s_tc = doc.add_paragraph()
            s_tc.paragraph_format.left_indent = Inches(0.5)
            i_s_tc = s_tc.add_run("T.C. Kimlik No \t\t:{}".format(sa[i][4]))
            i_s_tc.bold = False

            s_adr = doc.add_paragraph()
            s_adr.paragraph_format.left_indent = Inches(0.5)
            i_s_adr = s_adr.add_run("Adres \t\t:{}".format(sa[i][12]))
            i_s_adr.bold = False




def rapor_yaz(sorno, uz, uz_sicil):

    yersor = db.komut("select kayit_yeri from ayarlar")
    no = sorno.replace("/", "-")
    hedef_dizin = yersor[0][0] + "/" + no + "/" + "rapor.docx"

    dosya = db.komut("select * from dosyalar where uzno = '{}'".format(sorno))
    uzlastirma_no = dosya[0][1]
    sorusturma_no = dosya[0][2]
    mahkeme_esas_no = dosya[0][3]
    suc = dosya[0][4]
    uz_bilgileri = db.komut("select adres from uzlasmaci where isim = '{}'".format(uz))
    uz_adres = uz_bilgileri[0][0]

    doc = Document()
    run = doc.add_paragraph().add_run()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.bold = True

    baslik = doc.add_paragraph("UZLAŞTIRMA RAPORU")
    baslik.alignment = WD_ALIGN_PARAGRAPH.CENTER
    baslik.add_run()

    uzno = doc.add_paragraph("Uzlaştırma No\t\t\t\t:{}".format(dosya[0][1]))
    uzno.add_run()

    sno = doc.add_paragraph("Cumhuriyet Başsavcılığı Soruşturma No\t:{}".format(dosya[0][2]))
    sno.add_run()

    esno = doc.add_paragraph("Mahkeme Esas No\t\t\t\t:{}".format(dosya[0][3]))
    esno.add_run()

    suc = doc.add_paragraph("Uzlaştırma Konusu Suç/Suçlar \t\t:{}".format(dosya[0][4]))
    suc.add_run()

    doc_uz = doc.add_paragraph("Uzlaştırmacının")
    doc_uz.paragraph_format.space_before = Pt(12)
    doc_uz.add_run()

    adi = doc.add_paragraph()
    adi.paragraph_format.left_indent = Inches(0.5)
    i_adi = adi.add_run("Adı Soyadı \t\t\t\t:{}".format(uz))
    i_adi.bold = False

    sici = doc.add_paragraph()
    sici.paragraph_format.left_indent = Inches(0.5)
    i_sici = sici.add_run("Uzlaştırmacının Sicili \t\t:{}".format(uz_sicil))
    i_sici.bold = False

    dos_uzad = doc.add_paragraph()
    dos_uzad.paragraph_format.left_indent = Inches(0.5)
    i_dos_uzad = dos_uzad.add_run("İletişim Adresi \t\t\t:{}".format(uz_bilgileri[0][0]))
    i_dos_uzad.bold = False

    doc_gorev_tarihi = doc.add_paragraph("Görevlendirme Tarihi\t\t\t:{}".format("yazılacak"))
    doc_gorev_tarihi.add_run()

    doc_evrak_tarihi = doc.add_paragraph("Dosya içindeki belgelerin birer Örneğinin\n\tverildiği  /"
                                         " Uzl. Süresinin başladığı tarih\t:{}".format("Bakılacak"))
    doc_evrak_tarihi.add_run()

    doc_uzlasmateklif = doc.add_paragraph("Uzlaşma Teklif Tarihi\t\t\t:{}".format("uzlaşma teklif Tarihi"))
    doc_uzlasmateklif.add_run()

    doc_eksure = doc.add_paragraph("Ek süre verilme tarihi ve süresi\t\t:{}".format("Ek süre 10 gün"))
    doc_eksure.paragraph_format.space_after = Pt(12)
    doc_eksure.add_run()

    saniklar = db.komut("select * from taraflar where dosya='{}'and sifat='5'".format(sorno))
    sanik_temsilcileri = db.komut("select * from taraflar where dosya='{}'and sifat='6'".format(sorno))
    magdurlar = db.komut("select * from taraflar where dosya='{}'and sifat='1'".format(sorno))
    magdur_temsilcileri = db.komut("select * from taraflar where dosya='{}'and sifat='2'".format(sorno))
    zarar_gorenler = db.komut("select * from taraflar where dosya='{}'and sifat='3'".format(sorno))
    zarar_goren_temsilcileri = db.komut("select * from taraflar where dosya='{}'and sifat='4'".format(sorno))
    mustekiler = db.komut("select * from taraflar where dosya='{}'and sifat='7'".format(sorno))
    musteki_temsilcileri = db.komut("select * from taraflar where dosya='{}'and sifat='8'".format(sorno))


    if len(magdurlar) == 0:
        pass
    else:
        doc_s1 = doc.add_paragraph("Şüphelinin /Sanığın / Kanuni Temsilcisinin")
        doc_s1.paragraph_format.space_before = Pt(12)
        doc_s1.add_run()
        for i in range(len(magdurlar)):
            s_ad = doc.add_paragraph()
            s_ad.paragraph_format.left_indent = Inches(0.5)
            i_s_ad = s_ad.add_run("Ad Soyad \t\t:{}".format(magdurlar[i][1]))
            i_s_ad.bold = False

            s_tc = doc.add_paragraph()
            s_tc.paragraph_format.left_indent = Inches(0.5)
            i_s_tc = s_tc.add_run("T.C. Kimlik No \t\t:{}".format(magdurlar[i][4]))
            i_s_tc.bold = False

            s_adr = doc.add_paragraph()
            s_adr.paragraph_format.left_indent = Inches(0.5)
            s_adr.paragraph_format.space_after = Pt(12)
            i_s_adr = s_adr.add_run("Adres \t\t:{}".format(magdurlar[i][12]))
            i_s_adr.bold = False

            vekil_ara = db.komut("select * from temsilciler where dosya='{}'and kisi='{}'".format(sorno, magdurlar[i][1]))
            if len(vekil_ara) == 0:
                pass
            else:
                doc_s1 = doc.add_paragraph("Müdafinin")
                doc_s1.paragraph_format.space_before = Pt(12)
                doc_s1.add_run()

                v_ad = doc.add_paragraph()
                v_ad.paragraph_format.left_indent = Inches(0.5)
                i_v_ad = v_ad.add_run("Ad Soyad \t\t:{}".format(magdurlar[i][1]))
                i_v_ad.bold = False

                v_tc = doc.add_paragraph()
                v_tc.paragraph_format.left_indent = Inches(0.5)
                i_v_tc = v_tc.add_run("T.C. Kimlik No \t\t:{}".format(magdurlar[i][4]))
                i_v_tc.bold = False

                v_adr = doc.add_paragraph()
                v_adr.paragraph_format.left_indent = Inches(0.5)
                v_adr.paragraph_format.space_after = Pt(12)
                i_v_adr = v_adr.add_run("Adres \t\t:{}".format(magdurlar[i][12]))
                i_v_adr.bold = False
    if len(magdur_temsilcileri) == 0:
        pass
    else:
        doc_s1 = doc.add_paragraph("Şüphelinin /Sanığın / Kanuni Temsilcisinin")
        doc_s1.paragraph_format.space_before = Pt(12)
        doc_s1.add_run()
        for i in range(len(magdur_temsilcileri)):
            t_ad = doc.add_paragraph()
            t_ad.paragraph_format.left_indent = Inches(0.5)
            i_t_ad = t_ad.add_run("Ad Soyad \t\t:{}".format(magdur_temsilcileri[i][1]))
            i_t_ad.bold = False

            s_tc = doc.add_paragraph()
            s_tc.paragraph_format.left_indent = Inches(0.5)
            i_s_tc = s_tc.add_run("T.C. Kimlik No \t\t:{}".format(magdur_temsilcileri[i][4]))
            i_s_tc.bold = False

            s_adr = doc.add_paragraph()
            s_adr.paragraph_format.left_indent = Inches(0.5)
            s_adr.paragraph_format.space_after = Pt(12)
            i_s_adr = s_adr.add_run("Adres \t\t:{}".format(magdur_temsilcileri[i][12]))
            i_s_adr.bold = False

            vekil_ara = db.komut("select * from temsilciler where dosya='{}'and kisi='{}'".format(sorno, magdur_temsilcileri[i][1]))
            if len(vekil_ara) == 0:
                pass
            else:
                doc_s1 = doc.add_paragraph("Müdafinin")
                doc_s1.paragraph_format.space_before = Pt(12)
                doc_s1.add_run()
                v_ad = doc.add_paragraph()
                v_ad.paragraph_format.left_indent = Inches(0.5)
                i_v_ad = v_ad.add_run("Ad Soyad \t\t:{}".format(magdur_temsilcileri[i][1]))
                i_v_ad.bold = False

                v_tc = doc.add_paragraph()
                v_tc.paragraph_format.left_indent = Inches(0.5)
                i_v_tc = v_tc.add_run("T.C. Kimlik No \t\t:{}".format(magdur_temsilcileri[i][4]))
                i_v_tc.bold = False

                v_adr = doc.add_paragraph()
                v_adr.paragraph_format.left_indent = Inches(0.5)
                v_adr.paragraph_format.space_after = Pt(12)
                i_v_adr = v_adr.add_run("Adres \t\t:{}".format(magdur_temsilcileri[i][12]))
                i_v_adr.bold = False



    doc.save(hedef_dizin)

