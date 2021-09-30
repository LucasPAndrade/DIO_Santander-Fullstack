print('=' * 10)
print('DESAFIO 112 - Desafio 111 melhorado')
print('=' * 10, '\n')

from Desafio_112.utilidadesCV import moeda
from Desafio_112.utilidadesCV.dado import leiadado

v = leiadado('Digite um valor: R$ ')
aumento = float(input('Digite a porcentagem de aumento (0 a 100%): '))
redução = float(input('Digite a porcentagem de redução (0 a 100%): '))
formmoeda = True
fm = str(input('Formatar como moeda? [S/N] '))
if fm in 'nN':
    formmoeda = False

moeda.resumo(v,aumento,redução,formmoeda)