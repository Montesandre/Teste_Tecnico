def desafio2(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if numero == b or numero == 0:
        print(f"O número {numero} pertence a sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence a sequência de Fibonacci.")

if __name__ == "__main__":
    numero = int(input("Digite um número: "))
    desafio2(numero)
