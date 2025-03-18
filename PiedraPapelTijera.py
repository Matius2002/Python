"""EJERCICIO DE LOGICA DE PROGRAMACIÓN
Piedra, papel o tijera
Crea un programa que permita al usuario jugar al juego de Piedra, Papel o Tijera contra la computadora.
La computadora elige una opción al azar y el programa determina el ganador."""

import random #Importamos la libreria Random

#Función para jugar piedra, papel o tijera
def piedra_papel_tijera(): #Creamos el método
    opciones = ['piedra', 'papel', 'tijera'] #Creamos una lista
    computadora = random.choice(opciones) #Se selecciona un elemento de la lista y se asigna a la variable
    print("****************************************")
    usuario = input("\nElije piedra, papel o tijera: ").lower() #Convierte toda la cadena a minusculas y lo asigna a la variable

    if usuario not in opciones: #Si lo que se dijito esta mal muestra lo de abajo
        print("\nOpción no valida\n") #Muestra mensaje de opción no valida
        return #Sale del método y se detiene el código
    
    print(f"\nComputadora eligió: {computadora}") #Muestra la función del metodo Random (computadora)

    if usuario == computadora: #Si usuario es igual a computadora
        print("\n!Es un empate¡\n") #Muestra mensaje
    elif(usuario == 'piedra' and computadora == 'tijera') or \
        (usuario == 'papel' and computadora == 'piedra') or \
        (usuario == 'tijera' and computadora == 'papel'): #Si cualquiera de estas 3 condiciones es verdadera el usuairo gana: (La piedra vence la tijera)
        print("\n!Ganaste¡\n")
    else:
        print("\n¡Perdiste!\n")
        
#Jugar Piedra, Papel o Tijera
piedra_papel_tijera()
print("****************************************")