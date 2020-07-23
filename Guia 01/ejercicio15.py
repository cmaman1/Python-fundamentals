creditos = {
    'Matematicas': 6,
    'Física': 4,
    'Química': 5
}

total_creditos = 0

for i in creditos:
    print(i, 'tiene %i creditos' % creditos['%s' % i])
    total_creditos += creditos['%s' % i]

print(total_creditos)
