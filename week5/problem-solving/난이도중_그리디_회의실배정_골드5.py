# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

n = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key= lambda x : (x[1], x[0]))

total = 0
finish = -1

for start, end in meetings:
    if start >= finish:
        total += 1
        finish = end
print(total)

# meetings = []
# total = 1

# for _ in range(n):
#     meetings.append(tuple(map(int, input().split())))

# meetings.sort(key= lambda x : (x[1], x[0]))

# finish = meetings[0][1]

# for meeting in meetings[1:]:
#     if meeting[0] >= finish:
#         total += 1
#         finish = meeting[1]

# print(total)