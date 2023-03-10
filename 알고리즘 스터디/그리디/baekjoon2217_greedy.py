import sys
input = sys.stdin.readline

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

weight = 0
tot = 0
for rope in ropes:
    tot += 1
    if weight == 0:
        weight = rope
    else:
        weight += rope
        if weight/tot > rope:
            weight -= rope
            if rope*tot >= weight:
                weight = rope*tot

    
    
print(weight)
            
        
