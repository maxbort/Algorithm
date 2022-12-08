n = int(input())

stu = []

for i in range(n):
    student = tuple(input().split())
    stu.append(student)
    
stu.sort(key=lambda x:x[1])

for i in stu:
    print(i[0], end = ' ')