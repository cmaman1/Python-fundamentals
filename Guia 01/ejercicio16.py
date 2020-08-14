"""Ejercicio 16:
Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

datos = {}

nombre = input('Nombre: ')
datos['nombre'] = nombre
print(datos)

apellido = input('Apellido: ')
datos['apellido'] = apellido
print(datos)

edad = int(input('Edad: '))
datos['edad'] = edad
print(datos)

telefono = input('Telefono: ')
datos['telefono'] = telefono
print(datos)

email = input('Correo electronico: ')
datos['email'] = email
print(datos)
