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
