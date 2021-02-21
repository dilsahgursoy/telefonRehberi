def DosyaAc(adres,param):
    from os.path import exists
    if exists(adres):
        if param==1:
            return open(adres,"r+",encoding="UTF-8")
        if param==2:
            return open(adres,"a+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")
dosya=DosyaAc(r"C:\Users\90536\Desktop\kursTekrar\telefonDefteri.csv",1)
sayi=int(input("Rehbere kaç kişi eklemek istiyorsunuz?"))
for item in range(sayi):
    kisiAdi=input("Kisinin adini giriniz:")
    kisiSoyadi=input("Kisinin soyadini giriniz:")
    def TelNoKontrol():
        if len(telNo)==11:
            return telNo
        else:
            print("Geçerli bir telefon numarası giriniz.")    
    telNo=input("Telefon numarasini giriniz:")
    liste=[kisiAdi,kisiSoyadi,telNo]
    kayit=";".join(liste)+"\n"
    dosya.write(kayit)
    dosya.flush()
    dosya.seek(0)
    print(*dosya.readlines())
    print("Kisi eklendi.")

