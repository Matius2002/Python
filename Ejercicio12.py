"""Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience 
leyendo el número de barras vendidas que no sol del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento 
que se le hace por no ser fresca y el coste final total."""
print("------EJERCICIO DE LA PANADERÍA------")
PanVendidoDescuento = int(input("Dígite el pan vendido que no son del día: ")) #Pide la cantida de panes no frescos vendidos
panNormal = 12500 #Establece el valor del pan normal 
panDescuento = 0.60 #Se establece el porcentaje de descuento a los panes no frescos
coste = PanVendidoDescuento * panNormal * (1 - panDescuento) #Se establece el costo total de los panes vendidos con el descuento generado
print("El coste de una barra fresca es: "+str(panNormal)+" COP") #Se imprime el costo del pan normal
print("El descuento sobre una barra no fresca es: "+str(panDescuento * 100)+" %") #Se establece el porcentaje del descuento de la barra de pan que no es el del día
print("El coste final a pagar es: "+str(round(coste, 2))+ " COP")#El costo final vendido a los panes que no estan frescos
print("-------------------------------------")