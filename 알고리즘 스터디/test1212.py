def power(x,n):
    a = 1
    
    if n < 0:
        x = 1/x
        n = -n
    
    while n > 0:
        if n%2 == 0:
            x = x*x
            n = n/2
        else:
            a = a*x
            n = n-1
    return a



def apower(x,n):
    z = 1
    while n != 1:
        z = z*x
        n = n-1
    return z

print(power(3,-1))
print(apower(3,-1))




A = 5
for i in rangEa