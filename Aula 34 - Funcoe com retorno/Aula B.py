def divisao(n1, n2):
    if n2 == 0:
        return
    else:
        return n1 / n2


divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta invalida!')


# Uma variavel pode ser tornar uma função.
def f(var):
    return (var)


def dumb():
    return f  # Estou mandando retorna a função!


var = dumb()
var('Pode imprimir algo na tela')  # Propria variavel vira uma função!
print(type(var))
print(id(var), id(f))  # Os dois id são iguais! MESMO objeto!


# Pode retorna uma tupla!
def DEF():
    return 'Everton', 'Coelho'


var = DEF()
print(var, type(var))  # Me retorna um tupla!
