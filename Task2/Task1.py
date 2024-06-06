from math import factorial

n = int(input())

for i in range(0,n+1):
    print(' '*(n-i), end='')
    for m in range(0,i+1):
        if i == 0:
            print(1,end='')
            break
        print(int(factorial(i)/ (factorial(m)*factorial(i-m))),' ',end='')
    print()


