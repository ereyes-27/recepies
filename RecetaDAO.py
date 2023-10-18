import json
import certifi
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson import json_util
from pymongo import MongoClient
from config import config_parser


class RecetaDAO:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RecetaDAO, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        client = MongoClient(host="localhost", port=27017)
        #client = MongoClient(config_parser.get_mongo_cloud_conn(), tlsCAFile=certifi.where())
        db = client.recetas
        self.recetas = db.Recetas
        self.db_json = 'mongodb/data/recetas.Recetas.json'
        self.init_db()

    def init_db(self):
        with open(self.db_json) as file:
            file_data = json.load(file)
        load = json.loads(json_util.dumps(file_data))
        for row in load:
            found = self.get_by_id(row['_id']['$oid'])
            row['_id'] = ObjectId(row['_id']['$oid'])
            if found is None:
                self.recetas.insert_one(row)

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

    def exporta_db(self):
        # cursor = self.recetas.find({})
        # with open(self.db_json, 'w') as file:
        #     json.dump(json.loads(dumps(cursor)), file)
        cursor = self.recetas.find()
        list_cur = list(cursor)
        json_data = dumps(list_cur)
        with open(self.db_json, 'w') as file:
            file.write(json_data)
