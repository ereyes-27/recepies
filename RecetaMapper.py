#Mapea los datos del HttpRequest a un objeto tipo RecetaDTO
from RecetaDTO import *
from bson.objectid import ObjectId
class recetaMapper:
    recetaDTO = None
    def map(self, form):
        recetaDTO = RecetaDTO()
        recetaDTO.nombre = form['nombre']
        return recetaDTO

    def mapToJson(self, form):
        id = form['id']
        nomReceta = form['nombre']
        pasos = form['pasos']
        pasos = pasos.strip()

        ingredientes = []
        i = 0;
        for element in form:
            if 'ingrediente' in str(element):
               print("element:"+ str(element))
               sufix = element[len('ingrediente'):]
               #print("sufijo: ", sufix )
               cantidad = "cantidad"+sufix
               strCantidad = form[cantidad]
               ingredientes.insert(i, {'Ingrediente':form[element], 'Cantidad':strCantidad})
               i += 1

        print("_______________________________________________")
        print(ingredientes)


        dataDB = {"nombre": nomReceta, "pasos": pasos, "ingredientes": ingredientes}

        return ({'_id':  ObjectId(id)}, {"$set": dataDB })
