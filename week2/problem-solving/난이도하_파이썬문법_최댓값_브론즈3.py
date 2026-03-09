# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)

max_num = max(numbers)

print(max_num)
print(numbers.index(max_num) + 1)