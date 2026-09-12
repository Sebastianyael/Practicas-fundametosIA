import random
import math
import os
import tkinter as tk

ventana = tk.Tk()
ventana.title("Sistema de Diagnóstico Médico")
ventana.geometry("700x750")
ventana.configure(bg="gray")

label_nombre = tk.Label(ventana, text="Nombre:", bg="gray", fg="black")
label_nombre.pack(pady=1)
caja_nombre = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_nombre.pack(pady=1)

label_sexo = tk.Label(ventana, text="Sexo (masculino/femenino):", bg="gray", fg="black")
label_sexo.pack(pady=1)
caja_sexo = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_sexo.pack(pady=1)

label_peso = tk.Label(ventana, text="Peso (kg):", bg="gray", fg="black")
label_peso.pack(pady=1)
caja_peso = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_peso.pack(pady=1)

label_altura = tk.Label(ventana, text="Altura (m):", bg="gray", fg="black")
label_altura.pack(pady=1)
caja_altura = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_altura.pack(pady=1)

label_medicamento = tk.Label(ventana, text="¿Consumiendo medicamento? (si/no):", bg="gray", fg="black")
label_medicamento.pack(pady=1)
caja_medicamento = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_medicamento.pack(pady=1)

label_med_elegido = tk.Label(ventana, text="Nº Medicamento (1-5):", bg="gray", fg="black")
label_med_elegido.pack(pady=1)
caja_med_elegido = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_med_elegido.pack(pady=1)

label_tabaco = tk.Label(ventana, text="¿Consumes tabaco? (si/no):", bg="gray", fg="black")
label_tabaco.pack(pady=1)
caja_tabaco = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_tabaco.pack(pady=1)

label_alcohol = tk.Label(ventana, text="¿Consumes alcohol? (si/no):", bg="gray", fg="black")
label_alcohol.pack(pady=1)
caja_alcohol = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_alcohol.pack(pady=1)

label_actividad = tk.Label(ventana, text="Actividad física (1:Sedentario, 2:Ligeramente, 3:Moderadamente, 4:Muy):", bg="gray", fg="black")
label_actividad.pack(pady=1)
caja_actividad = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_actividad.pack(pady=1)

label_fiebre = tk.Label(ventana, text="Fiebre (s/n):", bg="gray", fg="black")
label_fiebre.pack(pady=1)
caja_fiebre = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_fiebre.pack(pady=1)

label_tos = tk.Label(ventana, text="Tos (s/n):", bg="gray", fg="black")
label_tos.pack(pady=1)
caja_tos = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_tos.pack(pady=1)

label_cabeza = tk.Label(ventana, text="Dolor de cabeza (s/n):", bg="gray", fg="black")
label_cabeza.pack(pady=1)
caja_cabeza = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_cabeza.pack(pady=1)

label_pecho = tk.Label(ventana, text="Dolor de pecho (s/n):", bg="gray", fg="black")
label_pecho.pack(pady=1)
caja_pecho = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_pecho.pack(pady=1)

label_fatiga = tk.Label(ventana, text="Fatiga (s/n):", bg="gray", fg="black")
label_fatiga.pack(pady=1)
caja_fatiga = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_fatiga.pack(pady=1)

label_estomago = tk.Label(ventana, text="Dolor de estómago (s/n):", bg="gray", fg="black")
label_estomago.pack(pady=1)
caja_estomago = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_estomago.pack(pady=1)

label_mareo = tk.Label(ventana, text="Mareo (s/n):", bg="gray", fg="black")
label_mareo.pack(pady=1)
caja_mareo = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_mareo.pack(pady=1)

label_orinar = tk.Label(ventana, text="Molestia al orinar (s/n):", bg="gray", fg="black")
label_orinar.pack(pady=1)
caja_orinar = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_orinar.pack(pady=1)

label_articular = tk.Label(ventana, text="Dolor articular (s/n):", bg="gray", fg="black")
label_articular.pack(pady=1)
caja_articular = tk.Entry(ventana, width=40, bg="gray80", fg="black")
caja_articular.pack(pady=1)

