print('=' * 10)
print('DESAFIO 108 - Desaf107 melhorado')
print('=' * 10, '\n')

from Desafio_108 import moeda
v = float(input('Digite um valor: R$ '))
f = float(input('Digite a porcentagem de aumento e redução (0 a 100%): '))

v2 = moeda.moeda(v)

print(f'{v2} aumentado em {f}% é igual a {moeda.aumentar(v,f)}.')
print(f'{v2} diminuído em {f}% é igual a {moeda.diminuir(v,f)}.')
print(f'O dobro de {v2} é igual a {moeda.dobro(v)}.')
print(f'A metade de {v2} é igual a {moeda.metade(v)}.')