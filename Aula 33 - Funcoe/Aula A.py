"""
Funções = def (Part 1)
"""


def funcao(msg):  # Criando sua função
    print(msg)  # Digite os code!


def saudacao(msg='Olá', nome='Usuario'):  # Usando parametros opcionais!
    print(msg, nome)


saudacao()
saudacao(nome="Henrique", msg='Tchau')
saudacao('Olá', 'Everton')
saudacao('Hello', 'Anna')
saudacao('Hi', 'Diego')

funcao('Olá mundo!')  # Usando parametros!
