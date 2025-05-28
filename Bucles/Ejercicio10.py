"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
número primo o no."""
print("--------------------INICIO DEL PROGRAMA--------------------")
while True:
    try:
        primo = int(input("Dígite un número primo: "))
        if primo <= 0:
            print("!Dígite número entero¡")
        else:
            break
    except ValueError:
        print("¡Entrada erronea!")
#Primera forma
for i in range(2,primo):
    if primo % i == 0:
        break
    if (i+1) == primo:
        print(str(primo)," Es primo")
    else:
        print(str(primo), " No es primo")
#Segunda forma    
i = 2
while primo % i != 0:
    i += 1
if i == primo:
    print(str(primo) + " es primo")
else:
    print(str(primo) + " no es primo")
print("--------------------FIN DEL PROGRAMA--------------------")    