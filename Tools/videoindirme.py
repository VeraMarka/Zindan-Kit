from pytube import YouTube

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download()
        print(colors.GREEN + "Video başarıyla indirildi!" + colors.ENDC)
    except Exception as e:
        print(colors.RED + "Video indirilirken bir hata oluştu: " + str(e) + colors.ENDC)

video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")

download_video(video_url)
