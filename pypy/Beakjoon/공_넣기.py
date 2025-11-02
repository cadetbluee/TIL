N,M=map(int,input().split())
list=[0]*(N)
for m in range(0,M):
    i,j,k=map(int,input().split())
    for n in range(i-1,j):
        list[n]=k
print(*list)