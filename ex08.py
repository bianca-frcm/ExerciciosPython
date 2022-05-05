def soma(n1, n2):
    print(f'A soma desses dois números é: {n1 + n2}')


def sub(n1, n2):
    print(f'A subtração desses dois números é: {n1 - n2}')


def mult(n1, n2):
    print(f'A multiplicação desses dois números é: {n1 * n2}')


def div(n1, n2):
    print(f'A divisão desses dois números é: {n1 / n2}')


def res(n1, n2):
    print(f'O resto da divisão desses dois números é: {n1 % n2}')


def fun1():
    n1 = int(input('Primeiro número:'))
    n2 = int(input('Segundo número:'))
    op = int(input('Digite o número opções: 1 p/ soma, 2 p/ subtração, 3 p/ multiplicação, 4 p/ divisão ou 5 p/resto: '))
    if op == 1:
        soma(n1, n2)
    elif op == 2:
        sub(n1, n2)
    elif op == 3:
        mult(n1, n2)
    elif op == 4:
        div(n1, n2)
    elif op == 5:
        res(n1, n2)

    return n1, n2


n1, n2 = fun1()
