N = int(input())
score = list(map(int, input().split()))
M = max(score)
for i in range(N):
    score[i] = score[i]/M*100
print(f'{sum(score)/N:.2f}')
