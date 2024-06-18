import sys
import heapq
sys.stdin = open('5208_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    n=list(map(int,input().split()))
    # stack=[(i,0) for i in range(1,n[1]+2)]
    min_cnt=len(n)
    # while stack:
    #     i,cnt=stack.pop()
    #     if i+n[i]>=len(n):
    #         min_cnt=min(min_cnt,cnt+1)
    #     elif cnt>min_cnt:
    #         break
    #     for j in range(i+1,n[i]+i+1):
    #         if j<len(n):stack.append((j,cnt+1))
    # print(f'#{tc}',min_cnt)
    def recur(i,cnt):
        global min_cnt
        if i+n[i]>=len(n):
            min_cnt=min(min_cnt,cnt)
            return
        if cnt>=min_cnt:
            return
        else:
            for j in range(i+1,i+n[i]+1):
                recur(j,cnt+1)
    recur(1,0)
    print(f'#{tc}',min_cnt)