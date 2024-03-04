def max_score(i):
    if i==N:
        print(idx)
        return
    for j in range(N):
        if j not in idx[:i]:
            idx[i]=j
            max_score(i+1)    
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
poul=0
for ining in range(N):
    idx=[0]*9