"""
HAZ UN PROGRAMA QUE PIDA NOTAS DE CLASE Y NO PARE HASTA QUE INTRODUZCAS UNA NOTA NEGATIVA. LUEGO IMPRIME LA SUMA
"""

nota = 0 #Se declara el valor de la variable nota
suma = 0 #Se declara el valor de la variable de suma
i = 1 #Se crea el valor del iterador para saber en que numero de nota va.

print("\n***DIGITE LAS NOTAS (SE DETIENE CUANDO SE INTRODUZCA UN NEGATIVO)***\n")

#Se crea el bucle while porque no se sabe hasta cuando se tiene que parar
while nota >= 0:
    nota = float(input(f"| Nota {i}: ")) #Se pide la nota
    i += 1 #Se incrementa el iterador

    if nota >= 0: #Condición para que realice la suma de las notas
        suma += nota #Se suma la nota

print("\n***LA SUMA DE LAS NOTAS ES: "+str(suma)+"***\n") #Se imprime el total de la nota