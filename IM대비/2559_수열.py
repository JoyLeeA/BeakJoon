import sys
sys.stdin = open('2559.txt', 'r')
input = sys.stdin.readline

N, K = map(int,input().split())
data = list(map(int,input().split()))

temp_sum = sum(data[0:K])
result = temp_sum
for i in range(K, N):
    temp_sum += data[i]
    temp_sum -= data[i-K]
    if temp_sum > result:
        result = temp_sum
print(result)

# temp = 0
# max_num = 0
# for i in range(N-K+1):
#     for j in range(K):
#         temp += data[i+j]
#     if temp > max_num:
#         max_num = temp
#     temp=0
#
# print(max_num)
