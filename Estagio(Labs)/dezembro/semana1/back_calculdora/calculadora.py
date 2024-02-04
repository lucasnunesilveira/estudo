
C = int(input())

for i in range(C):
    line = input().split()
    inteiros = [int(x) for x in line if x != '']

    media = sum(inteiros[1:])/inteiros[0]

    acima = [i for i in inteiros[1:] if i > media]
    print(f"{100*len(acima)/inteiros[0]:.3f}%")