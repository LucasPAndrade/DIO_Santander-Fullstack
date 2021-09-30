def aumentar(n, fator):
    if fator > 1:
        fator /= 100
    return moeda(n * (1+fator))


def diminuir(n, fator):
    if fator > 1:
        fator /= 100
    return moeda(n * (1-fator))


def dobro(n):
    return moeda(n * 2)


def metade(n):
    return moeda(n / 2)


def moeda(n):
    return f'R$ {n:.2f}'