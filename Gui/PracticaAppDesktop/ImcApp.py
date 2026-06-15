from tkinter import *

root = Tk()
root.title("Calculadora de IMC")

frame = Frame(root)
frame.pack(padx=20, pady=20)


def calcular_imc():
    try:
        v_peso = float(peso.get())
        v_altura = float(altura.get())

        imc_calculado = v_peso / (v_altura ** 2)
        imc_redondeado = round(imc_calculado, 2)

        imc_variable.set(imc_redondeado)

        # Determinar categoría
        if imc_calculado < 18.5:
            text_categoria = "Bajo peso"
        elif 18.5 <= imc_calculado < 24.9:
            text_categoria = "Peso normal"
        elif 25.0 <= imc_calculado < 29.9:
            text_categoria = "Sobrepeso"
        else:
            text_categoria = "Obesidad"

        categoria.set(text_categoria)

        print(f"\nSu IMC es: {imc_redondeado}")
        print(f"Clasificación: {text_categoria}")

    except ValueError:
        categoria.set("Error: Datos inválidos")


# Variables de Tkinter
altura = StringVar()
peso = StringVar()
categoria = StringVar()
imc_variable = StringVar()

# --- FILA 0: Altura ---
label1 = Label(frame, text='Altura (m):')
label1.grid(row=0, column=0, sticky='w', padx=5, pady=5)

alturaEntrada = Entry(frame, justify='center', textvariable=altura)
alturaEntrada.grid(row=0, column=1, padx=5, pady=5)

# --- FILA 1: Peso ---
label2 = Label(frame, text='Peso (kg):')
label2.grid(row=1, column=0, sticky='w', padx=5, pady=5)

pesoEntrada = Entry(frame, justify='center', textvariable=peso)
pesoEntrada.grid(row=1, column=1, padx=5, pady=5)

# --- FILA 2: Categoría (¡La nueva sección!) ---
label3 = Label(frame, text='Categoría:')
label3.grid(row=2, column=0, sticky='w', padx=5, pady=5)

# Este Label mostrará el resultado'
label_resultado_categoria = Label(
    frame, textvariable=categoria, font=("Arial", 10, "bold"), fg="blue")
label_resultado_categoria.grid(row=2, column=1, sticky='w', padx=5, pady=5)

# --- FILA 3: Botón Calcular ---
resultado = Button(frame, text='Calcular', bd=3,
                   font=("Courier", 10), command=calcular_imc)
resultado.grid(row=3, column=0, columnspan=2, pady=10)

# --- FILA 4: Entrada de Resultado Numérico ---
imcResultado = Entry(frame, bd=5, font=(
    "Courier", 14), state="readonly", textvariable=imc_variable, justify='center')
imcResultado.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
