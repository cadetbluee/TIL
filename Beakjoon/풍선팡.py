N=int(input())
arr=list(map(int,input().split()))
i=1
ans=[]
while len(ans)<N:
    ans.append(i)
    if i-2<0:
        i=len(arr)-1
    elif i-2>len(arr)-1:
        i=2
        
    i=i+arr.pop(i-2)
print(ans)
