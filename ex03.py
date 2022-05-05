#Primeira versão

#def area(base, altura):
    #a = base * altura / 2
    #print(f'A área de triângulo com {base}cm de base e {altura}cm de altura é: {a}cm²')

#base = int(input('Base do triângulo em cm:'))
#altura = int(input('Altura do triângulo em cm:'))
#area(base, altura)


#Fiz com ajuda de exemplos na internet

def dados():
    base = int(input('Base do triângulo em cm:'))
    altura = int(input('Altura do triângulo em cm:'))
    return base, altura

def calculo(base, altura):
    cal = base * altura / 2
    print(f'A área de triângulo com {base}cm de base e {altura}cm de altura é: {cal}cm²')

base, altura = dados()
calculo(base, altura)

