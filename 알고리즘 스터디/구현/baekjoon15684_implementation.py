import sys
input = sys.stdin.readline

n,m,h = map(int,input().split())

line = [list(map(int,input().split())) for _ in range(m)]

line.sort(key= lambda x : x[0])

