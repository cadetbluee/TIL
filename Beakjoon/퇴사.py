def recur(i,val):
    global max_val
    if i>N:
        return
    if i==N:
        max_val=max(max_val,val)
        return
    recur(i+arr[i][0],val+arr[i][1])
    recur(i+1,val)
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
max_val=0
recur(0,0)
print(max_val)