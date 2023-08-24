def porcentagem(N1=0, Porc=0, aumentar=True):
    if aumentar:
        Soma = N1 + (N1 * Porc / 100)
        return Soma
    else:
        Subtrair = N1 - (N1 * Porc / 100)
        return Subtrair


print(porcentagem(100, 100, False))
