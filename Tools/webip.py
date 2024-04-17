import socket

# Renkli metin oluşturmak için ANSI kaçış dizilerini kullan
class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# Kullanıcıdan hedef web sitesi URL'sini al
website_url = input("Hedef web sitesi URL'sini girin: ")

# Web sitesinin IP adresini bulan fonksiyon
def find_ip_address(website_url):
    try:
        ip_address = socket.gethostbyname(website_url)
        print(colors.GREEN + f"{website_url} web sitesinin IP adresi: {ip_address}" + colors.ENDC)
    except socket.gaierror:
        print(colors.RED + "Host adı çözümlenemedi. Geçerli bir URL girin." + colors.ENDC)

# Web sitesinin IP adresini bul
find_ip_address(website_url)
