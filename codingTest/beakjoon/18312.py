import sys
from itertools import combinations

# N, K = map(int, input().split())
# answer = 0

# if K > 6:
#     K_hour = 24-K
#     K_sec = 5
#     K_min = 5
#     answer = K_hour * K_sec * K_min
# else:
#     K_hour = 24-K
#     K_sec = 10
#     K_min = 10
#     answer = K_hour * K_sec * K_min

# print(answer)


N, K = map(int, input().split())
K = str(K)

cnt = 0

# 시간 / 분 / 초
for h in range(0, N+1): # 0~N
    if h < 10:
        h = '0' + str(h)
    else:
        h = str(h)

    for m in range(0, 60):  # 0~59
        if m < 10:
            m = '0' + str(m)
        else:
            m = str(m)

        for s in range(0, 60):   # 0~59
            if s < 10:
                s = '0' + str(s)
            else:
                s = str(s)

            if str(K) in h+m+s:
                cnt += 1

print(cnt)