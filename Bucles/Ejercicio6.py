"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido."""
numero = int(input("Dígite un número: "))
#Primera forma
for i in range(numero): #Filas
    for j in range(i+1): #Columnas
        print("*", end="") #Imprimir
    print("")
#Segunda forma
for i in range(numero):
   print("*"*(i+1))