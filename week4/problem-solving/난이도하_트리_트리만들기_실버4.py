# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

for i in range(n-m):
    print(f"{i} {i+1}")

for i in range(n-m+1,n):
    print(f"{n-m} {i}")
