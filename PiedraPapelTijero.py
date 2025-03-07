"""EJERCICIO DE LOGICA DE PROGRAMACIÓN
Piedra, papel o tijera
Crea un programa que permita al usuario jugar al juego de Piedra, Papel o Tijera contra la computadora.
La computadora elige una opción al azar y el programa determina el ganador."""

import random

#Función para jugar piedra, papel o tijera
def piedra_papel_tijera():
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    print("****************************************")
    usuario = input("\nElije piedra, papel o tijera: ").lower()

    if usuario not in opciones:
        print("\nOpción no valida\n")
        return
    
    print(f"\nComputadora eligió: {computadora}")

    if usuario == computadora:
        print("\n!Es un empate¡\n")
    elif (usuario == 'piedra' and computadora == 'tijera') or (usuario == 'papel' and computadora == 'piedra') or (usuario == 'tijera' and computadora == 'papel'):
        print("\n!Ganaste¡\n")
    else:
        print("\n¡Perdiste!\n")
        
#Jugar Piedra, Papel o Tijera
piedra_papel_tijera()
print("****************************************")