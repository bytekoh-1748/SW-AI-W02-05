# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

closest = sys.maxsize
left = 0
right = len(nums) -1
result_r = 0
result_l = 0
while closest != 0 and left != right:
    temp = nums[right] + nums[left]
    if abs(temp) < abs(closest):
        closest = temp
        result_r = nums[right]
        result_l = nums[left]
    if temp > 0:
        right = right -1
    elif temp < 0:
        left = left + 1
    else:
        break

print(f"{result_l} {result_r}")