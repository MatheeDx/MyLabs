import os
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

os.system('pause')
