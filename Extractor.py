import multiprocessing
import openai
#import datetime
import json
from Extractor_davinci03 import Extractor_Davinci
from config import config_parser

class Extractor:
    openai.api_key = config_parser.get_open_ai_key()
    davinci = Extractor_Davinci()

    # Función para llamar a la API de ChatGPT
    def call_chatgpt(self, prompt, salida):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto de cocina y debes deducir datos de un texto"},
                {"role": "user", "content": prompt}
            ]
        )
        # Extrae la respuesta del modelo de ChatGPT
        message = response['choices'][0]['message']
        content = message['content']
        salida.append(content)

    """
    obtiene el json a partir de la receta de texto
    """
    def getJSonFromReceta(self, origen, texto, nomImagen):
        # Lista de prompts para ChatGPT
        prompts = [
            "Infiere en español el nombre de Receta, retorna unicamente en formato JSON válido, retorna la estructura: RecetaNombre:? del texto:" + texto,
            "Infiere en español lista de pasos enumerados,retorna unicamente en formato JSON válido, retorna la estructura: Pasos:['paso':?] del texto:" + texto,
            "Infiere lista de Ingredientes en español, retorna en español y unicamente en formato JSON válido, retorna la estructura: Ingredientes:[{Ingrediente:?, Cantidad:?}. Retorna números como cadenas de texto del texto:" + texto,
            # Agrega aquí más prompts para ChatGPT
        ]
        salida = multiprocessing.Manager().list()

        # Crea un pool de procesos con el número de procesos deseados
        # Puedes ajustar el valor de `processes` a la cantidad de procesos que deseas utilizar
        with multiprocessing.Pool(processes=3) as pool:
            # Llama a la función `call_chatgpt` en paralelo con los prompts usando el pool de procesos
            # La función `map` mapea la lista de prompts a la función `call_chatgpt` y las ejecuta en paralelo
            pool.starmap(self.call_chatgpt, [(prompt, salida) for prompt in prompts])
        #print("find:")
        #print(datetime.datetime.now())

        jsonIngredientes = []
        jsonNombre = ""
        jsonPasos = ""
        pasos = ""
        for s in salida:
            #print(type(s))
            #print(s)
            #limpiando la cadena de texto cuando incluye texto antes del JSON
            if "JSON:" in s:
                s = s[s.find('JSON') + 5:]

            if "Ingredientes" in s:
                try:
                   json_object = json.loads(s)
                   jsonIngredientes = json_object['Ingredientes']
                except Exception as e:
                    print(f"Ingredientes error en el parser: {s}")
                    print("Error "+ str(e))
                    if '```' in s:
                        tmp = s[s.find('```'):]
                        #print("tmp de ingredientes: " +tmp)
                        try:
                           jsonIngredientes = json.loads(tmp)
                        except Exception as e:
                            print(str(e))
            elif "Ingrediente" in s:
                try:
                    json_object = json.loads(s)

                    if type(json_object) is list:
                        jsonIngredientes = json_object
                    else:
                        print("No se pudo identificar el tipo de dato en ingredientes")

                except Exception as e:
                    print("Error parseando Ingrediente como lista")
                    print("Error: "+ str(e))


            #elif type(s) is list and len(s) > 0 and "Ingrediente" in s[0]:
            #    jsonIngredientes = s
            #    print("los ingredientes son una lista!!!!")

            elif "RecetaNombre" in s:
                try:
                   tmp = s.replace(",","")
                   json_object = json.loads(tmp)
                   jsonNombre = json_object['RecetaNombre']
                   print(f"Parseo correcto del   nombre {jsonNombre}")
                except:
                   print(f"json exception parser RecetaNombre:{tmp}")
                   jsonNombre = tmp[tmp.find('RecetaNombre')+14:tmp.find('}')]

            elif "Pasos" in s:
                try:
                   s = s.replace("Paso","paso")
                   json_object = json.loads(s)
                   jsonPasos = json_object['pasos']

                   if len(jsonPasos) > 0:
                       for paso in jsonPasos:
                           pasos += paso['paso'] + "\n"
                except Exception as e:
                   print(f"Parser error  en pasos:{s}")
                   print('Error: ' + str(e))
            elif "Paso" in s or "paso" in s:
                try:
                    s = s.replace("Paso", "paso")
                    jsonPasos = json.loads(s)

                    if type(jsonPasos) is list:
                        if "Pasos" in json_object[0]:
                            jsonPasos= json_object[0]['pasos']
                    else:
                            jsonPasos = json_object[0]

                    if len(jsonPasos) > 0:
                        for paso in jsonPasos:
                            pasos += paso['paso'] + "\n"
                except Exception as e:
                    print("Error al extraer los pasos "+ str(e))

        dataDB = {"origen": origen, "nombre": jsonNombre, "pasos": pasos, "ingredientes": jsonIngredientes, 'img': nomImagen}
        return dataDB

