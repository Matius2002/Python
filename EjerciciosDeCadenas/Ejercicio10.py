"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada 
uno de los productos en una línea distinta."""
compra = input("Dígite los productos de la compra separadas por comas: ")
print(compra.replace(',', '\n'))