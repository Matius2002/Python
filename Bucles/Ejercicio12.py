"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
el número de veces que aparece la letra en la frase."""
frase = input("Dígite una frase: ")
letra = input("Dígite una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparace %2i veces en la frase '%s'."%(letra, contador,frase))