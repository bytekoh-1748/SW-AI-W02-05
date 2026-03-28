# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
small = set()
for _ in range(m):
    small.add(int(input()))

memo = {}

def ns(curr, x, memo):
    if curr == n:
        return 0
    
    if x -1 <0 or curr in small or curr > n:
        return sys.maxsize
    
    if (curr, x) in memo:
        return memo[(curr, x)]
    
    temp = min(ns(curr + x+1, x+1, memo), ns(curr + x, x, memo), ns(curr + x-1, x-1, memo))
    if temp == sys.maxsize:
        memo[(curr, x)] = temp
    else:
        memo[(curr, x)] = temp + 1

    return memo[(curr, x)]

a = ns(2, 1, memo)
if a == sys.maxsize:
    print(-1)
else:
    print(a + 1)