"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar"""
try:
    numero = int(input("Dígite un número: "))
    if numero % 4 == 0:
        print("¡El número es par!")
    else:
        print("¡El número es impar!")
except ValueError:
    print
    
"Nota: Para que un número sea par se dice que si al dividirlo entre 2 el residuo es 0 podemos decir que es par"