import sys
sys.stdin = open('5209_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    idx=[0 for i in range(n)]
    def min_cost(i,s):
        global min_re
        if i==n:
            min_re=min(min_re,s)
            return
        elif s>min_re:
            return
        for j in range(n):
            if j not in idx[:i]:
                idx[i]=j
                min_cost(i+1,s+arr[i][idx[i]])
    min_re=1e9
    min_cost(0,0)
    print(f'#{tc}',min_re)