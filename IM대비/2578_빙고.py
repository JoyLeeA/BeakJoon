def check(n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                board[i][j] = 0
                return


def bingo():
    cnt = 0
    for x in range(5):
        for y in range(5):
            if board[x][y] != 0:
                break
        else:
            cnt +=1

    for x in range(5):
        for y in range(5):
            if board[y][x] != 0:
                break
        else:
            cnt +=1

    for x in range(5):
        if board[x][x] != 0:
                break
    else:
        cnt +=1
    
    for x in range(5):
        if board[x][-1-x] != 0:
            break
    else:
        cnt +=1

    if cnt >= 3:
        return 1
    return 0

board=[]
for _ in range(5):
    board.append(list(map(int,input().split())))

data=[]
for _ in range(5):
    data.append(list(map(int,input().split())))

result = 0
for x in range(5):
    for y in range(5):
        check(data[x][y])
        if bingo():
            result = 5*x + y+1 
            break
    else:
        continue
    break
print(result)
             

