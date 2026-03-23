# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
values = [0 for _ in range(n)]
for i in range(n):
    values[i] = int(input())

mydeque = deque([(0,0)])
visited = set()

while mydeque:
    current_sum, current_level = mydeque.popleft()
    for value in values:
        next_sum = current_sum + value
        if next_sum == k:
            current_level += 1
            print(current_level)
            exit()
        if next_sum not in visited and next_sum<k:
            mydeque.append((next_sum, current_level + 1))
            visited.add(next_sum)

print(-1)