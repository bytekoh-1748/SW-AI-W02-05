# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

n = int(input())
squares = [list(map(int, input().split())) for _ in range(n)]

def finder(x,y,size):
    if size == 1:
        if squares[x][y] == 1:
            return (0,1)
        return (1,0)
    is_all = squares[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if squares[i][j] != is_all:
                half = size //2
                w1 , b1 = finder(x,y,half)
                w2 , b2 = finder(x + half,y,half)
                w3 , b3 = finder(x,y + half,half)
                w4 , b4 = finder(x + half,y + half,half)
                return (w1+w2+w3+w4, b1+b2+b3+b4)
            
    if is_all == 1:
        return (0,1)
    return (1,0)

tupl = finder(0,0,n)

print(tupl[0])
print(tupl[1])