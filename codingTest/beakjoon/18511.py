import itertools

N,K = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse=True)  # 7 5 1
answer = 0

length = len(str(N)) # 총 자리수

for i in range(length):
    for num in nums:
        val = num*(10**(length-i-1)) # 100, 500 700
        if answer + val <= N:
            answer += val
            break

print(answer)

'''
new_list = []
for num in list(itertools.product(nums, repeat=K)):
    if int(''.join(num)) <= N:
        new_list.append(int(''.join(num)))

print(max(new_list))
'''