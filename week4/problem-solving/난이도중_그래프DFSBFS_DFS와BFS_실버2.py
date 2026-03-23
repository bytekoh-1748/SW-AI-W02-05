# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260
from collections import deque
import sys
input = sys.stdin.readline

n, m, root = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)



def dfs(root):
    stack = [root]
    visited = [False] * (n+1)
    path = []
    for i in range(1, n + 1):
        graph[i].sort(reverse=True)

    while stack:
        temp = stack.pop()
        if not visited[temp]:      
            visited[temp] = True 
            path.append(temp)
        for i in graph[temp]:
            if not visited[i]:
                stack.append(i)

    return path
                
def bfs(root):
    mydeque = deque([root])
    visited = [False] * (n+1)
    visited[root] = True
    path = []
    for i in range(1, n + 1):
        graph[i].sort()
    while mydeque:
        temp = mydeque.popleft()
        path.append(temp)
        for i in graph[temp]:
            if not visited[i]:
                mydeque.append(i)
                visited[i] = True
    return path

print(*dfs(root))
print(*bfs(root))