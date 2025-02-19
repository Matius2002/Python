""""
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

while True:
    try:
        entero = int(input("\n***Digíte un número entero positivo: "))
        if entero >= 0:
            break
        print("\n| !No puede ser negativo¡ |")
    except ValueError:
        print("\n| Entrada invalida |")

print("")
for i in range(1, entero+1, 2):
    print(i, end=", ")
print("\n")