import sys

N, M, R = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
print(arr)