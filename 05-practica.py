from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017/"
nombre_db = "bad_prueba_dos"
nombre_col = "usuarios"

cliente = MongoClient(mongo_uri)
db = cliente[nombre_db]
coleccion = db[nombre_col]

registro = {"nombre": "sebastian yael"}
resultado = coleccion.insert_one(registro)

print("Registro insertado con éxito.")