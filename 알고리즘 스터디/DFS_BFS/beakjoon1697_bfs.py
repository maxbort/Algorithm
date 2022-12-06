from collections import deque

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        subin = queue.popleft()
        if subin == k:
            print(root[subin])
            break
        for i in (subin -1, subin +1, subin*2):
            if 0<= i <= 10**5 and root[i] == 0 :
                root[i] = root[subin] + 1
                queue.append(i)
            
    
    
    

n,k = map(int,input().split())
root =[0] * (10**5+1)

bfs()