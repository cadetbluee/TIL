def recur(i):
    if i==5:
        print(idx)
        return
    for j in range(1,5):
        idx[i]=j
        recur(i+1)
# N=int(input())
# arr=[list(map(int,input().split())) for _ in range(N)]
idx=[0]*5
recur(0)