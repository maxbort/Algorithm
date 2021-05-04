n = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))
total = sum(distance)
least = min(city)
secondleast = city[0]

for i in range(n-1):
    if i == 0:
        price = city[i]*distance[i]
        total -= distance[i]
    elif secondleast > city[i]:
        price += city[i]*distance[i]
        total -= distance[i]
        secondleast = city[i]
    else:
        price += secondleast*distance[i]
        total -= distance[i]
    if city[i] == least:
        price += least*total
        break
print(price)