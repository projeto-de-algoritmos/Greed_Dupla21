N = int(input())
print(N)

print(N // 100, "nota(s) de R$ 100,00")
N = N - (N//100)*100

print(N // 50, "nota(s) de R$ 50,00")
N = N - (N//50)*50

print(N // 20, "nota(s) de R$ 20,00")
N = N - (N//20)*20

print(N // 10, "nota(s) de R$ 10,00")
N = N - (N//10)*10

print(N // 5, "nota(s) de R$ 5,00")
N = N - (N//5)*5

print(N // 2, "nota(s) de R$ 2,00")
N = N - (N//2)*2

print(N // 1, "nota(s) de R$ 1,00")
N = N - (N//1)*1