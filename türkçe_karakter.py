#import os 
dosya=input('Türkçe karakterlerini değiştirmek istediğiniz dosyanın yolunu buraya koyalayın: ')

#with open(dosya,"r+") as çeviri:
#    içerik=çeviri.read()
#    print("çeviriliyor...")


yeni=input("oluşturmak istediğiniz yeni dosyanın uzantısıyla birlikte adını giriniz:")
yeni2=(*("/Users/berkcansacakli/Desktop/",yeni))
#yeni2="".join(u for u in yeni2 if u not in (",","'","(",")"))
print(yeni2)
#with open(yeni2,"w") as f:
    #kaynak = "şçöğüıŞÇÖĞÜİ"
    #hedef  = "scoguiSCOGUI"

    #çeviri_tablosu = str.maketrans(kaynak, hedef)
    #içerik=içerik.translate(çeviri_tablosu)
    #print("""çeviri işlemi tamamlandı...
    #yeni dosya oluşturuluyor... """)
    #f.write(içerik)
    
silme=(*("rm -f ",dosya))
    #silme="".join(u for u in silme if u not in (",","'","(",")"))
print(silme)
    #print("dosya oluşturuldu silme işlemine başlanıyor...")
            #os.system(silme)