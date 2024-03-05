import sys
sys.stdin=open('./15663_input.txt')
def recur(i):
    if i==M:
        ans=[0]*M
        for k in range(M):
            ans[k]=arr[idx[k]]
        list_ans.add(tuple(ans))
        
        return
    for j in range(N):
        if i!=0 and j >=max(idx[:i]):
            idx[i]=j
            recur(i+1)
        elif i==0:
            idx[i]=j
            recur(i+1)
        
N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

idx=[0]*M
list_ans=set()
recur(0)
list_ans=list(list_ans)
list_ans.sort()
for i in list_ans:
    print(*i)