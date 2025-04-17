"""Escribir un programa que pregunte el nombre completo del usuario en la consola y despues muestre por pantalla el nombre completo del usuario 
tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los 
apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""
nombre = input("Dígite su nombre completo: ")
print(nombre.lower()) #Método para las minusculas
print(nombre.upper()) #Método para las mayusculas
print(nombre.title()) #Método para CalmaCase