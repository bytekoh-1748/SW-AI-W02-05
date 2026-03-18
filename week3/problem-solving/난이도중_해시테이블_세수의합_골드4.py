# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

max_sum = nums[-1]


