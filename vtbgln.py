# -*- coding:utf-8 -*-
# -*- coding:cp1254 -*-
#sys.path.append(r'/home/istihza/programlar') komutu ile bu modülü python yoluna ekleyebilirsin

import sqlite3

class VbagKur(object):
    def __init__(self) -> object:
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

    def dosya_ekle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9):
        """ Dosya Bilgilerini veritabanına ekle

        :param: a1 : Uzlaşma No (str)
        :param: a2 : Sorgulama No (str)
        :param: a3 : Mahkeme Esas No (str)
        :param: a4 : Suç/Suçlar (str)
        :param: a5 : Teklif Tarihi (str)
        :param: a6 : Tevdi Teslim Tarihi (str)
        :param: a7 : Dosya Durumu (int)
        :param: a8 : Uzatma Tarihi (str)
        :param: a9 : Uzlaştırmacı(str)

        """
        self.im.execute("""INSERT INTO dosyalar VALUES(NULL, '{}','{}','{}','{}','{}','{}','{}','{}','{}')"""
                        .format(a1, a2, a3, a4, a5, a6, a7, a8, a9))
        self.vt.commit()
        return True

    def kolon_oku(self, sutun, tablo):
        self.im.execute("select {} from {}".format(sutun, tablo))
        veriler = self.im.fetchall()
        return veriler

    def tarafekle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13):
        """Taraf Ekleme Fonksiyonu
        
        :param a1: ad(str)
        :param a2: teklif tarihi (str)
        :param a3: Sıfat(str)
        :param a4: Tc no(str)
        :param a5: Baba adı(str)
        :param a6: Anne Adı(str)
        :param a7: Doğum Yeri (str)
        :param a8: Doğum Tarihi(str)
        :param a9: Cinsiyet (str)
        :param a10: Telefon (str)
        :param a11: Adres Niteliği(int)
        :param a12: adres(str)
        :param a13: Dosya Ulaşma no (str)
        :return: True
        """
        self.im.execute("""INSERT INTO taraflar VALUES(NULL,'{}','{}','{}',
        '{}','{}','{}',
        '{}','{}','{}',
        '{}','{}','{}','{}')""".format(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13))
        self.vt.commit()
        return True

    def temsilci_ekle(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11):
        """Temsilci Ekleme
        :param a1: Teklif Tarihi (str)
        :param a2: Ad (str)
        :param a3: Sicil No (str)
        :param a4: Telefon (str)
        :param a5: Adres (str)
        :param a6: Dosya Uzlaşma No (str)
        :param a7: Temsilcisi olduğu kişi(str)
        :param a7: Temsilci Niteliği (Müdafi, vekil)(str)
        :param a7: Bağlı Olduğu Baro(str)
        :param a7: Tc No(str)
        :return:  True
        """
        self.im.execute("INSERT INTO temsilciler VALUES(NULL,"
                        " '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(a1,a2,a3,a4,a5,a6, a7,a8,a9,a10,a11))
        self.vt.commit()
        return True

    def tercuman_ekle(self, a1, a2, a3, a4, a5, a6):
        """ Tercüman Ekle

        :param a1: Ad(str)
        :param a2: Tc no (str)
        :param a3: Adres(str)
        :param a4: Dosya(str)
        :param a5: Bağlı olduğu kişi(str)
        :param a6: Sifat(str)
        :return: True
        """
        self.im.execute("INSERT INTO tercuman VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}')".format(a1, a2, a3, a4, a5, a6))
        self.vt.commit()
        return True

    def sahis_guncelle(self, l):
        self.im.execute("""UPDATE taraflar SET 
        ad='{}', ttarihi='{}', sifat='{}',tc='{}',
        baba='{}',anne='{}',dyeri='{}',
        dtarihi='{}',cins='{}',tel='{}',
        adresniteligi='{}',adres='{}' WHERE id = '{}'""".format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10], l[11], l[12]))
        self.vt.commit()
        return True

    def vekil_guncelle(self, l):
        self.im.execute("""UPDATE temsilciler SET 
        ttarihi='{}', ad='{}',sicil='{}',tel='{}',
        adres='{}',kisi='{}', nitelik='{}',baro='{}',tc='{}' WHERE id = '{}'"""
                        .format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8], l[9]))
        self.vt.commit()
        return True

    def tercuman_guncelle(self, l):
        self.im.execute("""UPDATE tercuman SET 
        ad='{}',tc='{}',adres='{}',
        kisi='{}' WHERE id = '{}'""".format(l[0],l[1],l[2],l[3],l[4]))
        self.vt.commit()
        return True

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

    def satir_sil(self, sql):
        self.im.execute(sql)
        self.vt.commit()
        return True

    def gider_ekle(self, a1, a2, a3):
        """Dosya Gider Ekle

        :param a1: Gider Açıklaması (str)
        :param a2: Gider Tutarı (int)
        :param a3: Gider Yapılan Dosya(str)
        :return: True
        """
        self.im.execute("INSERT INTO giderler VALUES(NULL, '{}', '{}', '{}')".format(a1, a2, a3))
        self.vt.commit()
        return True

    def ek_ekle(self, a1, a2):
        """Dosya Gider Ekle

        :param a1: Gider Açıklaması (str)
        :param a2: Gider Yapılan Dosya(str)
        :return: True
        """
        self.im.execute("INSERT INTO ek VALUES(NULL, '{}', '{}')".format(a1, a2))
        self.vt.commit()
        return True

    def komut(self, komut):
        self.im.execute(komut)
        return self.im.fetchall()

    def yapistir(self, komut):
        self.im.execute(komut)
        self.vt.commit()
        return True

    def veritabanini_kapat(self):
        self.vt.close()

