"""Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última."""
print("-----------------INICIO DEL PROGRAMA-----------------")
palabra = input("Dígite una palabra:")
for i in range(len(palabra)-1,-1,-1):
    print(palabra[i])
print("-----------------FIN DEL PROGRAMA-----------------")