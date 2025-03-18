#Función para generar y mostrar la tabla de multiplicar de un número dado
def tabla_multiplicar(n): #Se crea el método con un parametro
    print("")
    for i in range(1, 21): #Bucle de 1 a 10
        print(n, "x", i, "=", n * i) #Me imprime cada valor del número
    

#Solicita al usuario ingresar un número
print("****************INICIO*****************")
numero  = int(input("\nIngresa un número: ")) #Pide el número entero
tabla_multiplicar(numero) #Llama a al método y se le pasa un argumento (Número digitado)
print("\n****************FIN*****************")