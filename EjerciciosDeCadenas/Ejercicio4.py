"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +57, y la extensión 
tiene dos dígitos (por ejemplo +57 3152926344-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por 
pantalla el número de teléfono sin el prefijo y la extensión."""
print("------------------------------------------------") #Decoración
numero = input("Dígite su número con este formato +xx xxxxxxxxxx-xx: ")
print("El número de teléfono es: "+numero[4:-3]) #Muestra Muestra apartir del 4 caracter y termina antes del 3 ultimo caracter.
print("------------------------------------------------")#Decoración