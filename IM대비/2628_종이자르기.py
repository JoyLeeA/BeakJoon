import sys
sys.stdin = open('2628.txt','r')
input = sys.stdin.readline

garo, sero = map(int, input().split())
N = int(input())
x_list = [0,garo]  # 가로 각각 길이
y_list = [0,sero]  # 세로 각각 길이
for _ in range(N):
    direction, length = map(int, input().split())
    if direction == 0:
        y_list.append(length)
    else:
        x_list.append(length)

x_list.sort()  # 좌, 위쪽부터 꺼내서 대조 하기 위함
y_list.sort()

max_square = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i - 1]
        height = y_list[j] - y_list[j - 1]
        if max_square < width * height:
            max_square = width * height

print(max_square)