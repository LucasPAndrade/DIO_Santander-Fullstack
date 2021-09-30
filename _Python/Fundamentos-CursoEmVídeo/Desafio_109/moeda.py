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