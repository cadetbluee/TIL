n=10
top,bottom,left,right=0,n-1,0,n-1
arr=[[0]*n for _ in range(n)]
num=1
while num<=n*n:
    #위
    for i in range(left,right+1):
        arr[top][i]=num
        num+=1
    top+=1
    #오른
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    #아래
    for i in range(right,left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #왼
    for i in range(bottom,top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1

for i in range(n):
    print(*arr[i])