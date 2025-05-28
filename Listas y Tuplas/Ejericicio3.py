"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""
print("***Inicio del programa***")
notas = [] #➡ Crea una lista vacía llamada notas para guardar las notas que ingreses.
asignaturas = ["Matemáticas","Física","Química","Historia","Lenguaje"] #➡ Crea una lista con los nombres de las asignaturas.
for asignatura in asignaturas: #➡ Comienza un bucle que recorre cada asignatura de la lista.
    nota = input("Dígite la nota de "+asignatura+":") #➡ Pide al usuario que escriba una nota para la asignatura actual.
    notas.append(nota) #➡ Agrega la nota ingresada a la lista notas.
print("") #➡ Imprime una línea en blanco para separar visualmente las secciones.
for i in range(len(asignaturas)): #➡ Recorre los índices de las listas usando range() y len().
    print("En "+asignaturas[i]+" has sacado "+notas[i]) #➡ Muestra qué nota sacaste en cada asignatura, usando el índice i.
print("***Fin del programa***")