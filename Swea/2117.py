import sys
sys.stdin=open('2117_input.txt')
def dirs (K):
    direction=[(0,0)]
    for k in range(1,K):
        direction.extend([(k,0),(0,k),(0,-k),(-k,0)])
    if K>2:
        for i in range(1,k):
            for j in range(k-1,0,-1):
                if
                direction.extend([(i, j), (-i, -j), (-i, j), (i, -j)])
    return direction
# T=int(input())
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     arr=[list(map(int,input().split())) for _ in range(N)]
#     profit=0
#     pre_profit=0
#     for K in range(1,N):
#
#         for i in range(N):
#             for j in range(N):
#                 sub_sum=-K*K-(K-1)*(K-1)
#                 for d in dirs(K):
#                     ni=i+d[0]
#                     nj=j+d[1]
#                     if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1:
#                         sub_sum+=M
#                 if sub_sum>profit:
#                     profit=sub_sum
#         if pre_profit==profit:
#             break
#         else:
#             pre_profit = profit
#             K+=1
#     print(profit)
print(dirs(4))