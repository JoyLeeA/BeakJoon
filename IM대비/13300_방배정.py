import sys
sys.stdin = open('13300.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())
girl = [0] * 7
boy = [0] * 7



for _ in range(N):
    S, Y = map(int, input().split())
    if S:
        boy[Y] +=1
    else:
        girl[Y] +=1

cnt = 0
for i in range(1, 7):
    if boy[i]%K:
        cnt += boy[i]//K +1
    else:
        cnt += boy[i] // K

    if girl[i]%K:
        cnt += girl[i]//K +1
    else:
        cnt += girl[i] // K


print(cnt)