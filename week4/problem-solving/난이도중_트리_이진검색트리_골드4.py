# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 제한을 넉넉하게 늘려줍니다.
nums = list(map(int, sys.stdin.read().split()))

def search(start, end):
    if start > end:
        return 
    
    root = start
    left = start + 1
    right = end + 1
    for i in range(left, end + 1):
        if nums[root] < nums[i]:
            right = i
            break
    search(left, right -1)
    search(right, end)
    print(nums[root])

search(0, len(nums) -1)