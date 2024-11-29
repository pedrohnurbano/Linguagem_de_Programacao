# Nome: Pedro Henrique do Nascimento Urbano | Turma: 2190 | Exercício 01

receitas = []
despesas = []
contador = 0

while(contador<2):
    contador += 1
    receita = float(input("Digite a receita do mês: "))
    despesa = float(input("Digite a despesa do referido mês: "))
    receitas.append(receita)
    despesas.append(despesa)

lucro = list(map(lambda x,y: x-y,receitas,despesas))
media_lucro = sum(lucro)/2
mes_prejuizo = list(filter(lambda x: x<0,lucro))

print(f"O lucro para cada mês, respectivamente é de: {lucro}")
print(f"A média total do lucro anual é: {media_lucro}")
print(f"Meses onde ocorreram prejuízos durante o perído: {mes_prejuizo}")