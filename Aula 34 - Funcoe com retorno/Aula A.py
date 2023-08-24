"""
Funções (def) - return (parte 2)
"""


def funcao(var):
    print(var)


def funcao2(var):
    print('Isso será executado!')  # Code add depois de return, não sera exibido/executado
    return var   # Para que retorne um valor, ultiliza-se RETURN


print(funcao('Qualquer coisa!'))  # Irá me retorna um tipo de dado 'NONE' -> um 'Não valor'

variavel = funcao2('Vai retorna!')
if variavel:
    print(variavel)
else:
    print('Nenhum valor!')
