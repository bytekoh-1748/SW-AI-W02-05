# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys
n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
received = []


while towers:
    temp = towers.pop()
    for i in range(len(towers)-1, 0, -1):
        if temp < towers[i]:
            received.append(i + 1)
            break
    else:
        received.append(0)


received.reverse()
for k in received:
    print(k, end =' ')