def aumentar(n, fator):
    if fator > 1:
        fator /= 100
    return n * (1+fator)

def diminuir(n, fator):
    if fator > 1:
        fator /= 100
    return n * (1-fator)

def dobro(n):
    return n * 2

def metade(n):
    return n / 2