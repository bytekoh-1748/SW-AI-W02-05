# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
nums = list(map(int, sys.stdin.read().split()))

def search(start, end):
    if start > end:
        return nums[start]
    
    root = start
    left = start + 1
    right = 0
    for i in range(left, end + 1):
        if nums[root] < nums[i]:
            right = i
            break
    result_left = search(left, right -1 )
    result_right = search(right, end)
    return [result_left] + [result_right] + [root]

print(search(0, len(nums) -1))