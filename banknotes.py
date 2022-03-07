valor_total = int(input())
print(valor_total)
notas = []
i = 0

numbers = [100, 20, 50, 10, 5, 2, 1]
numbers.sort(reverse = True)
for j in range(len(numbers)):
    qtd_notas = valor_total//numbers[j]
    valor_total -= qtd_notas*numbers[j]
    notas.append(qtd_notas)
print(f"{notas[0]} nota(s) de R$ 100,00\n{notas[1]} nota(s) de R$ 50,00\n{notas[2]} nota(s) de R$ 20,00\n{notas[3]} nota(s) de R$ 10,00\n{notas[4]} nota(s) de R$ 5,00\n{notas[5]} nota(s) de R$ 2,00\n{notas[6]} nota(s) de R$ 1,00")