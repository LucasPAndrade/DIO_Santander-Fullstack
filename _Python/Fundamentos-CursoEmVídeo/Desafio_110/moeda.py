def aumentar(n, fator,fmoeda=True):
    if fator > 1:
        fator /= 100
    return moeda(n * (1+fator),fmoeda)


def diminuir(n, fator, fmoeda=True):
    if fator > 1:
        fator /= 100
    return moeda(n * (1-fator),fmoeda)


def dobro(n, fmoeda=True):
    return moeda(n * 2,fmoeda)


def metade(n, fmoeda=True):
    return moeda(n / 2,fmoeda)


def moeda(n,ativo=True):
    if ativo:
        return f'R$ {n:.2f}'
    else:
        return n

def resumo(n,a,r,fmoeda=True):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(n,fmoeda):<10}')
    print(f'{"Dobro do preço:":<20}{dobro(n,fmoeda):<10}')
    print(f'{"Metade do preço:":<20}{metade(n, fmoeda):<10}')
    txtaumento = f'{a:.1f}% de aumento:'
    txtredução = f'{r:.1f}% de redução:'
    print(f'{txtaumento:<20}{aumentar(n,a,fmoeda):<10}')
    print(f'{txtredução:<20}{aumentar(n, r, fmoeda):<10}')
    print('-' * 30)