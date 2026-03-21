# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

t = int(input())

def travel():
    nm = list(map(int,input().split()))
    n = nm[0]
    m = nm[1]
    graph = [[] for _ in range(n + 1)]
    plane = 0

    for _ in range(m):
        uv = list(map(int,input().split()))
        graph[uv[0]].append(uv[1])
        graph[uv[1]].append(uv[0])
    print(n-1)



for _ in range(t):
    travel()