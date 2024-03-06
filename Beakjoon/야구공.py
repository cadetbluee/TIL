def max_score(i,arr,field,s,paul):
    if i==N:
        
        return
    for j in range(N):
        if j not in idx[:i]:
            idx[i]=j
            if arr[idx[i]]==0:
                max_score(i+1,arr,field,s,paul+1)
            elif arr[idx[i]]==1:
                max_score(i+1,arr,field+1,s,paul)
            elif arr[idx[i]]==2:
                max_score(i+1,arr,field+2,s,paul)
            elif arr[idx[i]]==3:
                max_score(i+1,arr,field+1,s,paul)
            else:
                max_score(i+1,arr,0,s+field+1,paul)
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
poul=0
for ining in range(N):
    idx=[0]*9
    max_score(0,arr[ining],0,0,0)