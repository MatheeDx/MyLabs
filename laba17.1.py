import os
print('Task (1-5):')
task = int(input())

if task == 1:
    lis = []
    print('Enter K = ', end='')
    k = int(input())-1
    print('Enter L = ', end='')
    l = int(input())-1

    print('Введите длину массива = ', end='')
    n = int(input())

    sum = 0
    for i in range(n):
        lis.append(int(input()))
        if i >= k and i <= l:
            sum += lis[i]

    print(sum / (l-k+1))
elif task == 2:
    lis = []
    print('Введите длину массива = ', end='')
    n = int(input())
    print("Введите элементы массива:")
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
        print("\nЭлементы массива образуют арифметическую прогрессию поэтому\n я вывожу разность прогрессии = ", d)
    else:
        print("\nЭлементы массива не образуют арифметическую прогрессию\n поэтому я вывожу 0")
elif task == 3:
    lis = []
    print('Введите длину массива = ', end='')
    n = int(input())
    min = 0
    num = 0
    print("Введите элементы массива:")
    for i in range(n):
        num = int(input())
        if i % 2 != 0:
            if min == 0 or num < min:
                min = num
    print("Готово!) \nМинимальный элемент из элементов массива с четными номерами =", min)
elif task == 4:
    lis = []
    print('Введите длину массива = ', end='')
    n = int(input())
    print("Введите элементы массива:")
    for i in range(n):
        lis.append(int(input()))
    if lis[0] > lis[1]:
        maxx = lis[0]
    for i in range(1,n-1):
        if (lis[i] > lis[i-1]) and (lis[i] > lis[i+1]):
            maxx = lis[i]
    if lis[n-1] > lis[n-2]:
        maxx = lis[n-1]
    print("Готово!) \nНомер последнего локального максимума массива =", maxx)
elif task == 5:
    lis = []
    print('Введите длину массива = ', end='')
    n = int(input())
    print("Введите элементы массива:")
    for i in range(n):
        lis.append(int(input()))
    buff = []
    for i in range(n):
        buff.append(lis[i])
    buff.sort()
    num = 0
    for i in range(n-1):
        if buff[i] == buff[i+1]:
            num = buff[i]
    fl = False
    if num != 0:
        print("Одинаковые элементы массива:")
        for i in range(n):
            if lis[i] == num:
                if not fl:
                    print("Позиция первого элемента -", i+1)
                    fl = True
                else:
                    print("Позиция второго элемента -", i+1)
    else:
        print("Одинаковых элементов массива нет(")

os.system('pause')