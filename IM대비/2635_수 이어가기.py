data = []

N = int(input())
max_len = 0
max_list = []

for i in range(N+1):
    result = [N, i]
    j = 0
    while True:
        temp = result[j] - result[j+1]
        if temp < 0:
            break
        result.append(temp)
        if max_len < len(result):
            max_len = len(result)
            max_list = result
        j += 1

print(max_len)
print(*max_list)