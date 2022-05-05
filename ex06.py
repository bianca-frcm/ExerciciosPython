def nomes():
    n1 = input('Digite um nome:')
    n2 = input('Digite outro um nome:')
    n3 = input('Ok, agora digite outro nome:')
    return n1, n2, n3


def nomes__inverso(n1, n2, n3):
    print('Aqui estão os nomes que você digitou invertidos:')
    print(f'{n1[::-1]} ')
    print(f'{n2[::-1]} ')
    print(f'{n3[::-1]} ')


n1, n2, n3 = nomes()
nomes__inverso(n1, n2, n3)
