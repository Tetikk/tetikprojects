import time
import random
#Şahbatur
#Gülbatur
#Ayşo
#Devirhan
#Yazıhan
#Kasemumkara
baslat = 0
tursayi = 0
kazananat = 0
para = 10000
while 1:
    if baslat == 0:
        kazanansayi = 0
        print("1| Şahbatur\n2| Gülbatur\n3| Ayşo\n4| Devirhan\n5| Yazıhan\n6| Kasemumkara")
        atismi = int(input("Bir At Seçiniz\t:"))
        print()
        print(para,"TL Bakiyeniz Bulunmakta")
        bahis = int(input("Bahis Yapacağınız Miktarı Giriniz\t:"))
        para = para-bahis
        if bahis>para:
            print("Bakiyeyi Aşmayınız.\n")
        else:
            baslat = int(input("Yarışı Başlamtak İçin '1' Yazınız\t:"))
    if baslat == 1:
        if tursayi<5:
            if tursayi==0:
                print("Yarış Başlamak Üzere")
                time.sleep(5)
                print("Yarış Başladı!")
                tursayi+=1
            else:
                sayi1 = random.uniform(1, 6)
                sayi1 = round(sayi1)
                tursayi+=1
                time.sleep(3)
                if sayi1 == 1.0:
                    print("Şahbatur Öne Geçti!")
                if sayi1 == 2.0:
                    print("Gülbatur Öne Geçti!")
                if sayi1 == 3.0:
                    print("Ayşo Öne Geçti!")
                if sayi1 == 4.0:
                    print("Devirhan Öne Geçti!")
                if sayi1 == 5.0:
                    print("Yazıhan Öne Geçti!")
                if sayi1 == 6.0:
                    print("Kasemumkara Öne Geçti!")       
        else:
            time.sleep(3)
            tursayi = 0
            baslat=0
            kazanansayi = random.uniform(1, 6)
            kazanansayi = round(kazanansayi)
            if kazanansayi == 1.0:
                print("Şahbatur Kazandı!\n")
                kazananat = 1
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr         
            elif kazanansayi == 2.0:
                print("Gülbatur Kazandı!\n")
                kazananat = 2
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr       
            elif kazanansayi == 3.0:
                print("Ayşo Kazandı!\n")
                kazananat = 3
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr      
            elif kazanansayi == 4.0:
                print("Devirhan Kazandı!\n")
                kazananat = 4
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr       
            elif kazanansayi == 5.0:
                print("Yazıhan Kazandı!\n")
                kazananat = 5
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr                                       
            elif kazanansayi == 6.0:
                print("Kasemumkara Kazandı!\n")
                kazananat = 6
                if atismi==kazananat:
                    print("Bahisi Kazandınız!\n")
                    kznpr = bahis*20/100
                    print(kznpr,"TL Kazandınız")
                    para = para+kznpr       
    else:
        time.sleep(1)    