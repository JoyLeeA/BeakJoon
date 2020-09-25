T = int(input())
for _ in range(T):
    N, data = input().split()
    N= int(N)
    for i in data:
        print(i*N, end='')
    print()