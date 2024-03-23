import sys
sys.stdin=open("1238_input.txt")
T=10
for tc in range(1,T+1):
    length,start=map(int,input().split())
    i_G=list(map(int,input().split()))
    m_G=max(i_G)+1
    G =[[] for _ in range(m_G+1)]
    for i in range(length//2):
        ni,nj=i_G[2*i],i_G[2*i+1]
        G[ni].append(nj)
    visited=[0]*(m_G+1)
    Q=[]
    Q.append(start)
    visited[start]=1
    max_visit=0
    while Q:
        t=Q.pop(0)

        for i in G[t]:
            if visited[i]==0:
                Q.append(i)
                visited[i]=visited[t]+1
                if max_visit<visited[i]:
                    max_visit=visited[i]
        # if not visited[t]:
        #     visited[t]=True
        #     print(G[t])
        #     for i in G[t]:
        #         if not visited:
        #             Q.append(i)
    max_idx=0

    for i in range(len(visited)-1,-1,-1):
        if visited[i]==max_visit:
            max_idx=i
            break
    print(f'#{tc}',max_idx)

#강사님 풀이
# def bfs(start):
#     q=[start]
#     visited=[0]*101
#     visited[start]=1
#     #가장 깊은 depth의 가장 큰수
#     max_number=start
#     #가장 깊은 depth저장
#     max_depth=1
#     while q:
#         now=q.pop(0)
#         for to in graph[now]:
#             if visited[to]:
#                 continue
#             #depth가 더 깊어졌네
#             #현재 방문 = 이전 방문 +1 번만에 왔다
#             visited[to]=visited[now]+1
#             if max_depth<visited[to] or \
#                     (max_depth==visited[to] and max_number<to):
#                 max_depth=visited[to]
#                 max_number=to
#             q.append(to)
#         return max_number
# for tc in range(1,11):
#     N,start=map(int,input().split())
#     input_graph=list(map(int,input().split()))
#     graph=[[] for _ in range(101)]
#     for i in range(0,N,2):
#         s=input_graph[i]
#         e=input_graph[i+1]
#         graph[s].append(e)
#     r=bfs(start)
#     print(f'#{tc} {r}')