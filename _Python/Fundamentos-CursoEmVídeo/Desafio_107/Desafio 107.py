print('=' * 10)
print('DESAFIO 107 - Testando módulos')
print('=' * 10, '\n')

from Desafio_107 import moeda
v = float(input('Digite um valor: R$ '))
f = float(input('Digite a porcentagem de aumento e redução (0 a 100%): '))

print(f'R$ {v:.2f} aumentado em {f}% é igual a R$ {moeda.aumentar(v,f):.2f}.')
print(f'R$ {v:.2f} diminuído em {f}% é igual a R$ {moeda.diminuir(v,f):.2f}.')
print(f'O dobro de R$ {v:.2f} é igual a R$ {moeda.dobro(v):.2f}.')
print(f'A metade de R$ {v:.2f} é igual a R$ {moeda.metade(v):.2f}.')