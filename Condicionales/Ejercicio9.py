"""Escribir un programa para una empresa que tiene salas de juegos para todos las edades y quiere calcular de forma automatica el precio que 
debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y motrar el precio de la entrada. Si el 
cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar  $5 y si es mayor de 18 años, $10."""
print("*************************************************")
while True:
    try:
        edad = int(input("Dígite su edad: "))
        if edad <= 0 or edad > 115:
            print("¡Edad no valida!")
        else:
            break
    except ValueError:
        print("Entrada invalida, ingrese un número valido")

if edad < 4:
    print("Bienvenido, su entrada es gratis.")
elif edad >= 4 and edad < 18:
    print("Bienvenido, su entrada cuesta $5")
else:
    print("Bienvenido, su entrada cuesta $10")
print("*************************************************")