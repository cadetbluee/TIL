import sys
sys.stdin = open('1486_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    N,B=map(int,input().split())
    heights=list(map(int,input().split()))
    result=sum(heights)
    for i in range(1<<N):
        sum_sub=0
        for j in range(N):
            if i&(1<<j):
                sum_sub+=heights[j]
        if sum_sub>=B:
            result=min(sum_sub,result)
    print(f'#{tc}',result-B)