# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
nums = list(map(int, input().split()))

sum_max = 0


def combination(n):

    def searching(start, current_combination):
        global sum_max
        if (len(current_combination) == n-1):
            sum = 0
            for i in range(n):
                if i not in current_combination:
                    current_combination.append(i)
            for i in range(n-1):
                sum += abs(nums[current_combination[i]] - nums[current_combination[i + 1]])
            if sum_max < sum:
                sum_max = sum
            current_combination.pop()
            return

        for i in range(n):
            if i not in current_combination:
                current_combination.append(i)
                searching(i + 1, current_combination)
                current_combination.pop()
        return
    

    searching(0,[])

combination(n)

print(sum_max)