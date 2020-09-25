idx = list(map(chr,range(97,123)))
data = input()
for i in idx: 
    print(data.find(i), end=' ')
