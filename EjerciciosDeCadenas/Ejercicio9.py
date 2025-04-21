"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzca con un solo carácter"""
fecha = input("Dígite la fecha dd/mm/aaaa: ")
print("Día: ",fecha[:2])
print("Mes: ",fecha[3:5])
print("Año: ",fecha[6:])

fecha2 = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha2[:fecha2.find('/')]
mesaño = fecha2[fecha2.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)