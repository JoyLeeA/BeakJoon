result_list = [0] * 10
data = [int(input()) for _ in range(3)]
result = 1
for i in data:
    result *= i
for j in str(result):
    result_list[int(j)] +=1
for k in result_list:
    print(k)   
    