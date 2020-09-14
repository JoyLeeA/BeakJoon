def solve(N):
    result = 0
    for i in range(1, N+1):
        if i <=99:
            result +=1
        else:
            num = list(map(int, str(i)))
            if num[0] - num[1] == num[1] - num[2]:
                result +=1
    return result

N = int(input())
print(solve(N))

