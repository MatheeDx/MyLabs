import math

print("Enter task number(1-5): ")
task = int(input())
if task == 1:
    print("Enter lenght: ")
    n = int(input())
    a = []
    b = []
    ab = []

    print("Enter A:")
    for i in range(n):
        a.append(int(input()))

    print("Enter B:")
    for i in range(n):
        b.append(int(input()))
    
    for i in range(n):
        ab.append(a[i])
    a = []
    for i in range(n):
        a.append(b[i])
    b = []
    for i in range(n):
        b.append(ab[i])
    print(a, b)
elif task == 2:
    print("Enter lenght: ")
    n = int(input())
    a = []
    b = []
    print("Enter A:")
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        sum = 0
        for j in range(i+1):
            sum += a[j]
        if sum/(i+1) == round(sum/(i+1)):
            b.append(int(sum/(i+1)))
        else:
            b.append(sum/(i+1))
    print(b)
elif task == 3:
    print("Enter lenght: ")
    n = int(input())
    a = []
    print("Enter A:")
    num3 = 0
    for i in range(n):
        num = int(input())
        a.append(num)
        if num % 2 != 0:
            num3 = num
    for i in range(n):
        if a[i] % 2 != 0:
            a[i] += num3
    print(a)
elif task == 4:
    print("Enter lenght: ")
    n = int(input())
    a = []
    print("Enter A:")
    for i in range(n):
        a.append(int(input()))
    mx = max(a)
    mn = min(a)
    d = False
    for i in range(n):
        if (a[i] == mn or a[i] == mx) and (not d):
            d = True
            continue
        if (a[i] == mn or a[i] == mx) and d:
            d = False
            break
        if d:
            a[i] = 0
    print(a)
elif task == 5:
    print("Enter lenght: ")
    n = int(input())
    a = []
    print("Enter A:")
    for i in range(n):
        a.append(int(input()))
    buff = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            buff = a[i]
            a[i] = a[i+1]
            a[i+1] = buff
        else:
            break
    print(a)