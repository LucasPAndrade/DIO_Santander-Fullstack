print('=' * 10)
print('DESAFIO 110 - Desafio 109 melhorado')
print('=' * 10, '\n')

from Desafio_110 import moeda
v = float(input('Digite um valor: R$ '))
aumento = float(input('Digite a porcentagem de aumento (0 a 100%): '))
redução = float(input('Digite a porcentagem de redução (0 a 100%): '))
formmoeda = True
fm = str(input('Formatar como moeda? [S/N] '))
if fm in 'nN':
    formmoeda = False

moeda.resumo(v,aumento,redução,formmoeda)