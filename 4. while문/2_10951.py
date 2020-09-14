N = input()
if len(N) == 1:
    N = '0' + N

A = N[0]
B = N[1]
cnt = 0
while True:
    cnt += 1
    temp = str(int(A) + int(B))
    if len(temp) == 1:
        temp = '0' + temp
    if B + temp[1]==N:
        break
    A = B
    B = temp[1]
print(cnt)
