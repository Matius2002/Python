"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 $ mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributr o no."""
edad =  int(input("Dígite su edad: ")) #Pregunto edad
ingresosMensuales = float(input("Dígite su ingresos mensuales: ")) #Pregunto sueldo mensual

if edad > 16 and ingresosMensuales >= 1000: #Si cumple que si es mayor de 17 años y tiene ingresos de 1000 usd o mas tiene que tributar.
    print("Tienes que tributar") #Muestra mensaje de tributación
else:
    print("No tienes que tributar") #Muestra mensaje de NO tributación