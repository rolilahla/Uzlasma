# -*- coding:utf-8 -*-
# -*- coding:cp1254 -*-
#sys.path.append(r'/home/istihza/programlar') komutu ile bu modülü python yoluna ekleyebilirsin

import sqlite3

class VbagKur(object):
    def __init__(self):
        self.vt = sqlite3.connect('lib/database/rolilahla.sqlite')
        self.im = self.vt.cursor()


    def uzlasma_olustur(self,a1,a2,a3,a4,a5,a6):
        """
            Dosya Bilgisini Veritabanına ekleme
        """
        self.im.execute("""INSERT INTO uzlasma VALUES(NULL, '{}','{}','{}','{}','{}','{}')""".format(a1, a2, a3, a4, a5, a6))
        self.vt.commit()

    def sorgu_no_bul(self):
        self.im.execute("select sorno from uzlasma")
        veriler = self.im.fetchall()
        return veriler

    def gemi_guncelle(self, l):
        """
        print (
            Değişkenler Alındı :
            Kod______________:{}
            Firma____________:{}
            Gemi_____________:{}
            Gemi Kodu________:{}
            Gemi Cinsi_______:{}
            Defter No________:{}
            Belge No_________:{}
            Sicil No_________:{}
            İmo _____________:{}
            Tel _____________:{}
            Acente___________:{}
            Acente Tel_______:{}
            Adres____________:{}
            Vergi Dairesi____:{}
            Vergi No_________:{}


            .format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[14],l[12],l[13]))"""
        self.im.execute("""UPDATE gemiler SET kod='{}',
        fad='{}',
        gad='{}',
        gemikod='{}',
        cins='{}',
        dno='{}',
        bno='{}',
        sno='{}',
        imo='{}',
        tel='{}',
        acente='{}',
        acentel='{}',
        adres='{}',
        verdaire='{}',
        vno='{}' WHERE gad = '{}'""".format
           (l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[14],l[12],l[13],l[2]))
        print ("Veri Ekleme işlemi tamamlandı")
        self.vt.commit()

    #Tüm verileri çekme
    def hepsini_oku(self, aranan=None, tablo = None, yer=None, istenilen=None):
        """
            Belli bir kritere göre toplam sonuç ve kritersiz gönderimde tüm sonuçları döker
            parametreler:
            - aranan : İstenilen bölümü çeker
            - tablo  : Arama yapılmak istenilen tablo 
            - Yer    : Where işleci için şart sütunu
            - İstenilen: Karşılaştırma

        """
        if istenilen == None:
            self.im.execute("SELECT {} FROM {}".format(aranan,tablo))
            veriler = self.im.fetchall()
            return veriler
        else:
            self.im.execute("SELECT {} FROM {} WHERE {} = '{}'".format(aranan, tablo, yer ,istenilen))
            return self.im.fetchall()

    #tek veri çekme
    def tek_oku(self, tablo, yer, deger):
        self.im.execute("SELECT * FROM {} Where {} == '{}'".format(tablo, yer, deger))
        veriler = self.im.fetchall()
        return veriler

    def veri_duzenle(self,demet):
        dizi = []
        for i in range(len(demet)):
            a = list(demet[i])
            dizi.append(str(a[0]))
        return dizi

    def dolum_ekle(self, t, l, k, y):
        print ("Değişkenler Alındı")
        self.im.execute("""INSERT INTO densitys VALUES(null, '{}', '{}', '{}', '{}', 0, 0, '{}', '{}')
            """.format(t, l, k, y, l, k))
        print ("Veri Ekleme işlemi tamamlandı")
        self.vt.commit()

    def veritabanini_kapat(self):
        self.vt.close()

