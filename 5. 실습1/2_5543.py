bugger = 2001
drink = 2001
for i in range(5):
    if i <=2:
        temp = int(input())
        if bugger > temp:
            bugger = temp        
    else:
        temp = int(input())
        if drink > temp:
            drink = temp
price = bugger + drink - 50
print(price)