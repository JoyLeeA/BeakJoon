N = int(input())
arr = list(map(int,input().split()))

cnt = 1
#result = []
max_l = 1
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        #result.append(cnt)
        cnt = 1
    if max_l < cnt:
        max_l = cnt        

cnt = 1
for i in range(1,N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        #result.append(cnt)
        cnt = 1
    if max_l < cnt:
        max_l = cnt
#print(max(result))
print(max_l)            