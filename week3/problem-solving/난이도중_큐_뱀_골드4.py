# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

coord = []
for _ in range(k):
    coord.append(list(map(int, sys.stdin.readline().split())))

l = int(sys.stdin.readline())
change = []

for _ in range(l):
    change.append(tuple(sys.stdin.readline().split()))

snake = deque()
second = 0
dir = "R"

snake.append((1,1))

while True:
    second += 1
    str = change[second - 1][1]
    for _ in range(change[second - 1][0]):
        pass


directions = {
    "T" : T,
    "R" : R,
    "L" : L,
    "D" : D
}
