#veriler = [('Uçurtm Avcısı', 'Konmakre', 500),
#           ('Satranç', 'Stefan', 600),
#           ('Suç ve Ceza', 'Dostayevski', '800'),
#           ('Pıtırcık', 'Yahya Öz', 120)]
#def tablo_olustur():
#    cursor.execute("CREATE TABLE IF NOT EXISTS kitap (kitap_ad TEXT,yazar TEXT, sayfa_sayisi INT,begeni TEXT)")
#def deger_ekle():
#for veri in veriler:
#   cursor.execute("INSERT INTO kitap (kitap_ad,yazar,sayfa_sayisi,begeni) VALUES(?,?,?,?)",veri)
#
import sqlite3
import time
import random
con = sqlite3.connect("kitapevi.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitap (kitap_ad TEXT,yazar TEXT, sayfa_sayisi INT,tur TEXT,kategori TEXT,fiyat INT)")
print("INCE KİTAPEVİ AÇILIYOR...")
time.sleep(3)
print("Yapabileceğiniz işlemler yükleniyor..")
time.sleep(1)
def deger_ekle():

        while True:
            try:
                kitap_ad = str(input("Kitap ismi giriniz:"))
                yazar = str(input("Kitabın yazarını giriniz:"))
                sayfa_sayisi = int(input("Kitabın sayfa sayısını giriniz:"))
                kategori=str(input("Kitabın kategorisini yazınız:"))
                tur=str(input("Kitabın türünü giriniz:"))
                fiyat = float(input("Kitabın fiyatını giriniz:"))
                cursor.execute("INSERT INTO kitap (kitap_ad,yazar,sayfa_sayisi,tur,kategori,fiyat) VALUES(?,?,?,?,?,?)",
                               (kitap_ad, yazar, sayfa_sayisi,tur,kategori, fiyat))
                con.commit()
                break
            except ValueError:
                print("Lütfen geçerli bir numara giriniz.")
def tablo_goster():
        cursor.execute("SELECT * FROM kitap")
        data = cursor.fetchall()
        for i in data:
            print(i)
def kitap_sil():
    print("Silme işlemine hoşgeldiniz..")
    time.sleep(3)
    sil_kitap=input("Silmek istediğiniz kitabın ismini yazınız.")
    cursor.execute("DELETE FROM kitap WHERE kitap_ad = ?",[sil_kitap])
    con.commit()
def kitap_guncelle():
    print("Güncelleme işlemine hoşgeldiniz..")
    time.sleep(3)
    gir_kitap_ad=input("Güncellemek istediğiniz kitabın ismini giriniz:")
    guncelle_yazar = input("Kitabın yazarını girin:")
    guncelle_sayfa_sayisi= input("Kitabın sayfa sayısı girin:")
    guncelle_tur=input("Kitabın türünü girin:")
    guncelle_kategori=input("Kitabın kategorisini girin:")
    guncelle_fiyat=input("Kitabın fiyatını girin:")
    cursor.execute("UPDATE kitap SET kategori = ?  WHERE kitap_ad = ? ",(guncelle_kategori,gir_kitap_ad))
    cursor.execute("UPDATE kitap SET fiyat = ?  WHERE kitap_ad = ? ",(guncelle_fiyat,gir_kitap_ad))
    cursor.execute("UPDATE kitap SET yazar = ?  WHERE kitap_ad = ? ",(guncelle_yazar,gir_kitap_ad))
    cursor.execute("UPDATE kitap SET tur = ?  WHERE kitap_ad = ? ",(guncelle_tur,gir_kitap_ad))
    cursor.execute("UPDATE kitap SET sayfa_sayisi = ?  WHERE kitap_ad = ? ",(guncelle_sayfa_sayisi,gir_kitap_ad))
    con.commit()
def komut():
    while True:
        print("-------------------------------------------------------------------------")
        print("Sistemdeki Kitapları Görüntüleme - 1")
        print("Sisteme Kitap Ekleme - 2")
        print("Sistemden Kitap Silme - 3")
        print("Sistemden Kitap Güncelleme - 4")
        print("Sistemden Çıkma - 5")
        islem = int(input("Kütüphane de yapmak istediğiniz işlemi seçiniz:"))
        if islem==1:
            tablo_goster()
            cikis = input("Çıkış yapmak istiyor musunuz? Evet / Hayır:")
            try:
                if cikis == "Evet" or cikis == "evet":
                    print("-----------------------------------------")
                    print("Kütüphaneden Çıkılıyor..")
                    time.sleep(2)
                    break
                elif cikis == "Hayır" or cikis == "hayır":
                    continue
            except ValueError:
                print("Lütfen geçerli bir ifade yazınız.")
        elif islem == 2:
            deger_ekle()
            cikis=input("Çıkış yapmak istiyor musunuz? Evet / Hayır:")
            try:
                if cikis=="Evet" or cikis=="evet":
                    print("Çıkış yapılıyor...")
                    time.sleep(2)
                    break
                elif cikis == "Hayır" or cikis == "hayır":
                    continue
            except ValueError:
                print("Lütfen geçerli bir ifade yazınız.")
        elif islem == 3:
            kitap_sil()
            cikis = input("Çıkış yapmak istiyor musunuz? Evet / Hayır:")
            try:
                if cikis == "Evet" or cikis == "evet":
                    print("-----------------------------------------")
                    print("Kütüphaneden Çıkılıyor..")
                    time.sleep(2)
                    break
                elif cikis == "Hayır" or cikis == "hayır":
                    continue
            except ValueError:
                print("Lütfen geçerli bir ifade yazınız.")
        elif islem == 4:
            kitap_guncelle()
        elif islem == 5:
            print("-----------------------------------------")
            print("Kütüphaneden Çıkılıyor..")
            time.sleep(2)
            break
con.commit()
tablo_olustur()
komut()
con.close()


