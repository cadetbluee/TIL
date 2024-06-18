N,K=map(int,input().split())
arr=[[0,0] for _ in range(6)]
for _ in range(N):
    S,Y=map(int,input().split())
    arr[Y-1][S]+=1
cnt=0
for i in arr:
    for j in i:
        while j>0:
            j-=K
            cnt+=1
print(cnt)