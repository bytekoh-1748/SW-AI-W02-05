# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

n = int(input())
tests = []
for _ in range(n):
    num = list(map(int, input().split()))
    tests.append(num)

for test in tests:
    sum = 0
    student_pass = 0
    student_num = test[0]
    for i in range(1, student_num + 1):
        sum += test[i]

    avg = sum/student_num
    for i in range(1, student_num + 1):
        if test[i] > avg:
            student_pass += 1
    print(str("{:.3f}".format((student_pass/student_num)* 100)) + "%")

