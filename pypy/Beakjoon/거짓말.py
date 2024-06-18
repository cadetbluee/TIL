def dfs(start):
    stack=[start]
    while stack:
        now=stack.pop()
        if visited[now]:
            continue
        visited[now]=1
        for to in graph[now]:
            stack.append(to)
N,M=map(int,input().split())
eye=list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
parties=[[] for _ in range(M)]
for i in range(M):
    people=list(map(int,input().split()))
    for j in range(1,people[0]):
        graph[people[j]].append(people[j+1])
        graph[people[j+1]].append(people[j])
    parties[i]=people[1:]

if eye[0]==0:
    print(M)
else:
    visited=[0]*(N+1)
    for i in range(1,eye[0]+1):
        dfs(eye[i])
    innocent=[]
    for v in range(1,N+1):
        if visited[v]==0:
            innocent.append(v)
    cnt=0
    for party in parties:
        lie=1
        for p in party:
            if p not in innocent:
                lie=0
                break
        if lie:
            cnt+=1
    print(cnt)