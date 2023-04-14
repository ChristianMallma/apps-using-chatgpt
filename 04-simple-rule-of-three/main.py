import tkinter as tk


def calcular_regla_de_tres():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        num3 = float(num3_entry.get())
        resultado = num3 * num2 / num1
        resultado_label.config(text=f"El resultado es: {resultado:.2f}")
    except ValueError:
        resultado_label.config(text="Ingrese números válidos.")


root = tk.Tk()

# Establecer el color de fondo en blanco
root.configure(bg='white')

# Establecer el color de primer plano en negro para todos los widgets
root.option_add('*foreground', 'black')

# Crear los widgets de entrada y etiqueta
num1_label = tk.Label(root, text="Número 1:")
num2_label = tk.Label(root, text="Número 2:")
num3_label = tk.Label(root, text="Número 3:")
num1_entry = tk.Entry(root)
num2_entry = tk.Entry(root)
num3_entry = tk.Entry(root)
resultado_label = tk.Label(root)

# Posicionar los widgets en una cuadrícula
num1_label.grid(row=0, column=0, padx=5, pady=5)
num2_label.grid(row=1, column=0, padx=5, pady=5)
num3_label.grid(row=2, column=0, padx=5, pady=5)
num1_entry.grid(row=0, column=1, padx=5, pady=5)
num2_entry.grid(row=1, column=1, padx=5, pady=5)
num3_entry.grid(row=2, column=1, padx=5, pady=5)
resultado_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Crear el botón de cálculo y posicionarlo debajo de los campos de entrada
calcular_button = tk.Button(root, text="Calcular", command=calcular_regla_de_tres)
calcular_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle principal de Tkinter
root.mainloop()
