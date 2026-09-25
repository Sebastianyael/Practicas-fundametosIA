import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

import matplotlib.pyplot as plt
from bson import ObjectId
from dotenv import load_dotenv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

usuario = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASSWORD")
cluster = os.environ.get("MONGO_CLUSTER")
database = os.environ.get("MONGO_DB")
coleccion = os.environ.get("MONGO_COLLECTION")

conexion = MongoClient(f"mongodb+srv://{usuario}:{password}@{cluster}/")
db = conexion[database]
mi_coleccion = db[coleccion]

seleccion = None
datos_locales = []


class AgenteClimatizacion:

    def __init__(self):
        self.temperatura = 0.0
        self.humedad = 0.0
        self.accion = ""

    def percibir(self, temp_str, hum_str):
        self.temperatura = float(temp_str)
        self.humedad = float(hum_str)

    def tomar_decision(self):
        if self.temperatura > 30 and self.humedad > 70:
            self.accion = (
                "Encender aire acondicionado (Modo Deshumidificador)"
            )
        elif self.temperatura > 30:
            self.accion = "Encender ventilador"
        elif self.temperatura < 18:
            self.accion = "Encender calefacción"
        else:
            self.accion = "Mantener sistema apagado"

    def a_documento(self):
        return {
            "accion": self.accion,
            "temperatura": self.temperatura,
            "humedad": self.humedad,
            "fecha": datetime.now(),
        }


def avisar(mensaje, color="gray"):
    estado.config(text=mensaje, foreground=color)


def evaluar():
    agente = AgenteClimatizacion()
    agente.percibir(entryTemp.get(), entryHum.get())
    agente.tomar_decision()
    return agente


def crear():
    try:
        agente = evaluar()
        mi_coleccion.insert_one(agente.a_documento())
        avisar(f"Creado -> {agente.accion}", "green")
        limpiar()
        leer()
    except ValueError:
        avisar("Ingresa valores numéricos válidos.", "red")
    except PyMongoError as error:
        avisar(f"Error de conexión: {error}", "red")


def leer():
    global datos_locales
    try:
        tabla.delete(*tabla.get_children())
        datos_locales = list(mi_coleccion.find().sort("fecha", -1))

        for registro in datos_locales:
            fecha = registro.get("fecha")
            tabla.insert(
                "",
                "end",
                iid=str(registro["_id"]),
                values=(
                    fecha.strftime("%d/%m/%Y %H:%M") if fecha else "-",
                    registro.get("temperatura", "-"),
                    registro.get("humedad", "-"),
                    registro.get("accion", "-"),
                ),
            )

        actualizar_grafico()

    except PyMongoError as error:
        avisar(f"Error de conexión: {error}", "red")


def cargar_seleccion_manual():
    global seleccion
    filas = tabla.selection()
    if not filas:
        avisar("Selecciona primero una fila de la tabla.", "red")
        return
    seleccion = filas[0]
    valores = tabla.item(seleccion, "values")
    entryTemp.delete(0, "end")
    entryTemp.insert(0, valores[1])
    entryHum.delete(0, "end")
    entryHum.insert(0, valores[2])
    avisar(f"Cargado para editar -> {valores[3]}")


def actualizar():
    if seleccion is None:
        avisar(
            "Selecciona un registro y presiona 'Cargar selección'.",
            "red",
        )
        return
    try:
        agente = evaluar()
        mi_coleccion.update_one(
            {"_id": ObjectId(seleccion)},
            {
                "$set": {
                    "temperatura": agente.temperatura,
                    "humedad": agente.humedad,
                    "accion": agente.accion,
                }
            },
        )
        avisar(f"Actualizado -> {agente.accion}", "green")
        limpiar()
        leer()
    except ValueError:
        avisar("Ingresa valores numéricos válidos.", "red")
    except PyMongoError as error:
        avisar(f"Error de conexión: {error}", "red")


def eliminar():
    if seleccion is None:
        avisar(
            "Selecciona un registro y presiona 'Cargar selección'.",
            "red",
        )
        return
    if not messagebox.askyesno(
        "Confirmar", "¿Eliminar el registro seleccionado?"
    ):
        return
    try:
        mi_coleccion.delete_one({"_id": ObjectId(seleccion)})
        avisar("Registro eliminado.", "green")
        limpiar()
        leer()
    except PyMongoError as error:
        avisar(f"Error de conexión: {error}", "red")


def limpiar():
    global seleccion
    seleccion = None
    entryTemp.delete(0, "end")
    entryHum.delete(0, "end")
    tabla.selection_remove(*tabla.selection())


