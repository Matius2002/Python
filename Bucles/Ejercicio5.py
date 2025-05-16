"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión."""
print("-------------INICIO DEL PROGRAMA-------------")
# Ciclo para asegurar que todas las entradas sean válidas
while True:
    try:
        inversion = float(input("Dígite la cantidad a invertir: "))
        if inversion <= 0:
            print("¡Dígite una cantidad válida!")
            continue
        interesAnual = float(input("Dígite el interés anual (en porcentaje, ej. 5 para 5%): "))
        if interesAnual <= 0:
            print("¡Dígite una cantidad válida!")
            continue
        años = int(input("Dígite el número de años: "))
        if años <= 0:
            print("¡Dígite una cantidad válida!")
            continue
        break
    except ValueError:
        print("¡Entrada inválida! Asegúrese de usar números correctamente.")
# Convertimos el porcentaje a decimal
interesDecimal = interesAnual / 100
# Mostrar el capital acumulado cada año con interés compuesto
print("\nCapital acumulado cada año:")
for i in range(1, años + 1):
    capital_total = inversion * (1 + interesDecimal) ** i
    print(f"Año {i}: ${round(capital_total, 2)}")
print("-------------FIN DEL PROGRAMA-------------")

