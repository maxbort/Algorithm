sugal = int(input())
vinyl = 0

while True:
    if sugal % 5 == 0:
        a = sugal // 5
        sugal = 0
        break
    elif sugal < 3:
        break
    sugal -= 3
    vinyl += 1

if sugal == 0:
    print(vinyl + a)
else:
    print(-1)