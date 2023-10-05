import json

from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
from service import Service


service = Service()
app = Flask(__name__)


@app.route('/')
def index():
    #print("Probando servicios")
    return render_template('index.html')

@app.route('/formulario')
def formulario():
   return render_template('formulario.html')

@app.route('/procesaReceta', methods=['POST', 'GET'])
def procesarReceta():
    print(request.method)
    if request.method == 'POST':
       form = request.form
       url = form['url']
       print("Descargar video de URL o file: "+url)
       resp = service.procesarVideo(url)

       if resp[0]:
           print("listar recetas")
           return listRecetas()
       else:
           return render_template('errorProceso.html', err = resp[1])

    else:
        print("El metodo metodo fue get??")
    return listRecetas()

@app.route('/listRecetas', methods=['POST', 'GET'])
def listRecetas():
   print("__________Listado de recetas _________")
   result = service.findAll()
   mod_dict = {}
   tl = ['  ', '  Receta  ', 'Ingredientes']



   for document in result:

        #print("Tipo de ingredienes" + document['nombre'])
        #print(type(document))
        ingredientes = []
        #print(type(document['ingredientes']))

        for ingrediente in document['ingredientes']:
            #print(type(ingrediente))
            #print("es diccionario")
            ingTmp = ""
            if (type(ingrediente)) is dict:
                for ing in ingrediente:
                    #print(ingrediente['Ingrediente'])
                    #print(ingrediente['Cantidad'])
                    ingTmp = str(ingrediente['Ingrediente']) + " " + str(ingrediente['Cantidad'])
            else:
                #ingrediente = json.loads(ingrediente)
            #print(ing_tmp + " "+ cant_tmp)
                try:
                   if type(ingrediente) is str:
                      #print(f"imprimiendo document-[ingrediente] {ingrediente}")

                      #print(document[ingrediente])
                      ingTmp = ingrediente
                   else:
                       print("La estructura del ingrediente no se pudo identificar")

                except:
                    print(f"no se puede parsear los ingredientes: {ingrediente}")
            #ingTmp = ing_tmp + " " + cant_tmp
            #print("Insertando en lista"+ ingTmp)
            ingredientes.insert(0,ingTmp)
        mod_dict[document['_id']] = {'nombre': document['nombre'], 'ingredientes': ingredientes, 'img':document['img']}
        #print(mod_dict)

   return render_template('listRecetas.html', dict=mod_dict, headings=tl)


@app.route('/recetaEdit/<id>', methods=['GET'])
def recetaEdit(id):

    #result = request.form
    result = service.findById(id)


    ingredientes = result['ingredientes']

    ingredientesHTML = []
    #<label for="ingrediente">Ingrediente:</label>
	#<input type="text" id="ingrediente" name="ingrediente" value="{{ ing['ingrediente'] }}">
    i = 0;
    for ing in ingredientes:
        html = "<label>Ingrediente:</label>"
        html += "<input type='text' name='ingrediente_" +str(i) + "' value='" + str(ing['Ingrediente'])+"' maxlength='50'>"
        html += "&nbsp;&nbsp;&nbsp;<label>Cantidad:</label>"
        html += "<input type='text' name='cantidad_"+str(i)+"' value='" + str(ing['Cantidad']) + "'}} maxlength='50'>"
        html += "<br/>"
        ingredientesHTML.insert(len(ingredientesHTML), html)

        i = i + 1;


    return render_template('editReceta.html',id=id, obj=result, html=ingredientesHTML)

@app.route('/updateReceta', methods=['POST'])
def recetaUpdate():
    print("update receta")
    msg = "La receta ha sido actualizada"

    if request.method == 'POST':
        form = request.form
        #print("imprimiendo el Form de update")
        #print(form)

        res = service.updateReceta(form)
        if res is False:
            msg = "Hubo un problema al actualizar los datos."
        
    
    return render_template('updateResult.html', msg = msg)

@app.route('/acerca', methods=['GET'])
def acerca():
    return render_template('acerca.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        fileName = "videos/"+f.filename
        f.save(fileName)
        resp = service.procesarVideoFile(fileName)
        if resp[0]:
            print("listar recetas")
            return listRecetas()
        else:
            return render_template('errorProceso.html', err=resp[1])

    return listRecetas()


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)
    #app.run(host='localhost', port=5001, debug=False)


