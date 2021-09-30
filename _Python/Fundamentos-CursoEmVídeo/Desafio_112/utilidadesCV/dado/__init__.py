def leiadado(msg):
    while True:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO! \'{entrada}\' é um valor inválido!\033[m')
        else:
            return float(entrada)
            break