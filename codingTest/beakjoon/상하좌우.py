N = int(input())
plans = input().split()

# dir = ['L', 'R', 'U', 'D']

x, y = 1, 1

for plan in plans:
    if plan == 'L':
        y -= 1
        if y == 0:
            y += 1
    elif plan == 'R':
        y += 1
        if y == N:
            y -= 1
    elif plan == 'U':
        if x-1 == 0 :
            continue
        x -= 1
    else:
        if x+1 == N:
            continue
        x += 1
        
print(x, y)