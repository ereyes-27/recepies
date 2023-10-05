from bson.objectid import ObjectId
from pymongo import MongoClient

class RecetaDAO:
   client = MongoClient(host="localhost", port=27017)

   def insert(self, receta):
      try:
         print(f"Insertando receta en DAO: {receta}")
         #client = MongoClient(host="localhost", port=27017)
         #print("se obtubo instancia de mongo client")
         db =  self.client.recetas
         recetasCollection = db.Recetas

         recetasCollection.insert_one(receta)

         #print('insertado: '+receta['nombre'])

      except Exception as error:
        print(f"Error insertando: {error[0]}")


   def findAll(self):
      try:
         print(f"findAll recetas en DAO")
         #print("se obtuvo instancia de mongo client")
         db =  self.client.recetas
         recetasCollection = db.Recetas

         result = recetasCollection.find()

         return result

      except Exception as error:
        print(f"Error insertando: {error[0]}")
           
   def getById(self, id):
      db = self.client.recetas
      recetasCollection = db.Recetas
      queryresult = recetasCollection.find_one({'_id': ObjectId(id)})
      #print("Query Result:")
      #print(queryresult)
      return queryresult

   def updateReceta(self, id, new_receta):
      db = self.client.recetas
      recetasCollection = db.Recetas
      entry_status = recetasCollection.update_one(id, new_receta)
      print("Resultado del update en DAO ", entry_status)
       

#if __name__ == '__main__':
#   print("running dao")
   #recetaDAO = RecetaDAO()
   #recetaDAO.getById('64251143196bb6f1be3136de')

   #receta = {'_id':'Recetas",
   #          'nombre':'recetaTest'
   #         }
   #recetaDAO.insert(receta)



