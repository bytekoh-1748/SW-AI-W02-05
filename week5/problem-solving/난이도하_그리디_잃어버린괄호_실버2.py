# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline
nums = input().strip().split('-')

total = sum(map(int, nums[0].split('+')))

for num in nums[1:]:
    total -= sum(map(int, num.split('+')))

print(total)