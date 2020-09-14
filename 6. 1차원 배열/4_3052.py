result = set()
data=[int(input())%42 for _ in range(10)]
for i in data:
    result.add(i)
print(len(result))