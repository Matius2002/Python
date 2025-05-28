"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el 
usuario escriba “salir” que terminará."""
print("----------------INICIO DEL PROGRAMA----------------")
while True:
    eco = input("Dígite lo que quiera, para salir escribe salir: ")
    if eco.lower() == 'salir':
        break
    else:
        print(eco)
print("----------------INICIO DEL PROGRAMA----------------")