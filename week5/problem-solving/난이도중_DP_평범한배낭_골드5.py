# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
objects = []
for i in range(n):
    w, v = map(int,input().strip().split())
    objects.append([w,v])

memo = {}
def ns(index, capacity, objects, memo):
    if index < 0:
        return 0
    
    if (index, capacity) in memo:
        return memo[(index, capacity)]
    
    if capacity - objects[index][0] < 0:
        memo[(index, capacity)] = ns(index -1, capacity, objects, memo)
        return memo[(index, capacity)]
    
    selected = ns(index -1, capacity - objects[index][0], objects, memo) + objects[index][1]
    n_selected = ns(index -1, capacity, objects, memo)
    
    memo[(index, capacity)] = max(selected, n_selected)
    return memo[(index, capacity)]

print(ns(n -1, k, objects, memo))