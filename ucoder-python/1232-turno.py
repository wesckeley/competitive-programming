data = {'M': 'Bom Dia!', 'V': 'Boa Tarde!', 'N': 'Boa Noite!'}

try:
    print(data[input()])
except KeyError:
    print('Valor Invalido!')
