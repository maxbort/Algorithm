import sys
input = sys.stdin.readline

word = input().rstrip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    word = word.replace(i,'a')
    
print(len(word))