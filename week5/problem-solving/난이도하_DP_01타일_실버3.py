# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

import sys
input = sys.stdin.readline

n = int(input())

def fib(n):
    prev1 = 1
    prev2 = 2

    if n == 1:
        return prev1
    if n == 2:
        return prev2
    
    for i in range(3, n+1):
        prev1, prev2 = prev2, (prev1 + prev2) % 15746
    
    return prev2

print(fib(n))




# def fib(n, memo = None):
#     if memo is None:
#         memo = {}
        
#     if n == 1:
#         memo[n] = 1
#     if n == 2:
#         memo[n] = 2
        
#     if n in memo:
#         return memo[n]
    
#     memo[n] = (fib(n-1, memo) + fib(n-2, memo)) % 15746
    
#     return memo[n]

# print(fib(n,None))