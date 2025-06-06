"""En una determinada empresa, sus empleados son evaluados al final del cada año. Los puntos que pueden obtener en la evaluación comienzan en
0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de $2.400 multiplicada por la puntuación del nivel
Nivel           Puntuación
Inaceptable     0.0
Aceptable       0.4
Meritorio       0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibira el usuario.
"""
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
print("*****************************************")
while True:
    try:
        puntos = float(input("Dígite su puntuación: "))
        if puntos < 0:
            print("Error, el número no puede ser negativo")
        else:
            break
    except ValueError:
        print("Entrada invalida, por favor, ingrese un número valido")
        
#Clasificación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
#Mostrar nivel de rendimiento
    if nivel:
        print("Tu nivel de rendimiento es %s" % nivel)
        print("Te corresponde cobrar %.2f$" % (puntos * bonificacion))
print("*****************************************")