data = []
for _ in range(9):
    data.append(int(input()))
result = max(data)
print(result)
print(data.index(result)+1)
