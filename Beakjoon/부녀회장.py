T=int(input())
for tc in range(T):
    k=int(input())
    n=int(input())
    arr=[[0]*n for _ in range(k+1)]
    for l in range(n):
        arr[0][l]=l+1
    for i in range(1,k+1):
        for j in range(1,n+1):
            arr[i][j-1]=sum(arr[i-1][:j])
    print(arr[k][n-1])