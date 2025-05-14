"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""
print("---------------------INICIO DEL PROGRAMA---------------------")
while True:
    try:
        edad = int(input("Dígite su edad en forma entera y sin letras: "))
        if edad <= 0 or edad >= 115:
            print("Edad Incorrecta")
        else:
            break 
    except ValueError:
        print("Entrada invalida, digíte una edad correcta")
print("")
for i in range(1,edad+1):
    print(i)
print("")
print("---------------------FIN DEL PROGRAMA---------------------")