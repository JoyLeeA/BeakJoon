import sys
sys.stdin = open('14696.txt','r')
input = sys.stdin.readline
# 4별 > 3동그라미 > 2네모 > 1세모


N = int(input())
for _ in range(N):
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]
    A.sort(reverse=True)
    B.sort(reverse=True)

    if len(A) > len(B):
        B += [0] * (len(A)-len(B))
    else:
        A += [0] * (len(B) - len(A))

    cnt = 0
    for i in range(len(A)):
        if A[i] > B[i]:
            print('A')
            break
        elif A[i] < B[i]:
            print('B')
            break
        else:
            cnt +=1
            if cnt == len(A):
                print('D')