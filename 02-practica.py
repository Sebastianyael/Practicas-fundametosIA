import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Sistema de autorización para examen final")
ventana.geometry("760x620")
ventana.configure(bg="gray")

label_titulo = tk.Label(ventana, text="SISTEMA DE AUTORIZACIÓN PARA EXAMEN FINAL", font=("Arial", 13, "bold"), bg="gray", fg="black")
label_titulo.pack(pady=10)

marco = tk.Frame(ventana, bg="gray")
marco.pack(pady=5)

label_asistencia = tk.Label(marco, text="Porcentaje de asistencia:", bg="gray", fg="black")
label_asistencia.grid(row=0, column=0, sticky="e", padx=5, pady=3)
caja_asistencia = tk.Entry(marco, width=10, bg="gray80", fg="black", insertbackground="black")
caja_asistencia.grid(row=0, column=1, sticky="w")

label_promedio = tk.Label(marco, text="Promedio:", bg="gray", fg="black")
label_promedio.grid(row=1, column=0, sticky="e", padx=5, pady=3)
caja_promedio = tk.Entry(marco, width=10, bg="gray80", fg="black", insertbackground="black")
caja_promedio.grid(row=1, column=1, sticky="w")

v_proyecto = tk.IntVar()
v_autorizacion = tk.IntVar()
v_adeudos = tk.IntVar()
v_lista = tk.IntVar()

chk_proyecto = tk.Checkbutton(marco, text="Entregó el proyecto", variable=v_proyecto, bg="gray", fg="black", activebackground="gray", selectcolor="gray80")
chk_proyecto.grid(row=2, column=0, columnspan=2, sticky="w", padx=5)

chk_autorizacion = tk.Checkbutton(marco, text="Tiene autorización especial", variable=v_autorizacion, bg="gray", fg="black", activebackground="gray", selectcolor="gray80")
chk_autorizacion.grid(row=3, column=0, columnspan=2, sticky="w", padx=5)

chk_adeudos = tk.Checkbutton(marco, text="Tiene adeudos pendientes", variable=v_adeudos, bg="gray", fg="black", activebackground="gray", selectcolor="gray80")
chk_adeudos.grid(row=4, column=0, columnspan=2, sticky="w", padx=5)

chk_lista = tk.Checkbutton(marco, text="Aparece en la lista de autorizados", variable=v_lista, bg="gray", fg="black", activebackground="gray", selectcolor="gray80")
chk_lista.grid(row=5, column=0, columnspan=2, sticky="w", padx=5)

salida = tk.Text(ventana, font=("Courier New", 10), height=5, state="disabled", bg="gray80", fg="black")

def evaluar():
    try:
        asistencia = float(caja_asistencia.get())
        promedio = float(caja_promedio.get())
    except ValueError:
        messagebox.showwarning("Datos inválidos", "La asistencia y el promedio deben ser números.")
        return

    P = asistencia >= 80
    Q = promedio >= 7
    R = v_proyecto.get() == 1
    S = v_autorizacion.get() == 1
    T = v_adeudos.get() == 0
    U = v_lista.get() == 1

    negacion_P = not P
    conjuncion = P and Q
    disyuncion = Q or S
    condicional = (not P) or Q
    bicondicional = P == Q
    expresion = (P and Q) or S

    resultado_final = expresion and T and U

    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    
    if resultado_final:
        salida.insert("1.0", "Puede presentar examen: SI")
    else:
        salida.insert("1.0", "Puede presentar examen: NO")
        
    salida.config(state="disabled")

btn_evaluar = tk.Button(ventana, text="Evaluar", width=18, command=evaluar, bg="gray70", fg="black", activebackground="gray60")
btn_evaluar.pack(pady=12)

salida.pack(fill="both", expand=True, padx=15, pady=(0, 15))

ventana.mainloop()