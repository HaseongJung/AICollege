'''
A = int(input())
T = int(input())
flag = int(input())

cnt = 1
cnt_flag = 0
while (cnt_flag == T):
    sentence = [0, 1, 0, 1]
    for i in range(4, A):
        sentence[i] = 
        if len(sentence) == A:
            break
        
        cnt += 1
'''


A = int(input())
T = int(input())
B = int(input())

status = []
b = 1
d = 1
n = 0

while True:
    prev = b
    n += 1
    for _ in range(2):
        status.append((b, 0))
        b += 1
        status.append((d, 1))
        d += 1
    for _ in range(n+1):
        status.append(b, 0)
        b+=1
    for _ in range(n+1):
        status.append(d, 0)
        d+=1
        
    if prev < T <= b:
        print(status.index(T, B) % A)