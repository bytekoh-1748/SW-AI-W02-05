#https://www.acmicpc.net/problem/20924
import sys
input = sys.stdin.readline
nr = list(map(int, input().split()))
n = nr[0]
r = nr[1]
prev = -1
root_sum = 0


graph = {i: [] for i in range(1, n + 1)}

for _ in range(n-1):
    temp = list(map(int, input().split()))
    graph[temp[0]].append((temp[1], temp[2]))
    graph[temp[1]].append((temp[0], temp[2]))

start_node = r

while True:
    if (r != start_node and len(graph[r]) == 2 or (r==start_node and len(graph[r]) == 1)):
        for next_node, length in graph[r]:
            if next_node != prev:
                root_sum += length
                prev = r
                r = next_node
                break
    else:
        break

max_leef_sum = 0
stack = []


stack.append((r, 0, prev))

while stack:
    curr_node, curr_length, parent = stack.pop()
    if curr_length > max_leef_sum:
        max_leef_sum = curr_length
    for next_node, length in graph[curr_node]:
        if next_node != parent:
            stack.append((next_node, curr_length + length, curr_node))

print(f"{root_sum} {max_leef_sum}")
