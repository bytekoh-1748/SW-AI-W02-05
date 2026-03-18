# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
import sys

nums = list(map(int, sys.stdin.readline().split()))

r = nums[0] % nums[2]

def multiplying(r, count, mod):
    if count == 1:
        return r
    
    half_count = count //2
    half_mul = multiplying(r, half_count, mod)
    if count % 2 == 0:
        count = count//2
        return (half_mul * half_mul) % mod
    if count % 2 == 1:
        return (r * half_mul * half_mul) % mod

result = multiplying(r, nums[1], nums[2]) % nums[2]

print(result)