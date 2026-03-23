# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
count = 0

def dfs(root, visited):
    stack = [root]
    visited[root] = True
    while stack:
        temp = stack.pop()
        for i in graph[temp]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)


for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i, visited)

print(count)