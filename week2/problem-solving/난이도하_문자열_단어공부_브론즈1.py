# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

str = input()
str_u = str.upper()
mydict = {}
doublemax = 0
max_v = 0
max_k = ''

letters = list(str_u)
for letter in letters:
    if letter in mydict:
        mydict[letter] += 1
    else: 
        mydict[letter] = 1
    
for key, value in mydict.items():
    if value > max_v:
        max_v = value
        max_k = key
    elif value == max_v:
        doublemax = value
        
if doublemax == max_v:
    print('?')
else:
    print(max_k)
