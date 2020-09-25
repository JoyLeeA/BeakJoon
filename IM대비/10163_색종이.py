import sys
sys.stdin = open('10163.txt','r')
input = sys.stdin.readline

N = int(input())
board = [[0] * 101 for _ in range(101)]

for num in range(1, N+1):
    x, y, w, h = map(int,input().split())
    for i in range(y,y+h):
        for j in range(x,x+w):
            board[i][j] = num


result = []
for i in range(1, N+1):
    cnt = 0
    for j in range(101):
        cnt += board[j].count(i)
    result.append(cnt)

for i in result:
    print(i)