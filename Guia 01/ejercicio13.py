"""Ejercicio 13:
Crear un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

divisas = {
    'Euro': '€',
    'Dolar': '$',
    'Yen': '¥'
}

divisa = input('Ingrese una divisa: ')

if divisa == 'Euro' or divisa == 'Dolar' or divisa == 'Yen':
    print(divisas['%s' % divisa])
else:
    print('No se encontro la divisa en el diccionario')
