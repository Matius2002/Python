"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión"""
capital = float(input("Dígite la cantidad a invertir: "))
interes = float(input("Dígite el interes anual: "))
anos = int(input("Dígite el número de años: "))
capitalFinal = round((capital * (interes / 100 + 1) ** anos), 2) #Interés compuesto
print("Su capital obtenido de la inversión final es:"+str(capitalFinal))
