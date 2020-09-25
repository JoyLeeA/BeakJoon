N = int(input())

board = [[0]*100 for _ in range(100)]

for _ in range(N):
    X, Y = map(int, input().split())
    for y in range(Y,Y+10):
        for x in range(X,X+10):
            board[y][x] = 1
result = 0
for i in board:
    result += sum(i)

print(result)