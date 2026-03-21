# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

visited = {1}
infected = [1]
for _ in range(m):
    inputs = list(map(int, input().split()))
    graph[inputs[0]].append(inputs[1])
    graph[inputs[1]].append(inputs[0])

while infected:
    temp = infected.pop()
    for node in graph[temp]:
        if node not in visited:
            infected.append(node)
            visited.add(node)

print(len(visited) -1)