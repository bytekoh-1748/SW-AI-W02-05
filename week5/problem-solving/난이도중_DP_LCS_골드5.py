# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
memo = {}
def dp(i, j, memo):
    if i == len(str1) or j == len(str2):
        return 0

    if (i,j) in memo:
        return memo[(i,j)]
    
    if str1[i] == str2[j]:
        memo[(i,j)] = dp(i +1, j +1, memo) + 1
    else:
        memo[(i,j)] = max(dp(i+1, j, memo), dp(i, j+1, memo))

    return memo[(i,j)]

print(dp(0,0, memo))