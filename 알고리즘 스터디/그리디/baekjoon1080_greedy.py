import sys

input = sys.stdin.readline

def cal(matrix,a,b):
    for k in range(3):
        for l in range(3):
            if matrix[a+k][b+l] == 0:
                matrix[a+k][b+l] = 1
            else:
                matrix[a+k][b+l] = 0
    return matrix

n, m = map(int,input().split())

Amatrix = []
Bmatrix = []
test = []

for _ in range(n):
    Amatrix.append(list(map(int,input().rstrip())))
for _ in range(n):
    Bmatrix.append(list(map(int,input().rstrip())))

answer = 0

if Amatrix == Bmatrix:
    print(answer)

else:
    if n < 2 or m < 2:
        print(-1)
    else:
        for i in range(n-2):
            for j in range(m-2):
                if Amatrix == Bmatrix:
                    break
                if Amatrix[i][j] != Bmatrix[i][j]:
                    answer += 1
                    Amatrix = cal(Amatrix,i,j)
                
        if Amatrix == Bmatrix:
            print(answer)
        else:
            print(-1)
