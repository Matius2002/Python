"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo."""
print("----------------INICIO DEL PROGRAMA----------------")
numero = int(input("Dígite un número: "))
for i in range(1,numero+1,2):
    for j in range(i,0,-2):
        print(j, end=" ")
    print("")
print("----------------FIN DEL PROGRAMA----------------")