## Desafio 1: Soma Acumulativa

def desafio1():
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    print(f"O valor da variável SOMA é: {soma}")

if __name__ == "__main__":
    desafio1()