def actualizar_grafico(event=None):
    ax.clear()

    filtro = comboFiltro.get()

    colores_accion = {
        "Encender calefacción": "#d9534f",
        "Encender ventilador": "#f0ad4e",
        "Encender aire acondicionado (Modo Deshumidificador)": "#0275d8",
        "Mantener sistema apagado": "#5cb85c",
    }

    if filtro == "Todas las acciones":
        registros_filtrados = datos_locales
    else:
        registros_filtrados = [
            r for r in datos_locales if r.get("accion") == filtro
        ]

    acciones_presentes = set(r.get("accion") for r in registros_filtrados)

    for accion in acciones_presentes:
        temps = [
            r.get("temperatura", 0)
            for r in registros_filtrados
            if r.get("accion") == accion
        ]
        hums = [
            r.get("humedad", 0)
            for r in registros_filtrados
            if r.get("accion") == accion
        ]
        color = colores_accion.get(accion, "#333333")

        ax.scatter(
            temps,
            hums,
            color=color,
            label=accion,
            edgecolors="black",
            s=50,
            alpha=0.8,
        )

    ax.axvline(x=18, color="blue", linestyle=":", alpha=0.4)
    ax.axvline(x=30, color="red", linestyle=":", alpha=0.4)
    ax.axhline(y=70, color="green", linestyle=":", alpha=0.4)

    ax.set_title(
        f"Gráfica: {filtro}", fontsize=10, fontweight="bold", pad=10
    )
    ax.set_xlabel("Temperatura (°C)", fontsize=8)
    ax.set_ylabel("Humedad (%)", fontsize=8)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.tick_params(axis="both", labelsize=8)

    if registros_filtrados:
        ax.legend(loc="upper left", fontsize=7)

    canvas.draw()


# ------------------------------ INTERFAZ ------------------------------
ventana = tk.Tk()
ventana.title("Agente de Climatización")
ventana.resizable(False, False)

marco = ttk.Frame(ventana, padding=16)
marco.grid(row=0, column=0, sticky="nw")

ttk.Label(marco, text="Temperatura (°C)").grid(row=0, column=0, sticky="w")
entryTemp = ttk.Entry(marco, width=12)
entryTemp.grid(row=1, column=0, sticky="w", pady=(0, 10))

ttk.Label(marco, text="Humedad (%)").grid(row=0, column=1, sticky="w", padx=(12, 0))
entryHum = ttk.Entry(marco, width=12)
entryHum.grid(row=1, column=1, sticky="w", padx=(12, 0), pady=(0, 10))

botones = ttk.Frame(marco)
botones.grid(row=1, column=2, columnspan=2, sticky="e", pady=(0, 10))
ttk.Button(botones, text="Crear", command=crear).grid(row=0, column=0, padx=2)
ttk.Button(
    botones, text="Actualizar", command=actualizar
).grid(row=0, column=1, padx=2)
ttk.Button(botones, text="Eliminar", command=eliminar).grid(row=0, column=2, padx=2)
ttk.Button(botones, text="Limpiar", command=limpiar).grid(row=0, column=3, padx=2)

estado = ttk.Label(marco, text="", foreground="gray")
estado.grid(row=2, column=0, columnspan=4, sticky="w", pady=(0, 8))

tabla = ttk.Treeview(
    marco, columns=("fecha", "temp", "hum", "accion"), show="headings", height=10
)
for columna, titulo, ancho in (
    ("fecha", "Fecha", 120),
    ("temp", "Temp", 60),
    ("hum", "Hum", 60),
    ("accion", "Acción", 250),
):
    tabla.heading(columna, text=titulo)
    tabla.column(columna, width=ancho, anchor="w")
tabla.grid(row=3, column=0, columnspan=4)

# Botón para cargar el registro seleccionado sin usar eventos automáticos
ttk.Button(
    marco, text="Cargar selección", command=cargar_seleccion_manual
).grid(row=4, column=0, columnspan=4, sticky="ew", pady=(8, 0))

# Panel Derecho (Gráfico)
marco_grafico = ttk.Frame(ventana, padding=(10, 16, 16, 16))
marco_grafico.grid(row=0, column=1, sticky="nsew")

ttk.Label(
    marco_grafico, text="Filtrar gráfica por decisión:", font=("Arial", 9, "bold")
).pack(anchor="w", pady=(0, 4))

opciones_filtro = [
    "Todas las acciones",
    "Encender calefacción",
    "Encender ventilador",
    "Encender aire acondicionado (Modo Deshumidificador)",
    "Mantener sistema apagado",
]

comboFiltro = ttk.Combobox(
    marco_grafico, values=opciones_filtro, state="readonly", width=42
)
comboFiltro.current(0)
comboFiltro.pack(anchor="w", pady=(0, 10))

# Botón opcional para actualizar el filtro manualmente sin eventos
ttk.Button(
    marco_grafico, text="Aplicar Filtro Gráfica", command=actualizar_grafico
).pack(anchor="w", pady=(0, 10))

fig, ax = plt.subplots(figsize=(5.5, 4.2), dpi=100)
fig.tight_layout(pad=3.0)

canvas = FigureCanvasTkAgg(fig, master=marco_grafico)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    leer()
    ventana.mainloop()