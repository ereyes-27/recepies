import certifi
from bson.objectid import ObjectId
from pymongo import MongoClient
from config import config_parser


class RecetaDAO:

    client = MongoClient(host="localhost", port=27017)
    #client = MongoClient(config_parser.get_mongo_cloud_conn(), tlsCAFile=certifi.where())
    db = client.recetas
    recetas = db.Recetas

    def insert(self, receta):
        try:
            print(f"Insertando receta en DAO: {receta}")
            self.recetas.insert_one(receta)
        except Exception as error:
            print(f"Error insertando: {error[0]}")

    def find_all(self):
        try:
            print(f"findAll recetas en DAO")
            result = self.recetas.find()
            return result
        except Exception as error:
            print(f"Error insertando: {error[0]}")

    def get_by_id(self, receta_id):
        return self.recetas.find_one({'_id': ObjectId(receta_id)})

    def get_by_origen(self, origen):
        return self.recetas.find_one({'origen': origen})

    def update_receta(self, receta_id, new_receta):
        entry_status = self.recetas.update_one(receta_id, new_receta)
        print("Resultado del update en DAO ", entry_status)

