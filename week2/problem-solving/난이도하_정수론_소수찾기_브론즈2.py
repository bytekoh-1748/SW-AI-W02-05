# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import math

n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    flag = False
    if num == 2 or num == 3:
        flag = True
    elif num < 2 or num % 2 == 0:
        pass
    else:
        flag = True
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if (num%i == 0):
                flag = False
                break
    if (flag):
        count += 1

print(count)