öğrenciogrenciler = []

def ogrenci_ekle():
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    numara = input("Öğrencinin numarasını girin: ")
    bolum = input("Öğrencinin bölümünü girin: ")
    not_ort = float(input("Öğrencinin not ortalamasını girin: "))

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Numara": numara,
        "Bölüm": bolum,
        "Not Ortalaması": not_ort
    }
    
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!")

def ogrenci_goruntule():
    if not ogrenciler:
        print("Henüz öğrenci eklenmemiş.")
        return
    for ogrenci in ogrenciler:
        print(ogrenci)

def ogrenci_bul():
    numara = input("Görüntülemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print(ogrenci)
            return
    print("Öğrenci bulunamadı.")

def ogrenci_guncelle():
    numara = input("Bilgilerini güncellemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            ogrenci["Ad"] = input("Yeni ad: ") or ogrenci["Ad"]
            ogrenci["Soyad"] = input("Yeni soyad: ") or ogrenci["Soyad"]
            ogrenci["Bölüm"] = input("Yeni bölüm: ") or ogrenci["Bölüm"]
            ogrenci["Not Ortalaması"] = float(input("Yeni not ortalaması: ") or ogrenci["Not Ortalaması"])
            print("Öğrenci bilgileri güncellendi!")
            return
    print("Öğrenci bulunamadı.")

def ogrenci_sil():
    numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            ogrenciler.remove(ogrenci)
            print("Öğrenci silindi.")
            return
    print("Öğrenci bulunamadı.")

def menu():
    while True:
        print("\nÖğrenci Yönetim Sistemi")
        print("1 - Öğrenci Ekle")
        print("2 - Tüm Öğrencileri Görüntüle")
        print("3 - Öğrenci Ara")
        print("4 - Öğrenci Güncelle")
        print("5 - Öğrenci Sil")
        print("6 - Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-6): ")
        
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_goruntule()
        elif secim == "3":
            ogrenci_bul()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Lütfen 1-6 arasında bir seçim yapın.")

menu()
