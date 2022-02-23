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
                print("Yarış Başladı")
                time.sleep(3)
                tursayi+=1
            else:
                sayi1 = random.uniform(1, 6)
                sayi1 = round(sayi1)
                tursayi = tursayi+1
                if sayi1 == 1.0:
                    print("Şahbatur Öne Geçti.")
                    time.sleep(3)
                if sayi1 == 2.0:
                    print("Gülbatur Öne Geçti.")
                    time.sleep(3)
                if sayi1 == 3.0:
                    print("Ayşo Öne Geçti.")
                    time.sleep(3)
                if sayi1 == 4.0:
                    print("Devirhan Öne Geçti.")
                    time.sleep(3)
                if sayi1 == 5.0:
                    print("Yazıhan Öne Geçti.")
                    time.sleep(3)
                if sayi1 == 6.0:
                    print("Kasemumkara Öne Geçti.")
                    time.sleep(3)          
        else:
            tursayi = 0
            kazanansayi = random.uniform(1, 6)
            kazanansayi = round(kazanansayi)
            if kazanansayi == 1.0:
                print("Şahbatur Kazandı\n")
                tursayi = 0
                baslat = 0             
            elif kazanansayi == 2.0:
                print("Gülbatur Kazandı\n")
                tursayi = 0
                baslat = 0
            elif kazanansayi == 3.0:
                print("Ayşo Kazandı\n")
                tursayi = 0
                baslat = 0
            elif kazanansayi == 4.0:
                print("Devirhan Kazandı\n")
                tursayi = 0
                baslat = 0
            elif kazanansayi == 5.0:
                print("Yazıhan Kazandı\n")
                tursayi = 0
                baslat = 0              
            elif kazanansayi == 6.0:
                print("Kasemumkara Kazandı\n")
                tursayi = 0
                baslat = 0
    else:
        time.sleep(1)

#MADE IT MUHAMMED ALİ TETİK