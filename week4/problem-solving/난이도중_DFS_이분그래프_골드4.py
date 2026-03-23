# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707
import sys
input = sys.stdin.readline
k = int(input())
for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V+1)
    stack = []
    is_bipartite = True
    for i in range(1, V+1):
        if visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            while stack:
                temp = stack.pop()
                for node in graph[temp]:
                    if visited[temp] == visited[node]:
                        is_bipartite = False
                        break
                    elif visited[temp] == 1 and visited[node] == 0:
                        visited[node] = 2
                        stack.append(node)
                    elif visited[temp] == 2 and visited[node] == 0:
                        visited[node] = 1
                        stack.append(node)
                if not is_bipartite:
                    break
            if not is_bipartite:
                    break
    if is_bipartite:
        print("YES")    
    else:
        print("NO") 

'''
import sys
input = sys.stdin.readline

# 이분 그래프 여부를 판별하는 함수
def is_bipartite_graph(V, graph):
    visited = [0] * (V + 1)
    
    for i in range(1, V + 1):
        if visited[i] == 0:
            stack = [i]
            visited[i] = 1  # 첫 정점은 1로 색칠
            
            while stack:
                curr = stack.pop()
                
                for nxt in graph[curr]:
                    if visited[nxt] == 0:  # 미방문 정점
                        # 현재 정점의 색상과 반대되는 색상(-1 곱하기)을 칠함
                        visited[nxt] = -visited[curr] 
                        stack.append(nxt)
                    elif visited[nxt] == visited[curr]:  # 모순 발생
                        return False  # 즉시 False 반환 후 함수 종료
    return True

def solve():
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        graph = [[] for _ in range(V + 1)]
        
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            
        if is_bipartite_graph(V, graph):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()'''
    