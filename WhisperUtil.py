import whisper
import ssl
import datetime

class WhisperUtil:
    ssl._create_default_https_context = ssl._create_unverified_context

    def transcribe(self, audio_file):
        print("Iniciando transcripción con Whisper:" +audio_file)

        model = whisper.load_model("base")
        texto = model.transcribe(audio_file, fp16=False)

        print(f"{datetime.datetime.now()} finalizo transcripción de video___")
        print(texto['text'])
        return texto['text']
"""
w = WhisperUtil()
w.transcribe("videos/_HNfyo0fj6o.mp4")
"""