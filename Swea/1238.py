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