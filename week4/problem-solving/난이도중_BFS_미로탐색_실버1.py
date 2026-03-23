# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input().strip())))
visited = [[False] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

mydeque = deque([(0,0,1)])
visited[0][0] = True
while mydeque:
    r, c, cnt = mydeque.popleft()
    if r == n-1 and c == m-1:
        print(cnt)
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr<n and 0<= nc < m\
        and not visited[nr][nc]\
        and maze[nr][nc] == 1:
            visited[nr][nc] = True
            mydeque.append((nr,nc,cnt + 1))
    