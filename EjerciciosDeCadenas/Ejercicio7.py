"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electónico con el mismo 
nombre (la parte delante de la arroba @ pero con dominio ceu.es)"""
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')]+'@ceu.es')