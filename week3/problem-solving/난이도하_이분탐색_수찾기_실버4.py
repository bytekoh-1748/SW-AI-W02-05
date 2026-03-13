# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

def find_num(nums, target, left, right):
    while left <= right:
        mid = (left + right)//2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid -1
        else:
            return 1
    return 0

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

m = int(input())
targets = list(map(int,input().split()))


for target in targets:
    print(find_num(nums, target, 0, len(nums) -1))
    
