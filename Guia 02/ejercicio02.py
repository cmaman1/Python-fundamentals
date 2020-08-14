"""Ejercicio 2: 
Crear una lista con 10 números enteros cualquiera. Indicar cuál es el número mayor y cuál es el número menor. Si al menos hay 3 números mayores a 100, imprimir esos números, si no, imprimir los números menores a 50 que formen parte de la lista."""

lista = [28, 23, 57, 204, 77, 110, 103, 64, 23, 53]
numero_mayor = 0
cantidad_numeros_mayores_cien = 0
lista_numeros_mayores_cien = []


for i in lista:
    if i > numero_mayor:
        numero_mayor = i

    if i > 100:
        cantidad_numeros_mayores_cien = + 1
        lista_numeros_mayores_cien.append(i)

if cantidad_numeros_mayores_cien >= 3:
    print(lista_numeros_mayores_cien)
