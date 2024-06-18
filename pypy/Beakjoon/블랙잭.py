def black_jack(i,s):
    global max_M
    if s>M:
        return
    elif i==3:
        if s>max_M:
            max_M=s
        return
    for j in range(N):
        if j not in idx[:i]:
            idx[i]=j
            black_jack(i+1,s+arr[idx[i]])
N,M=map(int,input().split())
arr=list(map(int,input().split()))
max_M=0
idx=[0]*3
black_jack(0,0)
print(max_M)