from oraculo import PREVISOES, consultar


# Regra 1: o oráculo precisa de pelo menos 5 previsões
assert len(PREVISOES) >= 5, "Poucas previsões!"

# Regra 2: a previsão sorteada precisa existir na lista
assert consultar() in PREVISOES, "O oráculo inventou uma previsão!"

print("Todos os testes passaram!")
