# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline
t = int(input())

def compare(people):
    if len(people) == 1:
        return 1
    total = 1
    min_rank = people[0][1]
    for i in range(1, len(people)):
        if people[i][1] < min_rank:
            total += 1
            min_rank = people[i][1]

    return total

for _ in range(t):
    n = int(input())
    people = []
    for _ in range(n):
        u, v = map(int, input().strip().split())
        people.append((u,v))
    people.sort(key = lambda x : x[0])
    print(compare(people))