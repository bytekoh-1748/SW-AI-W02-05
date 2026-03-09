# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

n = int(input())
str = ''

for _ in range(n):
    test = input().split()
    repeat = int(test[0])
    s = test[1]
    for i in range(0, len(s)):
        rs = s[i] * repeat
        str += rs

    print(str)
    str = ''
