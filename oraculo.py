import random


PREVISOES = [
    "Hoje seu código vai compilar de primeira. Aproveite, é raro.",
    "Cuidado com o ponto e vírgula esquecido. Ele está te observando.",
    "Um commit com a mensagem 'arrumei' vai te assombrar.",
]


def consultar():
    return random.choice(PREVISOES)


if __name__ == "__main__":
    print("## Oráculo DevOps")
    print(consultar())
