import tkinter as tk #Importación

ventana = tk.Tk() #Crea la variable
ventana.title("Este es el titulo") #Crea el titulo
ventana.geometry("1000x300") #Crea tamaño de la ventana

etiqueta = tk.Label(ventana, text="Esto es una etiqueta") #Crea un texto dentro de la ventana
etiqueta.pack(pady=100) #Distancia del texto interno

ventana.mainloop() #Mantiene la ventana abierta
