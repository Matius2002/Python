import calendar #Importamos el calendario

#Función para mostrar un calendario de un año y mes específicos
def mostrar_calendario(año, mes): #Creamos un método con 2 parámetros(año y mes)
    print("") #Salto de línea
    print(calendar.month(año, mes)) #Genera el calendario en texto en un mes de un año especifico y se imprime

#Solicita al usuario ingresar el año y mes
print("*******************************************")
año = int(input("\nIngresa el año: ")) #Se pide un año y se guarda
mes = int(input("\nIngresa el mes (1-12): ")) #Se pide el mes y se guarda
mostrar_calendario(año, mes) #Se le entrega las 2 variables para el método del calendario
print("*******************************************")