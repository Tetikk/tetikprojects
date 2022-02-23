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
while 1:
    if baslat == 0:
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
            elif kazanansayi == 2.0:
                print("Gülbatur Kazandı!\n")
            elif kazanansayi == 3.0:
                print("Ayşo Kazandı!\n")
            elif kazanansayi == 4.0:
                print("Devirhan Kazandı!\n")
            elif kazanansayi == 5.0:
                print("Yazıhan Kazandı!\n")           
            elif kazanansayi == 6.0:
                print("Kasemumkara Kazandı!\n")
    else:
        time.sleep(1)

#MADE IT MUHAMMED ALİ TETİK