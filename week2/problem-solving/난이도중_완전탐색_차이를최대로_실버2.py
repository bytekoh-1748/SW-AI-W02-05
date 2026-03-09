# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
nums = list(map(int, input().split()))
sum = 0
result = []

for i in range(n -1):
    sum += nums[i] + nums[i+1]
    result.append(sum)

def backtracking(start, current):
    if len(current) == n:
        return current
    
    for i in range(n):
        if nums[i] not in current:
            current.append(nums[i])
            
    