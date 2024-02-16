import sys
sys.stdin=open("5105_input.txt")
from collections import deque
# def bfs(grapth,start):
#     queue=deque(start)
#     while queue:
#         cur_n=queue.popleft()
#         cur_i=cur_n[0]
#         cur_j=cur_n[1]
#         if arr[cur_i][cur_j]==3:
#             return visited[cur_i][cur_j]
#         # if not visited[cur_n]:
#         #     visited[cur_n]=True
#         for [i,j] in grapth[cur_i][cur_j]:
#             if not visited[i][j]:
#                 queue.append(i)
#                 visited[i][j]=visited[cur_i][cur_j]+1
#     return 0
dirs=[(1,0),(-1,0),(0,1),(0,-1)]
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    Q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start=(i,j)  # 시작점 찾기
                break
    visited=[[0]*(N) for _ in range(N)]
    result=0

    visited[start[0]][start[1]] = 1
    Q.append(start)
    while Q:
        cur=Q.pop(0)

        for d in dirs:
            ni,nj=cur[0]+d[0],cur[1]+d[1]
            if 0<=ni<N and 0<=nj<N:
                if (arr[ni][nj]==0 or arr[ni][nj]==3) and visited[ni][nj]==0:
                    Q.append((ni,nj))
                    visited[ni][nj]=visited[cur[0]][cur[1]]+1
            if arr[cur[0]][cur[1]] == 3:
                result=visited[cur[0]][cur[1]]-2
                Q=[]
                break
    print(f'#{tc} {result}')
    # for i in range(N):
    #     for j in range(N):
    #         for d in dirs:
    #             ni,nj=i+d[0],j+d[1]
    #             if 0<=ni<N and 0<=nj<N:
    #                 if arr[ni][nj]==0:
    #                     grapth[i][j].append([ni,nj])



    # # print(arr)
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] == 2:
    #             cur_i, cur_j = [i, j]  # 시작점 찾기
    #             break
    # result = 0
    # dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    #
    # # cur_i=N-1
    # # cur_j=arr[cur_i].index(2)
    # stack = []
    # i_stack = []
    # j_stack = []
    # end = 0
    # count=0
    # cnt_stack=[]
    # while True:
    #     cnt = 0
    #
    #     for d in dirs:
    #         ni = cur_i + d[0]
    #         nj = cur_j + d[1]
    #         if 0 <= ni < N and 0 <= nj < N:
    #             if arr[ni][nj] == 0:
    #                 cnt += 1
    #                 i_stack.append(ni)
    #                 j_stack.append(nj)
    #             elif arr[ni][nj] == 3:
    #                 end = 1
    #
    #     if cnt > 1:
    #         stack.append((cur_i, cur_j))
    #         cnt_stack.append(count)
    #         cur_i = i_stack.pop()
    #         cur_j = j_stack.pop()
    #         arr[cur_i][cur_j] = 1
    #         count += 1
    #
    #     elif cnt == 1:
    #         cur_i = i_stack.pop()
    #         cur_j = j_stack.pop()
    #         arr[cur_i][cur_j] = 1
    #         count += 1
    #     else:
    #         if end == 1:
    #             count+=1
    #             result = 1
    #             break
    #         elif stack:
    #             cur_i, cur_j = stack.pop()
    #             count=cnt_stack.pop()
    #         else:
    #             break
    #
    # if result==0:
    #     print(f'#{tc} {result}')
    # else:
    #     print(f'#{tc} {count}')

    #최단 경로 찾을 때는 너비우선 탐색!
    #시간 복잡도는 깊이 우선이랑 똑같음
