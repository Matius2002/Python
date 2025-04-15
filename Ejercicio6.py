"Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros "
"desde 1 hasta n, La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2"
n = int(input("Introducir un entero: ")) #Pide el entero y lo almacena
suma = n * (n + 1) / 2 #realiza la suma y la almacena
print("La suma de los primeros números enteros desde 1 hasta: "+ str(n)+" es "+ str(suma)) #Muestra por pantalla el numero y la suma
