def recur(i,cnt):
    global min_try
    if i==K:
        min(min_try,cnt)
        return
    if i<min(N,K):
        return
    if i>max(N,K):
        return
    if cnt>min_try:
        return
    if visited[i]==0:
        visited[i]=1
        recur(i+1,cnt+1)
        visited[i]=0
    if visited[i]==0:
        visited[i]=1
        recur(i-1,cnt+1)
        visited[i]=0
    if visited[i]==0:
        visited[i]=1
        recur(i*2,cnt)
        visited[i]=0
N,K=map(int,input().split())
visited=[0]*100000
min_try=1e9
recur(N,0)
print(min_try)