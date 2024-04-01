N=int(input())
arr=list(map(int,input().split()))
temp=sorted(arr)
result=0
for t in range(N):
    result+=temp[t]*(N-t)
print(result)