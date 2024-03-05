import sys
sys.stdin=open('./15663_input.txt')
def recur(i):
    if i==M:
        
        return
    for j in range(N):
        if j not in idx[:i]:
            idx[i]=j
            recur(i+1)
        
N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
ans=[[0]*M]
idx=[0]*M
recur(0)