"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el 
nombre del usuario tantas veces como el número introducido."""
print("--------------------------------------------")
nombre = input("Dígite su nombre: ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))
print("--------------------------------------------")