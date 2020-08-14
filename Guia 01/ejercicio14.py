"""Ejercicio 14:
Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje."""

datos = {}

nombre = input('Nombre: ')
edad = int(input('Edad: '))
direccion = input('Direccion: ')
telefono = input('Teléfono: ')

datos['nombre'] = nombre
datos['edad'] = edad
datos['direccion'] = direccion
datos['telefono'] = telefono

print(datos)
