import sys
sys.stdin = open('sample.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    temp = []
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    for _ in range(N):
        student = list(map(int, input().split()))
        for i in range(M):
            if answer[i] == student[i]:
                student[i] = 1
            else:
                student[i] = 0
        temp.append(student)

    result = []
    #print(temp)
    for j in range(N):
        cnt = 1
        score = 0
        for i in range(M):
            if temp[j][i]:
                score += cnt
                cnt +=1
            else:
                cnt = 1
        result.append(score)

    print(f'#{test_case} {max(result)-min(result)}')
