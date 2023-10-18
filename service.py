import sys, os
from RecetaDAO import RecetaDAO
from RecetaMapper import *
import pandas as pd
import io

from YouTubeUtil import YouTubeUtil
from WhisperUtil import WhisperUtil
from Extractor import Extractor
from ImgUtil import ExtractImg
from CleanerUtil import CleanerUtil

youTubeUtil = YouTubeUtil()
whisperUtil = WhisperUtil()
extractor = Extractor()
imgExtractor = ExtractImg()
cleanerUtil = CleanerUtil()


class Service:

   dao = None
   mapper = None

   def __init__(self):
      print("Servicio inicializado")
      self.dao = RecetaDAO()
      self.mapper = recetaMapper()

   def find_all(self):
      return self.dao.find_all()

   def download_video(self, url):
      print("Descargando video")
      if (youTubeUtil.validaURL(url)):
         return youTubeUtil.descargaVideo(url)
      else:
         raise ValueError('La URL de descarga no es válida!!')

   def procesar_video(self, url):
      print(f"Procesando video {url}")
      if self.dao.get_by_origen(url):
         print("Video ya procesado")
         return (True,"")

      #Descaarga el video de YouTube
      file = ""
      try:
         file = self.download_video(url)
      except Exception as e:
         print("Error descangando el video: ")
         print(e)
         return (False, "Error descargando el video: "+ url + " Motivo: "+str(e))
      #Transcribe el texto uisando Whisper
      if len(file) <= 0:
         return (False, "Error en la descarga del video")
      texto = whisperUtil.transcribe(file)
      texto= cleanerUtil.cleanTxt(texto)
      print(f"Longitud del texto a consultar: {len(texto)}")

      if len(texto) < 350:
         return(False, "No se identificó voz en el video")

      #if len(texto) > 3800:
      #   return(False,"El video es muy largo, por el momento no se puede procesar")

      nomImagen = imgExtractor.extraerImgFromMp4(file)
      print(texto)
      #ingredientes = extractor.extraeIngredientes(texto)
      #Consulta a chatgpt y formatea a json
      try:
         JSON = extractor.getJSonFromReceta(url, texto, nomImagen)
         self.dao.insert(JSON)
         self.exporta_a_excel(JSON, False)
         self.dao.exporta_db()
      except Exception as err:
         print(f"Error al extraer la receta {str(err)}")
         return(False, "El video parese ser muy largo, intente con otro.")
      return (True,"")

   def exporta_a_excel(self, json, multiple=True):
      #aqui se exporta a excel
      excel_json = json if multiple else self.procesa_json_para_excel(json)
      exportar = pd.DataFrame(excel_json)
      buffer = io.BytesIO()
      exportar.to_excel(buffer, index=False)
      return buffer

   def find_by_id(self, id):
      return self.dao.get_by_id(id)

   def update_receta(self, form):
      try:
         json = self.mapper.mapToJson(form)
         print("resultado del mapper: ", json[0], json[1])
         self.dao.update_receta(json[0], json[1])
         self.dao.exporta_db()
         return True
      except Exception as error:
         print("Error actualizando receta:", str(error))
         return False

   def procesar_video_file(self, file):
      print(f"Procesando video x File: {file}")
      if self.dao.get_by_origen(file):
         print("Video ya procesado")
         return (True,"")

      texto = whisperUtil.transcribe(file)
      texto= cleanerUtil.cleanTxt(texto)
      print(f"Longitud del texto a consultar: {len(texto)}")

      if len(texto) < 350:
         return(False, "No se identificó voz en el video")

      if len(texto) > 3500:
         return(False,"El video es muy largo, por el momento no se puede procesar")

      nomImagen = imgExtractor.extraerImgFromMp4(file)
      print(texto)
      #ingredientes = extractor.extraeIngredientes(texto)
      #Consulta a chatgpt y formatea a json
      try:
         JSON = extractor.getJSonFromReceta(texto, nomImagen)
         self.dao.insert(JSON)
         self.dao.exporta_db()
      except Exception as err:
         print(f"Error llamando a ChatGPT: {str(err)}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         print(exc_type, fname, exc_tb.tb_lineno)
         return(False,"Hubo una excepción en la extracción de la receta, favor de intentar más tarde ")
      return (True,"")

   def procesa_json_para_excel(self, json_data):
      excel_json = {
         'nombre': [json_data["nombre"]],
         'pasos': [json_data["pasos"]],
         'ingredientes': [json_data["ingredientes"]],
         'url': [json_data["origen"]]
         }
      return excel_json
