## Desafio 3: Análise de Faturamento de Rotina

import json

def desafio3():
    with open("faturamento.json") as file:
        dados = json.load(file)

    faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]
    media = sum(faturamentos) / len(faturamentos)

    menor = min(faturamentos)
    maior = max(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    print(f"Menor faturamento: {menor}")
    print(f"Maior faturamento: {maior}")
    print(f"Dias com faturamento acima da media: {dias_acima_media}")

if __name__ == "__main__":
    desafio3()
