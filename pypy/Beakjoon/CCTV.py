from copy import deepcopy
def recur(i,arr):
    global min_cnt
    if i==len(CCTVs):
        cnt=0
        for i in arr:
            for j in i:
                if j==0:
                    cnt+=1
        min_cnt=min(cnt,min_cnt)
        return
    if CCTVs[i][2]==1:
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            temp=deepcopy(arr)
            for j in range(m):
                ni=CCTVs[i][0]+d[0]*j
                nj=CCTVs[i][1]+d[1]*j
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                    arr[ni][nj]=1
                elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==6:
                    break
                elif 0<=ni<N and 0<=nj<M and 1<=arr[ni][nj]<=5:
                    continue
                else:
                    break
            recur(i+1,arr)
            arr=temp
    elif CCTVs[i][2]==2:
        for dir in [[(0,1),(0,-1)],[(1,0),(-1,0)]]:
            temp=deepcopy(arr)
            for d in dir:
            
                for j in range(m):
                    ni=CCTVs[i][0]+d[0]*j
                    nj=CCTVs[i][1]+d[1]*j
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                        arr[ni][nj]=1
                    elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==6:
                        break
                    elif 0<=ni<N and 0<=nj<M and 1<=arr[ni][nj]<=5:
                        continue
                    else:
                        break
            recur(i+1,arr)
            arr=temp
    elif CCTVs[i][2]==3:
        for dir in [[(0,-1),(-1,0)],[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)]]:
            temp=deepcopy(arr)
            for d in dir:
                for j in range(m):
                    ni=CCTVs[i][0]+d[0]*j
                    nj=CCTVs[i][1]+d[1]*j
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                        arr[ni][nj]=1
                    elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==6:
                        break
                    elif 0<=ni<N and 0<=nj<M and 1<=arr[ni][nj]<=5:
                        continue
                    else:
                        break
            recur(i+1,arr)
            arr=temp
    elif CCTVs[i][2]==4:
        for dir in [[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]]:
            temp=deepcopy(arr)
            for d in dir:
                for j in range(m):
                    ni=CCTVs[i][0]+d[0]*j
                    nj=CCTVs[i][1]+d[1]*j
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                        arr[ni][nj]=1
                    elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==6:
                        break
                    elif 0<=ni<N and 0<=nj<M and 1<=arr[ni][nj]<=5:
                        continue
                    else:
                        break
            recur(i+1,arr)
            arr=temp
    elif CCTVs[i][2]==5:
        temp=deepcopy(arr)
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            for j in range(m):
                ni=CCTVs[i][0]+d[0]*j
                nj=CCTVs[i][1]+d[1]*j
                if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                    arr[ni][nj]=1
                elif 0<=ni<N and 0<=nj<M and arr[ni][nj]==6:
                    break
                elif 0<=ni<N and 0<=nj<M and 1<=arr[ni][nj]<=5:
                    continue
                else:
                    break
        recur(i+1,arr)
        arr=temp

N,M=map(int,input().split())
m=max(N,M)
arr=[list(map(int,input().split()))for _ in range(N)]
CCTVs=[]
min_cnt=N*M
for i in range(N):
    for j in range(M):
        if 1<=arr[i][j]<=5:
            CCTVs.append((i,j,arr[i][j]))
recur(0,arr)
print(min_cnt)