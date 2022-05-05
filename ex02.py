def obter_nome():
    n = input('Digite seu nome:')
    sn = input('Digite seu sobrenome: ')
    return n, sn


def mostre_nome(n, sn):
    print(f'Bom dia, {n} {sn}')


n, sn = obter_nome()
mostre_nome(n, sn)



