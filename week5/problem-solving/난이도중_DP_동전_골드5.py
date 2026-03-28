# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def find(m, memo, nums, index):
    total = 0
    if m == 0:
        return 1
    if m < 0 or index < 0:
        return 0
    if (m, index) in memo:
        return memo[(m, index)]
    
    total += find(m-nums[index], memo, nums, index) + find(m, memo, nums, index - 1)


    memo[(m, index)] = total

    return memo[(m, index)]


for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().strip().split()]
    m = int(input())
    memo = {}
    print(find(m, memo, nums,len(nums) -1))