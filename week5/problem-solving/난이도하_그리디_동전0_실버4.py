# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums= []
total = 0

for _ in range(n):
    nums.append(int(input()))

for coin in reversed(nums):
    total += k // coin
    k = k % coin

print(total)