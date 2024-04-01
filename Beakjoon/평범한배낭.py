import sys

input= sys.stdin.readline

def dfs(i,weight,value):
    global max_value
    if i==N:
        if weight<=K:
            max_value=max(max_value,value)
        return
    if weight>K:
        return
    if 
    dfs(i+1,weight+arr[i][0],value+arr[i][1])
    dfs(i+1,weight,value)

N,K=map(int,input().split())
idx=[0]*N
arr=[list(map(int,input().split())) for _ in range(N)]
max_value=0
dfs(0,0,0)
print(max_value)