# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
time = [-1] * (n+1)
indegree = [-1] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i], indegree[i] = data[0], data[1]
    for node in data[2:]:
        graph[node].append(i)

result = time[:]
working = deque([i for i in range(1, n+1) if indegree[i] == 0])

while working:
    temp = working.popleft()
    for node in graph[temp]:
        result[node] = max(result[node], result[temp] + time[node])
        indegree[node] -= 1
        if indegree[node] == 0:
            working.append(node)
            
print(max(result))