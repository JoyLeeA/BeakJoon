import sys
sys.stdin = open('2527.txt', 'r')
input = sys.stdin.readline

for _ in range(4):
    data = list(map(int, input().split()))
    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]
    tx1 = data[4]
    ty1 = data[5]
    tx2 = data[6]
    ty2 = data[7]

    if (x2 == tx1 and y2 == ty1) or (x1 == tx2 and y2 == ty1) or (x2 == tx1 and y1 == ty2) or (x1 == tx2 and y1 == ty2):
        print('c')
    elif (x2 == tx1 and y2 != ty1) or (x1 == tx2 and y2 != ty1) or (x2 != tx1 and y1 == ty2) or (x1 != tx2 and y1 == ty2):
        print('b')
    elif (x2 < tx1 or tx2 < x1 or y2 < ty1 or ty2 < y1):
        print('d')
    else:
        print('a')

