"""Ejercicio 10:
Escribir un programa que almacene todas las letras del abecedario y luego elimine las vocales y nos devuelva una lista sin las vocales, sin modificar la original."""

lista_abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

nueva_lista = []

for i in lista_abecedario:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        continue
    else:
        nueva_lista.append(i)

print(nueva_lista)
