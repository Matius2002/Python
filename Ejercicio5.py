"Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la "
"paga que le corresponde."
#variables para utlizar: horas trabajadas, costo por hora y pago correspodiente
HorasTrabajadas = float(input("Digite las horas trabajadas: "))
CostoHora = float(input("Digite el costo de su hora: "))
PagoFinal = (HorasTrabajadas * CostoHora)

print("Su pago es: ", PagoFinal)