"Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."
print("--------------------INICIO DEL PROGRAMA--------------------")
numero = int(input("Dígite un número a multiplicar: "))
for i in range(0,60):
    print(numero,"x",(i+1),"=",str((numero*(i+1))))
print("--------------------FIN DEL PROGRAMA--------------------")