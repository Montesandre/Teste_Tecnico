def desafio5(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    print(f"String invertida: {invertida}")

if __name__ == "__main__":
    texto = input("Digite uma string: ")
    desafio5(texto)
