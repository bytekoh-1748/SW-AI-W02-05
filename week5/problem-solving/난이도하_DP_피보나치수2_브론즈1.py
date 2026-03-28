# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys
input = sys.stdin.readline

n = int(input())

def fib(n):
    prev1 = 0
    prev2 = 1

    if n == 0:
        return prev1
    if n == 1:
        return prev2

    for n in range(2, n+1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2

print(fib(n))

# def fib(n, memo = None):
#     if memo is None:
#         memo = {}
    
    
#     if n == 0:
#         memo[n] = 0

#     if n == 1:
#         memo[n] = 1
#     if n in memo:
#         return memo[n]
    
#     memo[n] = fib(n-1,memo) + fib(n-2,memo)
    
#     return memo[n]

# print(fib(n, None))