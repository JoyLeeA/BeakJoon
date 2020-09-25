sm = []
for _ in range(9):
    sm.append(int(input()))

fake = sum(sm) - 100
result = []
for i in range(9):
    for j in range(i+1,9):
        if sm[i] + sm[j] == fake:
            result.append(sm[i])
            result.append(sm[j]) 

for i in range(2):
    sm.remove(result[i])

sm.sort()
for i in sm:
    print(i)

