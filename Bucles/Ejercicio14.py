"Realizar una calculadora con funciones el cual usuario elige que operación va ha realizar:"
import tkinter as tk
from tkinter import messagebox

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División entre cero no permitida"
    return a / b

def calcular(operacion):
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())

        if operacion == "Suma":
            resultado = suma(a, b)
        elif operacion == "Resta":
            resultado = resta(a, b)
        elif operacion == "Multiplicación":
            resultado = multiplicacion(a, b)
        elif operacion == "División":
            resultado = division(a, b)

        lbl_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "❌ Por favor, ingrese solo números válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("🧮 Calculadora Gráfica")
ventana.geometry("300x300")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="Calculadora Básica", font=("Arial", 16))
titulo.pack(pady=10)

# Entradas de números
entry_num1 = tk.Entry(ventana, justify='center', font=("Arial", 12))
entry_num1.pack(pady=5)
entry_num1.insert(0, "Primer número")

entry_num2 = tk.Entry(ventana, justify='center', font=("Arial", 12))
entry_num2.pack(pady=5)
entry_num2.insert(0, "Segundo número")

# Botones de operación
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Suma", width=10, command=lambda: calcular("Suma")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="Resta", width=10, command=lambda: calcular("Resta")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_botones, text="Multiplicación", width=10, command=lambda: calcular("Multiplicación")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botones, text="División", width=10, command=lambda: calcular("División")).grid(row=1, column=1, padx=5, pady=5)

# Resultado
lbl_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
lbl_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
