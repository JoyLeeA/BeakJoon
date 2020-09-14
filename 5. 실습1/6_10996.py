N = int(input())
if N==1:
    print('*')
elif N%2: #홀수
    for i in range(1, N*2+1):
        num = (N//2)+1
        if i%2:
            for k in range(num):
                print('* ', end ='')
            print()
        else:
            for l in range(num-1):
                print(' *', end='')
            print()
else: #짝수
    for i in range(1, N*2+1):
        num = (N//2)+1
        if i%2:
            for k in range(num-1):
                print('* ', end ='')
            print()
        else:
            for l in range(num-1):
                print(' *', end='')
            print()
