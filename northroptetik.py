import random
import time
hp = 1000
northrop = 1000
while 1:
    if northrop<=0:
        print("Kazandınız.\n")
        northrop = 1000
        hp = 1000
    elif hp<=0:
        print("Kaybettiniz.\n")
        northrop = 1000
        hp = 1000
    else:
        print("1| Kritik Hasar\n2| Hasar\n3| Savunma")
        secenek1 = int(input("Yapmak İstediğiniz İşlemi Seçiniz\t:"))
        if secenek1 == 1:
            sans = random.uniform(1, 5)
            sans = round(sans)
            if sans==1.0:
                kritik = random.uniform(100, 500)
                kritik = round(kritik)
                northrop = northrop-kritik
                print(kritik,"Hasar Vurdunuz.")
                print(northrop,"Canı Kaldı\n")
                time.sleep(5)
                nthasar = random.uniform(10, 200)
                nthasar = round(nthasar)
                hp = hp-nthasar
                print(nthasar,"Hasar Aldınız")
                print(hp,"Canınız Kaldı\n")
            else:
                print("Hasar Vuramadınız.\n")
                time.sleep(5)
                nthasar = random.uniform(10, 200)
                nthasar = round(nthasar)
                hp = hp-nthasar
                print(nthasar,"Hasar Aldınız")
                print(hp,"Canınız Kaldı\n")
        elif secenek1 == 2:
            hasar = random.uniform(20, 250)
            hasar = round(hasar)        
            northrop = northrop-hasar
            print(hasar,"Hasar Vurdunuz.")
            print(northrop,"Canı Kaldı\n")
            time.sleep(5)
            nthasar = random.uniform(10, 200)
            nthasar = round(nthasar)
            hp = hp-nthasar
            print(nthasar,"Hasar Aldınız")
            print(hp,"Canınız Kaldı\n")
        else:
            time.sleep(5)
            nthasar = random.uniform(10, 200)
            nthasar = round(nthasar)
            koruma = random.uniform(10, 100)
            koruma = round(koruma)
            nthasar = nthasar-nthasar*koruma/100
            print(nthasar,"Hasar Aldınız")
            print(hp,"Canınız Kaldı\n")

#MUHAMMED ALİ TETİK