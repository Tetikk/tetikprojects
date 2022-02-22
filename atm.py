from tkinter import N
from unicodedata import name
a = 0
sifre = 0
while 1:
    if sifre == 0:
        sifre = int(input("Bir Şifre Oluşturunuz\t:"))
        sifreonay = int(input("Şifreyi Tekrarlayınız\t:"))
    else:
        giris = int(input("Lütfen Şifrenizi Giriniz\t:"))
        if giris == sifre:
            print("Para Çekmek İçin|1\nPara Yatırmak İçin|2\nBakiye Öğrenmek İçin|3\nÇıkış Yapmak İçin|0")
            islem = int(input("Hangi İşlemi Yapmak İstersiniz\t:"))
            if islem == 1:
                paracek = int(input("Çekeceğiniz Miktarı Giriniz\t:"))
                if paracek==0 or paracek<0:
                    print("İşlem Geçersiz\n")
                elif paracek>a:
                    print("Hesabınızda Bu Kadar Miktar Bulunmuyor.\n")
                else:
                    a = a-paracek
                    print(paracek,"TL Para Çektiniz\n")
            elif islem == 2:
                parayatir = int(input("Yatıracağınız Miktarı Giriniz\t:"))
                if parayatir==0 or parayatir<0:
                    print("İşlem Geçersiz\n")
                else:
                    a = a+parayatir
                    print(parayatir,"TL Para Yatırdınız\n")
            elif islem == 3:
                print(a,"TL Bakiyeniz Bulunmakta\n")
            elif islem == 0:
                break
            elif islem == 4:
                print("Faiz %1")
                kredi = int(input("Kredi Çekeceğiniz Miktarı Giriniz\t:"))
                odenecekkredi = kredi+(kredi*1/100)
                print("Ödencek Miktar",odenecekkredi)
                b = int(input("Onaylıyor musunuz?(1:evet, 0:hayır)\t:"))
                if b==1:
                    print("İşlem Gerçekleştirilmiştir.\n")
                    a = a+kredi
                else:
                    print("")
            elif islem == 5:
                c = int(input("Ödenecek Tutarı Giriniz\t:"))
                if c>odenecekkredi:
                    print("Girdiğiniz tutar borcunuzdan fazla.\n")
                elif c<1:
                    print("İşlem Geçersiz.")
                elif odenecekkredi==0:
                    odenecekkredi = odenecekkredi-c
                    print("Kredi Borcunuz Kalmadı")
                else:
                    odenecekkredi = odenecekkredi-c
                    print(odenecekkredi,"TL Borcunuz Kaldı")                    
            elif islem == 6:
                print(odenecekkredi,("TL Kredi borcunuz bulunmakta.\n"))
        else:
            print("Şifre Yanlış Lütfen Tekrar Deneyiniz.\n")