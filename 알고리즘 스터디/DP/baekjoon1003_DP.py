t = int(input())

for _ in range(t):
    n = int(input())
    z_list = [1,0,1]
    o_list = [0,1,1]

    length = len(z_list)

    if n >= length:
        for i in range(length,n+1):
            z_list.append(z_list[i-2] + z_list[i-1])
            o_list.append(o_list[i-2] + o_list[i-1])
    print(z_list[n],o_list[n])