salida = tk.Text(ventana, font=("Courier New", 9), height=12, state="disabled", bg="gray80", fg="black")

niveles_de_actividad_fisica = {
    "Sedentario": "Estilo de vida principalmente sentado o acostado (trabajo de escritorio, ver televisión, conducir).",
    'Ligeramente activo (1 a 3 días por semana)': 'Ejercicio suave o caminatas periódicas integradas en la rutina semanal.',
    "Moderadamente activo": "Ejercicio estructurado de intensidad media-alta llevado a cabo de forma regular.",
    "Muy activo": "Entrenamiento de alta intensidad casi diario o un empleo que requiere esfuerzo físico constante."
}

medicamentos_lista = {
    "1": "Paracetamol",
    "2": "Ibuprofeno",
    "3": "Ketorolaco",
    "4": "Omeprazol",
    "5": "Loratadina"
}

numero_diagnostico = random.randint(1, 10)

def diagnosticar():
    nombre = caja_nombre.get()
    sexo = caja_sexo.get()
    
    try:
        peso = float(caja_peso.get())
        altura = float(caja_altura.get())
    except ValueError:
        return

    medicamento = caja_medicamento.get()

    medicamento_consumido = "Ninguno"
    consumiendo_medicamento = medicamento == 'si'
    if consumiendo_medicamento:
        medicamento_elejido = caja_med_elegido.get()
        if medicamento_elejido in medicamentos_lista:
            medicamento_consumido = medicamentos_lista[medicamento_elejido]

    tabaco = caja_tabaco.get()
    alcohol = caja_alcohol.get()
    opcion_nivel_ejercicio = caja_actividad.get()

    sedentario = opcion_nivel_ejercicio == "1"
    ligeramente_activo = opcion_nivel_ejercicio == "2"
    moderadamente_activo = opcion_nivel_ejercicio == "3"
    muy_activo = opcion_nivel_ejercicio == "4"

    consume_tabaco = tabaco == "si"
    consume_alcohol = alcohol == 'si'
    IMC = peso / (altura ** 2)
    peso_paciente = "Desconocido"

    es_bajo_peso = IMC < 18.5
    es_peso_normal = 18.5 <= IMC < 25.0
    es_sobrepeso = 25.0 <= IMC < 30.0
    es_obesidad = IMC >= 30.0

    if es_bajo_peso:
        peso_paciente = "Bajo peso"
    elif es_peso_normal:
        peso_paciente = "Peso normal"
    elif es_sobrepeso:
        peso_paciente = "Sobrepeso"
    elif es_obesidad:
        peso_paciente = "Obesidad"

    lista_niveles = list(niveles_de_actividad_fisica.keys())
    if opcion_nivel_ejercicio in ["1", "2", "3", "4"]:
        nivel_actividad_texto = lista_niveles[int(opcion_nivel_ejercicio) - 1]
    else:
        nivel_actividad_texto = "No especificado"

    fiebre = caja_fiebre.get().lower()
    tos = caja_tos.get().lower()
    dolor_cabeza = caja_cabeza.get().lower()
    dolor_pecho = caja_pecho.get().lower()
    fatiga = caja_fatiga.get().lower()
    dolor_estomago = caja_estomago.get().lower()
    mareo = caja_mareo.get().lower()
    molestia_orinar = caja_orinar.get().lower()
    dolor_articular = caja_articular.get().lower()

    if dolor_pecho == "s" and (mareo == "s" or fatiga == "s"):
        diagnostico = "Alerta del corazón o presión arterial. Necesitas ir a urgencias de inmediato."
    elif dolor_pecho == "s" and (fiebre == "s" or tos == "s"):
        diagnostico = "Problema respiratorio. Debes consultar a un médico lo antes posible."
    elif fiebre == "s" and tos == "s" and dolor_articular == "s":
        diagnostico = "Gripe fuerte con dolor de cuerpo."
    elif fiebre == "s" and tos == "s" and fatiga == "s":
        diagnostico = "Gripe o infección en los pulmones con mucho cansancio."
    elif fiebre == "s" and tos == "s":
        diagnostico = "Infección en la garganta"
    elif tos == "s" and dolor_cabeza == "s":
        diagnostico = "Irritación en las vías respiratorias o alergia"
    elif dolor_estomago == "s" and fiebre == "s":
        diagnostico = "Infección estomacal o digestiva."
    elif dolor_estomago == "s" and (consume_alcohol or consume_tabaco):
        diagnostico = "Gastritis o irritación del estómago causada por el alcohol o cigarro."
    elif dolor_estomago == "s":
        diagnostico = "Malestar de estómago común o indigestión."
    elif dolor_cabeza == "s" and mareo == "s":
        diagnostico = "Dolor de cabeza por presión descompensada, deshidratación o migraña."
    elif dolor_cabeza == "s" and fatiga == "s":
        diagnostico = "Dolor de cabeza por estrés, cansancio o falta de sueño."
    elif molestia_orinar == "s" and fiebre == "s":
        diagnostico = "Infección de orina avanzada con fiebre."
    elif molestia_orinar == "s":
        diagnostico = "Infección o irritación al orinar."
    elif fiebre == "s" and dolor_cabeza == "s":
        diagnostico = "Fiebre con dolor de cabeza. Reposa y toma suficientes líquidos."
    elif fatiga == "s" and sedentario and (es_sobrepeso or es_obesidad):
        diagnostico = "Cansancio frecuente por falta de ejercicio y sobrepeso."
    elif fiebre == "s" or tos == "s" or dolor_cabeza == "s" or fatiga == "s" or dolor_articular == "s":
        diagnostico = "Síntomas leves. Si no mejoras en unos días, acude al médico."
    else:
        diagnostico = "No se detectaron problemas ni síntomas claros de enfermedad."

    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, "=" * 60 + "\n")
    salida.insert(tk.END, "       INFORME MÉDICO PRELIMINAR Y DIAGNÓSTICO      \n")
    salida.insert(tk.END, "=" * 60 + "\n")
    salida.insert(tk.END, f"• Nombre del Paciente:   {nombre}\n")
    salida.insert(tk.END, f"• Sexo:                  {sexo.capitalize()}\n")
    salida.insert(tk.END, f"• Peso:                  {peso} kg | Altura: {altura} m\n")
    salida.insert(tk.END, f"• Ín. de Masa Corporal:  {IMC:.2f} ({peso_paciente})\n")
    salida.insert(tk.END, f"• Medicamento en uso:    {medicamento_consumido}\n")
    salida.insert(tk.END, f"• Consumo de Tabaco:     {'Sí' if consume_tabaco else 'No'}\n")
    salida.insert(tk.END, f"• Consumo de Alcohol:    {'Sí' if consume_alcohol else 'No'}\n")
    salida.insert(tk.END, f"• Nivel de Actividad:    {nivel_actividad_texto}\n")
    salida.insert(tk.END, "-" * 60 + "\n")
    salida.insert(tk.END, " SÍNTOMAS REPORTADOS:\n")
    salida.insert(tk.END, f"• Fiebre: {fiebre.upper()} | Tos: {tos.upper()} | Dolor Cabeza: {dolor_cabeza.upper()}\n")
    salida.insert(tk.END, f"• Dolor Pecho: {dolor_pecho.upper()} | Fatiga: {fatiga.upper()} | Mareo: {mareo.upper()}\n")
    salida.insert(tk.END, f"• Dolor Estómago: {dolor_estomago.upper()} | Molestia Orinar: {molestia_orinar.upper()}\n")
    salida.insert(tk.END, f"• Dolor Articular: {dolor_articular.upper()}\n")
    salida.insert(tk.END, "-" * 60 + "\n")
    salida.insert(tk.END, " RESULTADO DEL DIAGNÓSTICO:\n")
    salida.insert(tk.END, f" ► {diagnostico}\n")
    salida.insert(tk.END, "=" * 60 + "\n")
    salida.config(state="disabled")

btn_evaluar = tk.Button(ventana, text="Generar Diagnóstico", width=20, command=diagnosticar, bg="gray70", fg="black", activebackground="gray60")
btn_evaluar.pack(pady=5)

salida.pack(fill="both", expand=True, padx=10, pady=5)

ventana.mainloop()