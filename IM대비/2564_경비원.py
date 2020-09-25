def small(temp1, temp2):
    if temp1 < temp2:
        return temp1
    else:
        return temp2

garo, sero = map(int,input().split()) #100이하
N = int(input()) #100이하
# 1:북 2:남 3:서 4:동
shops = [list(map(int,input().split()))for _ in range(N)]
person = list(map(int,input().split()))

result = 0
if person[0] == 1: #20
    for shop in shops:
        temp1 = temp2 = 0
        if shop[0] == 1:
            result += abs(person[1]-shop[1])
            
        elif shop[0] == 2:
            temp1 = person[1] + sero + shop[1]
            temp2 = (garo-person[1]) + sero + (garo-shop[1])
            result += small(temp1, temp2)

        elif shop[0] == 3:
            temp1 = person[1] + shop[1]
            temp2 = (garo-person[1]) + sero + garo + (sero-shop[1])
            result += small(temp1, temp2)

        elif shop[0] == 4:
            temp1 = (garo-person[1]) + shop[1]
            temp2 = person[1] + sero + garo + (sero-shop[1])
            result += small(temp1, temp2)

elif person[0] == 2:
    for shop in shops:
        temp1 = temp2 = 0
        if shop[0] == 1:
            temp1 = person[1] + sero + shop[1]
            temp2 = (garo-person[1]) + sero + (garo-shop[1])
            result += small(temp1, temp2)
            
        elif shop[0] == 2:
            result += abs(person[1]-shop[1])

        elif shop[0] == 3:
            temp1 = person[1] + (sero-shop[1])
            temp2 = (garo-person[1]) + sero + garo + shop[1]
            result += small(temp1, temp2)

        elif shop[0] == 4:
            temp1 = (garo-person[1]) + (sero-shop[1])
            temp2 = person[1] + sero + garo + shop[1]
            result += small(temp1, temp2)

elif person[0] == 3: #18
    for shop in shops:
        temp1 = temp2 = 0
        if shop[0] == 1:
            temp1 = person[1] + shop[1]
            temp2 = (sero-person[1]) + garo + sero + (garo-shop[1])
            result += small(temp1, temp2)
            
        elif shop[0] == 2:
            temp1 = (sero-person[1]) + shop[1]
            temp2 = person[1] + garo + sero + (garo-shop[1])
            result += small(temp1, temp2)

        elif shop[0] == 3:
            result += abs(person[1]-shop[1])

        elif shop[0] == 4:
            temp1 = person[1] + garo + shop[1]
            temp2 = (sero-person[1]) + garo + (sero-shop[1])
            result += small(temp1, temp2)

if person[0] == 4: #28
    for shop in shops:
        temp1 = temp2 = 0
        if shop[0] == 1:
            temp1 = person[1] + (garo-shop[1])
            temp2 = (sero-person[1]) + garo + sero + shop[1]
            result += small(temp1, temp2)
            
        elif shop[0] == 2:
            temp1 = person[1] + garo + sero + shop[1]
            temp2 = (sero-person[1]) + (garo-shop[1])
            result += small(temp1, temp2)

        elif shop[0] == 3:
            temp1 = person[1] + garo + shop[1]
            temp2 = (sero-person[1]) + garo + (sero-shop[1])
            result += small(temp1, temp2)

        elif shop[0] == 4:
            result += abs(person[1]-shop[1])

print(result)