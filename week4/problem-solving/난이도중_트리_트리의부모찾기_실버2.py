# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

stack =[1]
parent = [0] * (n+1)
parent[1] = -1

while stack:
    prev = stack.pop()
    for node in graph[prev]:
        if parent[node] == 0:
            stack.append(node)
            parent[node] = prev

for i in range(2,n+1):
    print(parent[i])