import openai
import multiprocessing
import json


class Extractor_Davinci:
    openai.api_key = "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"  # reemplaza esto con tu propia clave de API de OpenAI

    def extraeIngredientes(self, texto):
        print("_extraer ingredientes_")

    """
    Llamada al API ChatGPT
    parametros:
    texto: todo el texto que proviene de whisper
    prompt: las instrucciones que debe realizar
    return_dict un diccionario tipo global donde se almacenarán el resultado
    key: identificador
    """
    def callOpenAIAPI(self, texto, prompt, return_dict):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt + "'" + texto + "'",
            temperature=0,
            max_tokens=3000,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )
        print("respuesta del call chatgpt")
        print(type(response))
        print(response)
        res = response['choices'][0]['text']
        print("Obteniendo la respuesta de davinci: ")
        print(res)
        return res

    """
       obtiene el json a partir de la receta de texto
    """
    def getJSonFromReceta(self, texto, nomImagen):
        #declaracion de los prompts
        ingredientes = "Obtener lista de Ingredientes con Porciones en formato JSON, retornar los campos Ingredientes, Ingrediente, Cantidad"
        pasos = "Obtener lista de la receta de pasos enumerados, Nombre de la Receta en formato JSON, usar los campos Nombre, Pasos:"
        #prepara los objetos para el multiproceso
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        jobs = []
        tasks = [ingredientes, pasos]
        for task in tasks:
            p = multiprocessing.Process(target=self.callOpenAIAPI, args=(texto, task, return_dict, tasks.index(task)))
            jobs.append(p)
            p.start()

        #print("Inicio:")
        #print(datetime.datetime.now())
        #for proc in jobs:
        #    proc.join()
        #print("Fin:")

        #print(datetime.datetime.now())
        #print(return_dict.values())

        result = return_dict.values()

        txtReceta = ""
        txtPasos = ""
        dataDBIng = []

        for r in result:
            print("__________buscando en result_________________:"+r[0])
            print(type(r))
            print(r)
            if r.find("JSON:") > 0:
                print("Removiendo cadena JSON")
                r = r.replace("JSON:","")
            if r.find("Ingredientes:") > 0:
                #print("Removiendo caneba JSON")
                #r = r.replace("JSON:","")
                r = r.replace("\n","")

            json_object = json.loads(r)
            if "Nombre" in json_object:
                txtReceta = json_object['Nombre']
            if "Nombre de la receta" in json_object:
                txtReceta = json_object['Nombre de la receta']

            if "Pasos" in json_object:
                txtPasos = json_object['Pasos']

            if "Ingredientes" in json_object:
                dataDBIng = json_object['Ingredientes']

            pasos = "";
            if len(txtPasos) > 0:
                for paso in txtPasos:
                   paso = paso.strip().replace('\t','')

                   if len(pasos) > 0:
                       pasos += paso+ '\n'
                   else :
                       pasos += paso


            if type(json_object) is list:
                #print("Buscando la lista de ingredientes: " + str(len(json_object)))
                dataDBIng = json_object
                #for obj in json_object:
                #    print(obj['Ingrediente'] + " " + obj['Cantidad'])

        dataDB = {"nombre": txtReceta, "pasos": pasos, "ingredientes": dataDBIng, 'img': nomImagen}
        return dataDB


    def callDavinci(self, tipoConsulta, texto):
        prompt = ""
        respuesta = ""
        match tipoConsulta:
            case "Nombre":
                prompt = "Deduce en español el nombre de Receta, retorna unicamente en formato JSON válido, retorna la estructura: RecetaNombre:? del texto:" + texto

            case "Ingredientes":
                print("Ingredientes")
                prompt = "Deduce ingredientes retorna formato JSON: Ingredientes:[{Ingrediente:?, Cantidad:?} de:" + texto
            case "Pasos":
                print("Paasos")
                "Deduce en español lista de pasos enumerados,retorna unicamente en formato JSON válido, retorna la estructura: Pasos:['paso':?] del texto:" + texto
            case _:
                print("La consulta no es viable")
                return ""

        respuesta = self.callOpenAIAPI(texto,prompt, respuesta)
        return respuesta


