# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

n = int(input())
square = []
visited = [[False]* n for _ in range(n)]
stack = [(0,0)]
visited[0][0] = True
for _ in range(n):
    square.append(list(map(int, input().split())))

while stack:
    r, c = stack.pop()
    jump = square[r][c]

    if square[r][c] == -1:
        print("HaruHaru")
        exit()
        
    if jump == 0:
        continue
 
    if r + jump < n and not visited[r + jump][c]:
            visited[r + jump][c] = True
            stack.append((r + jump, c))
    if c + jump < n and not visited[r][c + jump]:
            visited[r][c + jump] = True
            stack.append((r, c + jump))


print("Hing")

