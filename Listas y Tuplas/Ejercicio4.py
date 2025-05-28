"""Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene 
en una lista y los muestre por pantalla ordenados de menor a mayor."""
print("***Inicio del programa***")
loteria = [] #→Arreglo
for i in range(6): #Arreglo de 0 a 5 (6 datos)
    loteria.append(int(input("Introduce un número ganador: "))) #Pregunta un número y lo guarda como entero en el arreglo loteria
loteria.sort() #Ordena el arreglo de menor a mayor
print("Los números ganadores son: "+str(loteria)) #Muestra los número ordenados a penas halla recorrido los 6 datos
print("***Fin del programa***") 