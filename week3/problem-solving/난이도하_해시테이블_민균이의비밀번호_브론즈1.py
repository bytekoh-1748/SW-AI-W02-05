# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

n = int(input())
strs = list(input() for _ in range(n))

my_dict = {str: str[::-1] for str in strs}

for str in strs:
    if my_dict[str] in my_dict:
        if my_dict[my_dict[str]] == str:
            mid = (len(str) + 1) // 2 - 1
            print(f"{len(str)} {str[mid]}")
            break
    if my_dict[str] == str:
        mid = (len(str) + 1) // 2 - 1
        print(f"{len(str)} {str[mid]}")
        break