import re
import ssl
import yt_dlp

class YouTubeUtil:
    """
    Descarga el video de YouTube y retorna el nombre del video descargado
    """
    def descargaVideo(self, video_url):
        ssl._create_default_https_context = ssl._create_unverified_context
        #print(f"{datetime.datetime.now()}  YoutubeUtil ")
        if "https://www.youtube.com/watch?v=" in video_url:
            file = video_url.replace("https://www.youtube.com/watch?v=","")+".mp4"
        #https://youtube.com/shorts/GdH7K0S0gw8?feature=share
        elif "https://youtube.com/shorts/" in video_url:
            file = video_url.replace("https://youtube.com/shorts/","")
            file = file.replace('?feature=share','')
            file = file+".mp4"

        file ="videos/"+file

        ydl_opts = {
            'ignoreerrors': True,
            'outtmpl': file,
            'format': 'mp4',
            'f': '22'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(video_url)
            #print("Resultado de la descarga: ")

            if error_code > 0:
                raise ValueError("Error en la descarga del video, URL no válida")
        return file

    def validaURL(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None
