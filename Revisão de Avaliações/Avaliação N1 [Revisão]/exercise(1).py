# Nome: Pedro Henrique do Nascimento Urbano | Turma: 2190 | Exercício 01

campeonato_brasileiro_futebol = ("Botafogo","Fortaleza","Flamengo","Palmeiras","São Paulo","Cruzeiro","Bahia","Athletico-PR","Atlético-MG","Vasco","Bragantino","Juventude","Grêmio","Criciúma","Internacional","Vitória","Corinthians","Fluminense","Cuiabá","Atlético-GO")

print(f'Os 5 primeiros colocados: {campeonato_brasileiro_futebol[:5]}')
print(f'Os últimos 4 colocados: {campeonato_brasileiro_futebol[-4:]}')
print(f'Times em ordem alfabética: {sorted(campeonato_brasileiro_futebol)}')
print(f'Posição do time "Criciúma" na tabela:')

for "Criciúma" in campeonato_brasileiro_futebol:
    campeonato_brasileiro_futebol.index(("Criciúma")+1)