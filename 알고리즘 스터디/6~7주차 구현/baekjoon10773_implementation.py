stack = []
k=int(input())

for i in range(k):
    data = int(input())
    if data == 0:
        stack.pop()
    else:
        stack.append(data)
print(sum(stack))