import sys
sys.stdin = open('1244.txt', 'r')
input = sys.stdin.readline

def swap(n, T):
    if n:
        switch[T] = 0
    else:
        switch[T] = 1

N = int(input())
switch = [-1]+list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, num = map(int,input().split())

    # if sex==1:
    #     for i in range(num, N+1 ,3):
    #         if 0 < i <= N+1:
    #             swap(i)
    #
    if sex == 1:
        cnt = 1
        K = num
        while 0 < num <= N:
            swap(switch[num],num)
            cnt +=1
            num = K * cnt

    else:
        # swap(num)
        # comp = N-num
        # if comp >= num:
        #     for i in range(1, num+1):
        #         if switch[num-i] == switch[num+i]:
        #             swap(num-i)
        #             swap(num+i)
        #         else:
        #             break
        #
        # else:
        #     for i in range(1, comp+1):
        #             if switch[num - i] == switch[num + i]:
        #                 swap(num - i)
        #                 swap(num + i)
        #             else:
        #                 break
        swap(switch[num], num)
        cnt = 1
        while 0 < num-cnt and num+cnt <= N+1:
            if switch[num-cnt] == switch[num+cnt]:
                swap(switch[num-cnt], num-cnt)
                swap(switch[num+cnt], num+cnt)
                cnt+=1
            else:
                break

# for i in range(1, N, 20):
#     print(*switch[i:i+20])

cnt = 1
for i in switch[1:]:
    if cnt <= 20:
        print(i, end=' ')
    else:
        print()
        print(i, end=' ')
        cnt = 1
    cnt +=1