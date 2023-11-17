import copy
from collections import Counter

# 입력 코드
R, C = map(int, input().split())

graph = []

for i in range(R):
    graph.append(list(input()))


# copy본 생성
new_graph = copy.deepcopy(graph)

# 인접한 세 칸에 바다가 있는 땅 잠김
# for문 구현
for x in range(R):
    for y in range(C):
        if graph[x][y] == 'X':
            try:
                if 2 < Counter(graph[x-1][y])['.'] + Counter(graph[x][y-1])['.'] + Counter(graph[x][y+1])['.'] + Counter(graph[x+1][y])['.']:
                    new_graph[x][y] = '.'
            except:
                pass

print(f'new graph: {new_graph}')


#  출력할 지도 크기 계산
min_row = min_col = 999
max_row = max_col = 0

for x in range(R):
    if 'X' in new_graph[x]:
        max_row = x
        if min_row > x:
            min_row = x

### max_col 이상함
    for  y in range(C):
        if 'X' in new_graph[x][y]:
            max_col = y
            if min_col > y:
                min_col = y

print(new_graph[min_row:max_row+1])


# 출력
for x in range(min_row, max_row+1):
    for y in range(min_col, max_col+1):
        print(new_graph[x][y], end='')
    print()

''''    
    for area in gra:
        new_line = []
        if area == '.':
            new_line.append('0')
        else:
            new_line.append(1)
        print(new_line)
    map.append(new_line)

print(map)
'''