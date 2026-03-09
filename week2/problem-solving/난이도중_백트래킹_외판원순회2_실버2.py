# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]

result = []
    
def backtracking(start, left, current, city_sum):
    if left == []:
        if w[current][start[0]] == 0:
            return
        

    for 


backtracking(0, [], 0)
print(min(result))