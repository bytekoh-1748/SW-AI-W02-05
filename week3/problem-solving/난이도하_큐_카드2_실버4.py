# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque
n = int(input())
cards = deque()
for i in range(1, n+1):
    cards.append(i)

while not len(cards) == 1:
    cards.popleft()
    cards.append(cards.popleft())
    
print(cards[0])