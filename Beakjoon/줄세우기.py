N=int(input())
arr=list(map(int,input().split()))
ans=[]
for num in range(1,N+1):
    ans.insert(len(ans)-arr[num-1],num)
print(*ans)