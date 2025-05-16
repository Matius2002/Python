"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero 
separados por comas."""
while True:
    try:
        numero = int(input("Dígite un número entero positivo: "))
        if numero < 0:
            print("¡Números negativos, dígite número entero positivo!")
        else:
            break
    except ValueError:
        print("¡Caracteres invalidos, dígite un número entero positivo!")
for i in range(numero,-1,-1):
    print(i,end=", ")