"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
por la contraseña hasta que introduzca la contraseña correcta."""
print("----------------INICIO DEL PROGRAMA----------------")
contrasena = "HelloWorld123@"
while True:
    password = input("Dígite la contraseña: ")
    if password != contrasena:
        print("Contraseña erronea, intente de nuevo.")
    else:
        break
print("¡Contraseña correcta!")
print("----------------FIN DEL PROGRAMA----------------")