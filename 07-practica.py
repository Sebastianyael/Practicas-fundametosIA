import os
import tkinter as tk
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

usuario = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASSWORD')
cluster = os.environ.get('MONGO_CLUSTER')
database = os.environ.get('MONGO_DB')
coleccion = os.environ.get('MONGO_COLLECTION')

conexion = MongoClient(f"mongodb+srv://{usuario}:{password}@{cluster}/")
db = conexion[database]
mi_coleccion = db[coleccion]

ventana = tk.Tk()  
ventana.title("Pantalla inicial")
ventana.geometry("300x200")

def insertar():
    texto = entry.get()
    if texto:  
        documento = {"dato": texto}
        mi_coleccion.insert_one(documento)
        entry.delete(0, tk.END) 
        etiqueta.config(text="¡Dato insertado correctamente!", fg="green")
    else:
        etiqueta.config(text="Escribe algo antes de insertar", fg="red")

entry = tk.Entry(ventana, width=30)
entry.pack(pady=10)

boton = tk.Button(ventana, text="Insertar dato", command=insertar)
boton.pack(pady=20)

etiqueta = tk.Label(ventana, text="Presiona el botón para insertar dato")
etiqueta.pack(pady=10)

ventana.mainloop()