"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta                   Tipo Impositivo
Menos de $10000         5%
Entre $10000 y $20000   15%
Entre $20000 y 35000    20%
Entre 35000 y 60000     30%
Más de 60000            45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""
while True:
    try:
        rentaAnual = float(input("Dígite su renta anual: "))
        if rentaAnual < 0: #Si el número es negativo entra al mensaje
            print("La renta debe ser un número positivo. Intente de nuevo.") #Muestra el mensaje
        else:
            break #Sale del ciclo si la entrada es válida
    except ValueError: #Si introduce una entrada invalida
        print("Entrada invalida. Por favor, ingrese un número válido.")

if rentaAnual < 10000:
    print("Su impositivo es 5%")
elif rentaAnual >= 10000 and  rentaAnual < 20000:
    print("Su impositivo es 15%")
elif rentaAnual >= 20000 and  rentaAnual < 35000:
    print("Su impositivo es 20%")
elif rentaAnual >= 35000 and  rentaAnual <= 60000:
    print("Su impositivo es 30%")
else:
    print("Su impositivo es 45%")