import tkinter as tK
from tkinter import messagebox
from dotenv import load_dotenv
from pymongo import MongoClient
import os

ventana = tK.Tk()
ventana.title("Agente de detección de humedad")
ventana.geometry("320x300")
load_dotenv()

usuario = os.environ.get('MONGO_USER')
password = os.environ.get('MONGO_PASSWORD')
cluster = os.environ.get('MONGO_CLUSTER')
database = os.environ.get('MONGO_DB')
coleccion = os.environ.get('MONGO_COLLECTION')

conexion = MongoClient(f"mongodb+srv://{usuario}:{password}@{cluster}/")
db = conexion[database]
mi_coleccion = db[coleccion]

class AgenteClimatizacion:
    def __init__(self):
        self.temperatura = 0.0
        self.humedad = 0.0
        self.accion = ""

    def percibir(self, temp_str, hum_str):
        """Captura y convierte los datos del entorno."""
        self.temperatura = float(temp_str)
        self.humedad = float(hum_str)

    def tomar_decision(self):
        """Aplica la regla condición-acción basada en la percepción."""
        if self.temperatura > 30 and self.humedad > 70:
            self.accion = (
                "Encender aire acondicionado (Modo Deshumidificador)"
            )
        elif self.temperatura > 30:
            self.accion = "Encender ventilador"
        elif self.humedad > 30:
            self.accion = "Encender calefacción"
        else:
            self.accion = "Mantener sistema apagado"

    def mostrar_resultado(self):
        """Muestra el estado del agente y la acción a realizar."""
        print("--- RESUMEN DEL AGENTE ---")
        print(
            f"Percepción -> Temp: {self.temperatura}°C | Humedad:"
            f" {self.humedad}%"
        )
        print(f"Acción -> {self.accion}")
        documento = {"accion" : self.accion, "temperatura" : self.temperatura, "humedad" : self.humedad}
        mi_coleccion.insert_one(documento)

labelTemp = tK.Label(ventana, text="Temperatura actual (°C):")
labelTemp.pack(pady=(10, 0))
entryTemperatura = tK.Entry(ventana, width=25)
entryTemperatura.pack(pady=5)

labelHum = tK.Label(ventana, text="Humedad actual (%):")
labelHum.pack(pady=(10, 0))
entryHumedad = tK.Entry(ventana, width=25)
entryHumedad.pack(pady=5)

labelResultado = tK.Label(
    ventana, text="", fg="blue", wraplength=280, justify="center"
)

def ejecutar_agente():
    try:
        agente = AgenteClimatizacion()
        agente.percibir(entryTemperatura.get(), entryHumedad.get())
        agente.tomar_decision()
        agente.mostrar_resultado()
        labelResultado.config(text=f"Acción: {agente.accion}")
    except ValueError:
        messagebox.showerror(
            "Error", "Por favor, ingresa valores numéricos válidos."
        )

btnEvaluar = tK.Button(ventana, text="Evaluar Agente", command=ejecutar_agente)
btnEvaluar.pack(pady=15)
labelResultado.pack(pady=5)

if __name__ == "__main__":
    ventana.mainloop()