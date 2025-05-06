"""Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el 
nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
con 8 dígitos enteros y 2 decimales."""
producto = input("Dígite su producto: ")
precio = float(input("Dígite el precio del producto: "))
unidades = int(input("Dígite el número de unidades del producto: "))
print('{producto}: {precio:9.2f}$ x {unidades:3d} unidades = {total:11.2f}$'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))