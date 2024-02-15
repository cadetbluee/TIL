import sys
sys.stdin=open("5099_input.txt")
# T=int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     Ci = list(map(int, input().split()))
#     cQ=[-1]*M
#     # front=0
#     # rear=0
#
#     stack=[]
#     for q in range(N):
#         cQ[q]=Ci[q]
#         stack.append(q)
#     i=N
#     while i<M:
#         # if (rear + 1) % (N+1)==front:
#         while 0 not in cQ:
#             for j in stack:
#                 cQ[j]=cQ[j]//2
#
#         while 0 in cQ:
#             idx=cQ.index(0)
#             cQ[idx]=-1
#             stack.pop(stack.index(idx))
#             if i<M:
#                 cQ[i]=Ci[i]
#                 stack.append(i)
#                 i+=1
#         print(cQ)
#         # rear=1
#         # else:
#         #     rear=(rear + 1) % (N+1)
#         #     cQ[i]=Ci[i]
#         #     stack.append(i)
#         #     i+=1
#
#     while 0 in cQ:
#         idx = cQ.index(0)
#         cQ[idx] = -1
#         stack.pop(stack.index(idx))
#     while 0 not in cQ:
#         for j in stack:
#             cQ[j]=cQ[j]//2
#     print(f'#{tc}',cQ.index(max(cQ))+1)
from collections import deque
T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    oven=[]
    remain=[]
    for i in range(N):
        oven.append([i+1,Ci[i]])
    for i in range(N,M):
        remain.append([i+1,Ci[i]])

    while len(oven)>1:
        pizza=oven.pop(0)
        pizza[1]//=2
        if pizza[1]==0:
            if len(remain)>0:
                oven.append(remain.pop(0))
        else:
            oven.append(pizza)
    print(f'#{tc}',oven[0][0])