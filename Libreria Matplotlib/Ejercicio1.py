"""Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla 
un diagrama de líneas con la evolución de las ventas."""
import matplotlib.pyplot as plt
inicio = int(input("Dígite el año inicial: "))
fin = int(input("Dígite el año final: "))
ventas = {}
for i in range(inicio,fin+1):
    ventas[i] = float(input("Dígite las ventas del año: "+str(i)+': '))
fig, ax = plt.subplots()
ax.plot(ventas.keys(),ventas.values())
plt.show()