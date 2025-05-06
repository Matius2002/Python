"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres 
con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte 
al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""
#Validar nombre
while True:
    nombre = input("Dígite su nombre: ").strip()
    if nombre.isalpha():
        break
    else:
        print("Error: Primer nombre.")
        
#Validar sexo
while True:
    sexo = input("Dígite su sexo con M o F:").strip().upper()
    if sexo in ("M", "F"):
        break
    else:
        print("Error: Sexo erróneo. Ingrese M o F")

#Asignar grupo
if sexo == "F":
    if nombre.lower() < "f":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es "+grupo)