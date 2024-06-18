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
#강사님 풀이
# def dfs(cnt,sum_height):
#     global ans
#     #기저조건
#     #1. 모든 점원이 탑을 쌓으면 종료
#     #2. 키의 합이 B이상이면 종료
#     # -> 현재까지 쌓은 탑의 높이
#     if sum_height>=B:
#         #제일 높이가 낮은 탑이 정답
#         ans=min(ans,sum_height)
#         return
#     if cnt==N:
#         return
#     dfs(cnt+1,sum_height+arr[cnt])
#     dfs(cnt+1,sum_height)
# T=int(input())
# for tc in range(1,T+1):
#     N,B=map(int,input().split())
#     arr=list(map(int,input().split()))
#     ans=int(1e9)
#     dfs(0,0)
#     print(f'#{tc} {abs(ans-B)}')