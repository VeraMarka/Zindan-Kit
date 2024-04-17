import socket

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

target = input("Hedef IP adresi veya alan adını girin: ")

def port_scan(target, start_port, end_port):
    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(colors.GREEN + "Port {} açık".format(port) + colors.ENDC)
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        print("\nTarama kullanıcı tarafından iptal edildi.")
        exit()
    except socket.gaierror:
        print(colors.RED + "Host adı çözümlenemedi." + colors.ENDC)
        exit()
    except socket.error:
        print(colors.RED + "Bağlantı hatası." + colors.ENDC)
        exit()
    
    print("Tarama tamamlandı.")
    if not open_ports:
        print("Hedefte açık port bulunamadı.")
    else:
        print("Açık portlar:", open_ports)

start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

port_scan(target, start_port, end_port)
