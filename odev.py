def top_tipi(x):
    if x=='B' or x=='b':
        return 0.7
    elif x=='F' or x=='f':
        return 0.75
    elif x=='V' or x=='v':
        return 0.9
    else:    
        print(" HATALI GIRIS YAPTINIZ!!")
        return 0


def top_hareketi(yukseklik , ziplama , katsayi):
    if katsayi==0:
        print("")
    else:
        ziplama = 0
        yukseklik *= 100
        toplam_mesafe = yukseklik
        x = True  
        while x:
            yukseklik = yukseklik * katsayi
            toplam_mesafe += 2 * yukseklik
            ziplama += 1
            
            if yukseklik < 10:
                x = False
                
        print("---------------------------")
        print("Toplam mesafe " , toplam_mesafe/100)
        print("ziplama sayisi" , ziplama)
   
while True:
    yukseklik=int(input("Bir yukselik giriniz(m):"))
    top=input("top tipini giriniz(B/F/V):")[0]
    ziplama=0
    top_hareketi(yukseklik , ziplama , top_tipi(top)) 

    
    
    


    