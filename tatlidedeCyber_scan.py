import os  # İşletim sistemi ile etkileşim kurmak için os modülünü içe aktarıyoruz
import subprocess  # Komutları çalıştırmak ve çıktıyı almak için subprocess modülünü içe aktarıyoruz

# Hedef cihazın IP adresi
hedef_ip = "192.168.0.1"

# Ağ taraması işlevi
def ag_taramasi():
    print("Ağ taraması başlatılıyor...")
    # Hedef IP'de belirli portları (21, 22, 80, 139, 445, 3389) taramak için nmap kullanıyoruz
    os.system(f"nmap -sV -p 21,22,80,139,445,3389 {hedef_ip}")

# Traceroute işlevi
def traceroute():
    print("Traceroute başlatılıyor...")
    # Traceroute komutunu çalıştırarak hedef IP'ye giden yolları buluyoruz
    os.system(f"traceroute {hedef_ip}")

# Mesaj gönderme işlevi
def mesaj_gonderme():
    print("Açık port aranıyor...")
    # nmap kullanarak SSH veya FTP portunun açık olup olmadığını kontrol ediyoruz
    sonuc = subprocess.getoutput(f"nmap -p 21,22 {hedef_ip}")
    
    # Nmap çıktısını kontrol ediyoruz
    if "open" in sonuc:
        print("Açık port bulundu! Mesaj gönderiliyor...")
        # Eğer bir açık port bulunursa, hedef cihaza mesaj gönderiyoruz
        os.system(f"echo 'TatlıdedeCyber burada! Güvenlik açığınızı tespit ettim, dikkatli olun!' | ssh user@{hedef_ip}")
    else:
        print("Açık bir SSH veya FTP portu bulunamadı.")  # Açık port yoksa uyarı mesajı

# Ana menü işlevi
def menu():
    while True:
        # Menü seçeneklerini yazdırıyoruz
        print("\n1 - Ağ Taraması")
        print("2 - Traceroute")
        print("3 - Mesaj Gönder")
        print("4 - Çıkış")
        
        # Kullanıcıdan menü seçimi alıyoruz
        secim = input("Bir işlem seçin: ")
        
        if secim == "1":
            ag_taramasi()  # Seçim 1 ise ağ taraması başlatılır
        elif secim == "2":
            traceroute()  # Seçim 2 ise traceroute işlemi başlatılır
        elif secim == "3":
            mesaj_gonderme()  # Seçim 3 ise mesaj gönderme işlemi yapılır
        elif secim == "4":
            print("Çıkış yapılıyor. Bu kadarı yeter hocam!")  # Seçim 4 ise çıkış mesajı yazdırılır
            break  # Döngü sonlandırılır ve program kapanır
        else:
            print("Geçersiz seçim, tekrar deneyin.")  # Geçersiz bir seçim yapılırsa uyarı verir

# Programın ana menüsünü başlatıyoruz
menu()
