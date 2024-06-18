import sys
sys.stdin=open("5102_input.txt")


def bfs(start,N,goal):
    Q=[]
    visited=[0]*(N+1)
    Q.append(start)
    visited[start]=1
    while Q:
        t=Q.pop(0)
        if t==goal:
            return visited[t]-1 #최단경로
        for i in adjl[t]:
            if visited[i]==0:
                Q.append(i)
                visited[i]=visited[t]+1
    return 0


T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    adjl=[[] for _ in range(V+1)]
    for i in range(E):
        n1,n2=map(int,input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S,G=map(int,input().split())
    print(f'#{tc}',bfs(S,V,G))