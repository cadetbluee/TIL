from pprint import pprint
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
dirs=[0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
move=[(-1,-1),(1,1),(-1,1),(1,-1)]
stack=[(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for _ in range(M):
    d,s=map(int,input().split())
    temp=[]
    for i,j in stack:
        
        ni=(i+dirs[d][0]*s)%N
        nj=(j+dirs[d][1]*s)%N
        temp.append((ni,nj))
        arr[ni][nj]+=1
    for ni,nj in temp:
        for m in move:
            mi=ni+m[0]
            mj=nj+m[1]
            if 0<=mi<N and 0<=mj<N and arr[mi][mj] !=0:
                arr[ni][nj]+=1
    stack=temp
    temp=[]
    for y in range(N):
        for x in range(N):
            if arr[y][x]>=2 and (y,x) not in stack:
                temp.append((y,x))
                arr[y][x]-=2
    stack=temp

result=0
for a in arr:
    for b in a:
        result+=b
print(result)
            
            