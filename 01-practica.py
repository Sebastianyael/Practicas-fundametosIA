import tkinter as tk

root = tk.Tk()
root.title("Tabla de Verdad")
root.configure(bg="gray")

text_resultado = tk.Text(root, width=60, height=10, bg="gray80")
text_resultado.pack(padx=10, pady=10)

def ejecutar_logica():
    text_resultado.delete("1.0", tk.END)
    
    output = []
    output.append("P\tQ\tNO P\tP Y Q\tP O Q\tP->Q\tP<->Q")
    output.append("-" * 50)
    
    P = True
    Q = True

    negacion = not P
    conjuncion = P and Q

    disyuncion = P or Q

    if P == True and Q == False:
        condicional = False
    else:
        condicional = True

    if P == Q:
        bicondicional = True
    else:
        bicondicional = False

    output.append(f"{P}\t{Q}\t{negacion}\t{conjuncion}\t{disyuncion}\t{condicional}\t{bicondicional}")

    P = True
    Q = False

    negacion = not P
    conjuncion = P and Q
    disyuncion = P or Q

    if P == True and Q == False:
        condicional = False
    else:
        condicional = True

    if P == Q:
        bicondicional = True
    else:
        bicondicional = False

    output.append(f"{P}\t{Q}\t{negacion}\t{conjuncion}\t{disyuncion}\t{condicional}\t{bicondicional}")

    P = False
    Q = True

    negacion = not P
    conjuncion = P and Q
    disyuncion = P or Q

    if P == True and Q == False:
        condicional = False
    else:
        condicional = True

    if P == Q:
        bicondicional = True
    else:
        bicondicional = False

    output.append(f"{P}\t{Q}\t{negacion}\t{conjuncion}\t{disyuncion}\t{condicional}\t{bicondicional}")

    P = False
    Q = False

    negacion = not P
    conjuncion = P and Q
    disyuncion = P or Q

    if P == True and Q == False:
        condicional = False
    else:
        condicional = True

    if P == Q:
        bicondicional = True
    else:
        bicondicional = False

    output.append(f"{P}\t{Q}\t{negacion}\t{conjuncion}\t{disyuncion}\t{condicional}\t{bicondicional}")
    
    text_resultado.insert(tk.END, "\n".join(output))

btn_ejecutar = tk.Button(root, text="Mostrar Tabla", bg="gray70", command=ejecutar_logica)
btn_ejecutar.pack(padx=10, pady=5)

root.mainloop()