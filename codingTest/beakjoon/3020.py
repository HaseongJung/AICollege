import sys
def input():
    return sys.stdin.readline().rstrip()
import bisect

N, H = map(int, input().split())
obs = [int(input()) for _ in range(N)]

top, bot = [], []
for i in range(N):
    if i%2 == 0:
        bot.append(obs[i])
    else:
        top.append(obs[i])
top.sort()
bot.sort()


# 최종 결과 : 최소값 (파괴하는 종유석과 석순의 갯수의 합)
# => 파괴하는 종유석/석순의 개수

# 가능한 높이 범위: 1 ~ H : for문
min = 200000
cnt = 0

for h in range(1, H+1):
    b = bisect.bisect_left(bot, h)  # 석순
    t = bisect.bisect_left(top, H-h+1)  # 종유석 # H=10, h=4, 7

    cnt = N - (t+b)
    if cnt < min:
        min = cnt
        cnt = 0
    else:
        cnt += 1

print(min, cnt)