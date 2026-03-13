# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

n = int(input())
chess = [[0 for _ in range(n)] for _ in range(n)]

def backtracking(n):
    
    for i in range(n):
        for j in range(n):
            chess[i][j] = 1
            