"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número
separados por comas."""
print("-----------------INICIO DE PROGRAMA-----------------")
while True:
    try:
        enteroPositivo = int(input("Dígite un número entero positivo: "))
        if enteroPositivo < 0:
            print("¡Números no permitidos!")
        else:
            break
    except ValueError:
        print("¡Dígito caracteres no permitidos!")
for i in range(1,enteroPositivo+1,2):
    print(i)
print("-----------------FIN DEL PROGRAMA-----------------")