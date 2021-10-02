import os
print('Task (1-5):')
task = int(input())

if task == 1:
    lis = []
    print('Enter K = ', end='')
    k = int(input())-1
    print('Enter L = ', end='')
    l = int(input())-1

    print('Enter lenght array = ', end='')
    n = int(input())

    sum = 0
    for i in range(n):
        lis.append(int(input()))
        if i >= k and i <= l:
            sum += lis[i]

    print(sum / (l-k+1))
elif task == 2:
    lis = []
    print('Enter lenght array = ', end='')
    n = int(input())
    for i in range(n):
        lis.append(int(input()))
    lis.sort()
    d = lis[1] - lis[0]
    fl = True
    for i in range(1, n-1):
        if lis[i+1] - lis[i] != d:
            fl = False
            break
    if fl:
        print(d)
    else:
        print(0)
elif task == 3:
    lis = []
    print('Enter lenght array = ', end='')
    n = int(input())
    min = 0
    num = 0
    for i in range(n):
        num = int(input())
        if i % 2 != 0:
            if min == 0 or num < min:
                min = num
    print(min)

elif task == 4:
    lis = []
    print('Enter lenght array = ', end='')
    n = int(input())
    for i in range(n):
        lis.append(int(input()))
    if lis[0] > lis[1]:
        maxx = lis[0]
    for i in range(1,n):
        if (lis[i] > lis[i-1]) and (lis[i] > lis[i+1]):
            maxx = lis[i]
    if lis[n-1] > lis[n-2]:
        maxx = lis[n-1]
    print(maxx)
elif task == 5:
    print("Task 5")

os.system('pause')
