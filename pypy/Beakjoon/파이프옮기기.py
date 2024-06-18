
sys.stdin=open('./17070_input.txt')
import sys

input=sys.stdin.readline
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
dir1=[(0,1)]
dir2=[(1,0)]
dir3=[(0,1),(1,0)]
dird=[(0,1),(1,0),(1,1)]
start=[(0,0),(0,1)]
cnt=0
Q=[]
Q.append(start)
if arr[N-1][N-1]==1:
    print(0)
else:
    while Q:
        temp=Q.pop()
        s=temp[0]
        e=temp[1]
        cntd=0
        for d in dird:
            ni=e[0]+d[0]
            nj=e[1]+d[1]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                cntd+=1
            else:
                break
        if cntd==3:
            if e[0]+1==N-1 and e[1]+1==N-1:
                cnt+=1
            else:
                Q.append([e,(e[0]+1,e[1]+1)])
        if e[0]-s[0]==1 and e[1]-s[1]==1:
            for d in dir3:
                ni=e[0]+d[0]
                nj=e[1]+d[1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj]==0:
                        if ni==N-1 and nj==N-1:
                            cnt+=1
                        else:
                            Q.append([e,(ni,nj)])
        elif e[0]-s[0]==1:
            for d in dir2:
                ni=e[0]+d[0]
                nj=e[1]+d[1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj]==0:
                        if ni==N-1 and nj==N-1:
                            cnt+=1
                        else:
                            Q.append([e,(ni,nj)])
        elif e[1]-s[1]==1:
            for d in dir1:
                ni=e[0]+d[0]
                nj=e[1]+d[1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj]==0:
                        if ni==N-1 and nj==N-1:
                            cnt+=1
                        else:
                            Q.append([e,(ni,nj)])
    print(cnt)