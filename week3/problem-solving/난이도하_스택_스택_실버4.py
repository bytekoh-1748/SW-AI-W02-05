# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys
def push(stack, x):
    stack.append(x)
    
def pop(stack):
    if stack: 
        print(stack.pop())
        return
    print(-1)
    
def size(stack):
    print(len(stack))

def empty(stack):
    if stack:
        print(0)
        return
    print(1)

def top(stack):
    if stack:
        print(stack[len(stack) -1])
        return
    print(-1)

command_map = {
    "push" : push,
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "top" : top
}

n = int(input())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    fnc = command_map[command[0]]
    arg = command[1:]
    fnc(stack, *arg)
