"""Ejercicio 4:
Ingresar 6 números por teclado, preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla."""

numeros = []
i = 0

while i < 6:
    numero = int(input("Ingrese un numero por favor: "))
    numeros.append(numero)
    i += 1

print(numeros)
