"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a 
continuación:
° Ingredientes vegetarianos: Pimiento y tofu.
° Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los 
ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""
print("-------------INICIO DEL PROGRAMA-------------") #Mensaje de inicio del programa
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n") #Mensaje de opción a elegir por el usuario
while True: #Entra al bluce
    try: #Establece una condición
        tipo = int(input("Dígite el número correspondiente al tipo de pizza que quieres: ")) #Pregunta al usuario en formato entero si es 1 o 2
        if tipo <= 0 or tipo > 2: #Condición para que si usuario digita un núermo fuera del rango
            print("¡Número equivocado! (1 o 2)") #Muestra el mensaje porque el número esta fuera del rango
        else: #caso contrario de que si estuviera en el rango, entra
            break #sale del bucle para pasar a las otras condiciones.
    except ValueError: #Si el usuarios ingresa otro culquier caracter que no este permitido
        print("Digito una entrada invalida, La opción es 1 o 2") #Muestra el mensaje
    #Decisión sobre el tipo de pizza
if tipo == 1: #Si digito 1 es pizza vegetariana
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n") #Muestra los ingredientes de las pizzas vegetarianas
    ingrediente = input("Introduce el ingrediente que deseas: ") #Se digita el ingrediente y se almacena en la variable como cadena
    print("Pizza vegetariana con mozzarella, tomate y ", end="") #Se muestra la primera parte del mensaje sin hacer salto de línea al final.
    if ingrediente == "1": #Condición para saber si es 1 entra
        print("pimiento") #Muestra mensaje
    else: #Caso contrario entra
        print("tofu") #Muestra mensaje
else: #Si no digito 1 se sabe que es 2 (pizza no vegetariana)
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n") #Muestra el mensaje de la opción de ingredientes del tipo de pizza
    ingrediente = input("Introduce el ingrediente que deseas: ") #Ingrediente a introducir y se guarda en la variable como str (cadena)
    print("Pizza no vegetariana con mozarrella, tomate y ", end="") #Muestra la primera parte del mensaje sin hacer salto de línea
    if ingrediente == "1": #si es 1 entra
        print("peperoni") #muestra mensaje
    elif ingrediente == "2": #Si es 2, entra
        print("jamón") #Muestra mensaje
    else: #Caso contrario, entra
        print("salmón") #Muestar mensaje
print("-------------FIN DEL PROGRAMA-------------") #Mensaje dando a concer que se termino la ejecución del programa.