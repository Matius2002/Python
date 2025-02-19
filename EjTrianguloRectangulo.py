""""
ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NÚMERO ENTERO Y MUESTRE POR PANTALLA UN TRIÁNGULO RECTÁNGULO COMO EL DE MÁS ABAJO, DE ALTURA EL NÚMERO INTRODUCIDO
*
**
***
****
*****
******
"""

while True: #Entrada al bucle
    try: #Entra a la excepción
        numero = int(input("\n| Digité un número entero: ")) #Se digita el número entero
        if numero >= 0: #Si el número es positivo sale
            break #Sale del bucle
        print("\nEl número no puede ser negativo. Inténtelo de nuevo.") #Si es negativo muestra el mensaje
    except ValueError: #Si se digita cualquier otro número
        print("\nEntrada inválida. Debe ingresar un número entero.") #Se muestra el mensaje

print("") #Salto de línea
for i in range(numero): #Genera valores desde 0 hasta numero - 1 | i representa la fila actual del triangulo
    for j in range(i+1): #Genera valores 0 hasta i, lo que hace que en cada fila haya i+1 asteriscos | j representa la cantidad de asteristicos en cada fila.
        print("*", end="") #Imprime un asteristico * sin salto de línea (end="" evita el \n automático)
    print("") #Esto imprime un salto de línea después de completar cada fila.
print("") #Salto de línea final
