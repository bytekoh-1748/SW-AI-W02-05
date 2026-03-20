# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

n = int(input())

test_case1 = list(map(int, input().split()))
temp = []
for _ in range(test_case1[1]):
    temp.append(list(map(int, input().split())))
