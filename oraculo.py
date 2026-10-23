import random


PREVISOES = [
    "Hoje seu código vai compilar de primeira. Aproveite, é raro.",
    "Cuidado com o ponto e vírgula esquecido. Ele está te observando.",
    "Um commit com a mensagem 'arrumei' vai te assombrar.",
    "O bug não está no computador. Está entre a cadeira e o teclado.",
    "Hoje é um ótimo dia para escrever testes.",
    "Nunca faça deploy na sexta-feira às 17h.",
    "Seu café vai acabar exatamente quando o pipeline ficar verde.",
    "Um conflito de merge vai testar sua paciência antes dos testes unitários.",
    "Hoje você vai descobrir que o TODO de ontem virou a tarefa de amanhã.",
]


def consultar():
    return random.choice(PREVISOES)


if __name__ == "__main__":
    print("## Oráculo DevOps")
    print(consultar())
