import sys
input = sys.stdin.readline

x = int(input())

check = 1

while x > check:
    x -= check
    check += 1
    print(x, check, "x & check  point")

    
y = check - x + 1

if check % 2 == 0:
    print(x, '/', y, sep='')
else:
    print(y, '/', x, sep='')
    

