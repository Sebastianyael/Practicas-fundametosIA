import random
import tkinter as tk

ventana = tk.Tk()
ventana.title("Chatbot de Diagnóstico")
ventana.geometry("500x650")
ventana.configure(bg="gray")

label_nombre = tk.Label(ventana, text="¿Cuál es tu nombre?", bg="gray", fg="black")
label_nombre.pack(pady=2)
caja_nombre = tk.Entry(ventana, width=40, bg="gray80", fg="black", insertbackground="black")
caja_nombre.pack(pady=2)

label_direccion = tk.Label(ventana, text="¿Cuál es tu dirección?", bg="gray", fg="black")
label_direccion.pack(pady=2)
caja_direccion = tk.Entry(ventana, width=40, bg="gray80", fg="black", insertbackground="black")
caja_direccion.pack(pady=2)

label_equipo = tk.Label(ventana, text="¿Qué equipo deseas diagnosticar?\n1) Escritorio  2) Laptop  3) Servidor  4) Tablet  5) Salir", bg="gray", fg="black")
label_equipo.pack(pady=5)
caja_equipo = tk.Entry(ventana, width=10, bg="gray80", fg="black", insertbackground="black")
caja_equipo.pack(pady=2)

label_p1 = tk.Label(ventana, text="¿Está conectado a la luz / tiene batería? (si/no):", bg="gray", fg="black")
label_p1.pack(pady=2)
caja_p1 = tk.Entry(ventana, width=10, bg="gray80", fg="black", insertbackground="black")
caja_p1.pack(pady=2)

label_p2 = tk.Label(ventana, text="¿Recibió algún golpe recientemente? (si/no):", bg="gray", fg="black")
label_p2.pack(pady=2)
caja_p2 = tk.Entry(ventana, width=10, bg="gray80", fg="black", insertbackground="black")
caja_p2.pack(pady=2)

label_p3 = tk.Label(ventana, text="¿Observas algún golpe, abolladura o pieza suelta? (si/no):", bg="gray", fg="black")
label_p3.pack(pady=2)
caja_p3 = tk.Entry(ventana, width=10, bg="gray80", fg="black", insertbackground="black")
caja_p3.pack(pady=2)

salida = tk.Text(ventana, font=("Courier New", 10), height=12, state="disabled", bg="gray80", fg="black")

def diagnosticar():
    nombre = caja_nombre.get().lower()
    direccion = caja_direccion.get().lower()
    
    try:
        equipo_a_diagnosticar = int(caja_equipo.get())
    except ValueError:
        return

    salida.config(state="normal")
    salida.delete("1.0", tk.END)

    def generarNumero():
        no_reporte = random.randint(1, 10)
        salida.insert(tk.END, "====================\n")
        salida.insert(tk.END, f"Okey {nombre} tu numero de reporte es {no_reporte}, comenzemos =)\n")
        salida.insert(tk.END, "====================\n")

    if equipo_a_diagnosticar == 1:
        generarNumero()
        conectado_luz = caja_p1.get().lower()
        
        P = conectado_luz == 'si'
        salida.insert(tk.END, f"P (Conectado a la luz): {P}\n")
        
        if conectado_luz == 'si':
            recibio_algun_golpe = caja_p2.get().lower()
            
            Q = recibio_algun_golpe == 'si'
            salida.insert(tk.END, f"Q (Recibió golpe): {Q}\n")
            
            if recibio_algun_golpe == "si":
                gabinete_dañado = caja_p3.get().lower()
                
                R = gabinete_dañado == 'si'
                salida.insert(tk.END, f"R (Gabinete dañado): {R}\n")
                
                evaluacion = P and Q and R
                salida.insert(tk.END, f"Proposición (P ∧ Q ∧ R): {evaluacion}\n")

    if equipo_a_diagnosticar == 2:
        generarNumero()
        tiene_bateria = caja_p1.get().lower()
        
        P = tiene_bateria == 'si'
        salida.insert(tk.END, f"P (Tiene batería): {P}\n")
        
        if tiene_bateria == 'si':
            recibio_algun_golpe = caja_p2.get().lower()
            
            Q = recibio_algun_golpe == 'si'
            salida.insert(tk.END, f"Q (Recibió golpe): {Q}\n")
            
            evaluacion = P and Q
            salida.insert(tk.END, f"Proposición (P ∧ Q): {evaluacion}\n")

    if equipo_a_diagnosticar == 3:
        generarNumero()
        conectado_luz = caja_p1.get().lower()
        
        P = conectado_luz == 'si'
        salida.insert(tk.END, f"P (Conectado a la luz): {P}\n")
        
        if conectado_luz == 'si':
            recibio_algun_golpe = caja_p2.get().lower()
            
            Q = recibio_algun_golpe == 'si'
            salida.insert(tk.END, f"Q (Recibió golpe): {Q}\n")
            
            evaluacion = P and Q
            salida.insert(tk.END, f"Proposición (P ∧ Q): {evaluacion}\n")

    if equipo_a_diagnosticar == 4:
        generarNumero()
        tiene_bateria = caja_p1.get().lower()
        
        P = tiene_bateria == 'si'
        salida.insert(tk.END, f"P (Tiene batería): {P}\n")
        
        if tiene_bateria == 'si':
            recibio_algun_golpe = caja_p2.get().lower()
            
            Q = recibio_algun_golpe == 'si'
            salida.insert(tk.END, f"Q (Recibió golpe): {Q}\n")
            
            evaluacion = P and Q
            salida.insert(tk.END, f"Proposición (P ∧ Q): {evaluacion}\n")

    if equipo_a_diagnosticar == 5:
        salida.insert(tk.END, f"======Hasta luego {nombre} espero haberte ayudado=====\n")

    salida.config(state="disabled")

btn_ejecutar = tk.Button(ventana, text="Diagnosticar", width=18, command=diagnosticar, bg="gray70", fg="black", activebackground="gray60")
btn_ejecutar.pack(pady=8)

salida.pack(fill="both", expand=True, padx=15, pady=(0, 15))

ventana.mainloop()