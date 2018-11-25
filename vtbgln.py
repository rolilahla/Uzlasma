# -*- coding:utf-8 -*-
# -*- coding:cp1254 -*-
#sys.path.append(r'/home/istihza/programlar') komutu ile bu modülü python yoluna ekleyebilirsin

import sqlite3

class VbagKur(object):
    def __init__(self):
        self.vt = sqlite3.connect('lib/database/rolilahla.sqlite')
        self.im = self.vt.cursor()

    def uzlastirmaci_ekle(self, a1, a2, a3, a4, a5):
        """Uzlaştırmacı Ekle

           :param      :a1 = Ad Soyad (str)
           :param      :a2 = Sicil No (str)
           :param      :a3 = Telefon No (str)
           :param      :a4 = Bağlı bulunduğu şehir (str)
           :param      :a5 = Adres (str)
           """
        self.im.execute(
            """INSERT INTO uzlasmaci VALUES(NULL, '{}','{}','{}','{}','{}')""".format(a1, a2, a3, a4, a5))
        self.vt.commit()
        return True

    def dosya_ekle(self, a1, a2, a3, a4, a5, a6, a7):
        """ Dosya Bilgilerini veritabanına ekle

        :param: a1 : Uzlaşma No (str)
        :param: a2 : Sorgulama No (str)
        :param: a3 : Mahkeme Esas No (str)
        :param: a4 : Suç/Suçlar (str)
        :param: a5 : Teklif Tarihi (str)
        :param: a6 : Tevdi Teslim Tarihi (str)
        :param: a7 : Dosya Durumu (int)

        """
        self.im.execute("""INSERT INTO dosyalar VALUES(NULL, '{}','{}','{}','{}','{}','{}','{}')""".format(a1, a2, a3, a4, a5, a6, a7))
        self.vt.commit()
        return True

    def dosya_sil(self, arg):
        """ Dosya Sil

        :param arg:  uzlaşma no(str)
        :return: true
        """
        self.im.execute("delete * from dosyalar where uzno == arg")

    def kolon_oku(self, sutun, tablo):
        self.im.execute("select {} from {}".format(sutun, tablo))
        veriler = self.im.fetchall()
        return veriler

    def tarafekle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14):
        """Taraf Ekleme Fonksiyonu
        
        :param a1: ad(str)
        :param a2: Sıfat(str)
        :param a3: Tc no(str)
        :param a4: Baba adı(str)
        :param a5: Anne Adı(str)
        :param a6: Doğum Yeri (str)
        :param a7: Doğum Tarihi(str)
        :param a8: Cinsiyet (str)
        :param a9: Telefon (str)
        :param a10: Adres Niteliği(int)
        :param a11: adres(str)
        :param a12: Kanuni Temsilci adı (str)
        :param a13: Tercüman Adı (str)
        :param a14: Dosya Ulaşma no (str)
        :return: True
        """
        self.im.execute("""INSERT INTO taraflar VALUES(NULL,'{}','{}','{}',
        '{}','{}','{}',
        '{}','{}','{}',
        '{}','{}','{}',
        '{}','{}')""".format(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14))
        self.vt.commit()
        return True

    def temsilci_ekle(self, a1, a2, a3, a4, a5, a6, a7):
        """Temsilci Ekleme
        :param a1: Ad (str)
        :param a2: Sicil No (str)
        :param a3: Telefon (str)
        :param a4: Adres (str)
        :param a5: Dosya Uzlaşma No (str)
        :param a6: Temsilcisi olduğu kişi(str)
        :param a7: Temsil ettiği kişinin sıfatı(str)
        :return:  True
        """
        self.im.execute("INSERT INTO temsilciler VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a1,
                                                                                                                 a2,a3,
                                                                                                                 a4,a5,
                                                                                                                 a6,a7))
        self.vt.commit()
        return True

    def tercuman_ekle(self, a1, a2, a3, a4, a5):
        """ Tercüman Ekle

        :param a1: Ad(str)
        :param a2: Tc no (str)
        :param a3: Adres(str)
        :param a4: Dosya(str)
        :param a5: Bağlı olduğu kişi(str)
        :return: True
        """
        self.im.execute("INSERT INTO tercuman VALUES(NULL, '{}', '{}', '{}', '{}', '{}')".format(a1, a2, a3, a4, a5))
        self.vt.commit()
        return True

    def taraf_cek(self):
        self.im.execute("select ")

    def gemi_guncelle(self, l):
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

    def komut(self, komut):
        self.im.execute(komut)
        return self.im.fetchall()


    def veritabanini_kapat(self):
        self.vt.close()

