import subprocess

# Renkli metin oluşturmak için ANSI kaçış dizilerini kullan
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Kullanılabilir araçları ve renklerini bir sözlükte tanımla
tools = {
    "1": {"name": "izlenme.py", "color": colors.BLUE},
    "2": {"name": "ipconfig.py", "color": colors.GREEN},
    "3": {"name": "port.py", "color": colors.BLUE},
    "4": {"name": "videoindirme.py", "color": colors.GREEN},
		"5": {"name: "webip.py", "color": colors.GREEN},
}

# Menüyü göster
print("Kullanılabilir araçlar:")
for key, tool in tools.items():
    print(tool["color"] + key + ". " + tool["name"] + colors.ENDC)

# Kullanıcıdan seçim yapmasını iste
selection = input("Hangi aracı çalıştırmak istiyorsunuz? (1/2/3/4/5): ",colors.HEADER)

# Kullanıcının seçimine göre ilgili aracı çalıştır
if selection in tools:
    tool_name = tools[selection]["name"]
    subprocess.run(["python", tool_name])
else:
    print(colors.FAIL + "Geçersiz seçim!" + colors.ENDC)
