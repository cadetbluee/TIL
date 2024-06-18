N=int(input())
squares=[list(map(int,input().split())) for _ in range(N)]
arr=[[0]*100 for _ in range(100)]
cnt=0
for c in range(N):
    for i in range(squares[c][1],squares[c][1]+10):
        for j in range(squares[c][0],squares[c][0]+10):
            if arr[i][j]==0:
                arr[i][j]=1
                cnt+=1
            else:
                pass
print(cnt)