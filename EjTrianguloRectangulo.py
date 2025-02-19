""""
ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NÚMERO ENTERO Y MUESTRE POR PANTALLA UN TRIÁNGULO RECTÁNGULO COMO EL DE MÁS ABAJO, DE ALTURA EL NÚMERO INTRODUCIDO
*
**
***
****
*****
******
"""

numero = int(input("Digite un número entero: "))

for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")
