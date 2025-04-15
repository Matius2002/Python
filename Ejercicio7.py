"Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacena en una "
"variable, y muestre por pantalla a frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado "
"con dos decimales."
peso = input("Dígite su peso (kg): ")
estatura = input("Dígite su estatura (m): ")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es "+ str(imc))