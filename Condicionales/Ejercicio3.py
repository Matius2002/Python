"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa 
debe mostrar un error."""
numero1 = float(input("Dígite el dividendo: "))
numero2 = float(input("Dígite el divisor: "))

if numero2 == 0:
    print("¡Error! No se puede dividir por 0")
else:
    print("La división es: ",round(numero1/numero2,3))