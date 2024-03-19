N=int(input())
# arr=[list(map(int,input().split())) for _ in range(N)]
arr=[i for i in range(N)]
print(arr)
idx=[0]*N
visited=[]
def recur(i):
    if i==N:
        print(arr)
        return
    for j in range(i,N):
        arr[i],arr[j]=arr[j],arr[i]
        if arr[:N//2] not in visited:
            visited.append(arr[:N//2])
            recur(i+1)
        
        arr[i],arr[j]=arr[j],arr[i]
recur(0)