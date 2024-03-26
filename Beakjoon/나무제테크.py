# from collections import deque
# import sys
# input=sys.stdin.readline
# N,M,K=map(int,input().split())
# land=[[5]*N for _ in range(N)]
# A=[list(map(int,input().split())) for _ in range(N)]
# trees=deque()
# for _ in range(M):
#     r, c, height = map(int, input().split())
#     trees.append([r-1,c-1,height])

# dirs=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
# for _ in range(K):
   
#     tree_len=len(trees)
#     fertile=[]
#     temp=[]
#     for _ in range(tree_len):
#         i,j,height=trees.popleft()
#         if land[i][j]>=height:
#             land[i][j]-=height
#             trees.append([i,j,height+1])
#             temp.append([i,j,height+1])
#         else:
#             fertile.append([i,j,height])
#     for i,j,height in fertile:
#         land[i][j]+=height//2
#     for i,j,height in temp:
      
        
#         if height%5==0:
#             for d in dirs:
#                 ni=i+d[0]
#                 nj=j+d[1]
#                 if 0<=ni<N and 0<=nj<N:
#                     trees.appendleft([ni,nj,1])
#     for r in range(N):
#         for c in range(N):
#             land[r][c]+=A[r][c]
# print(len(trees))    
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land.append([5] * N)
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

tree_info = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, age = map(int, sys.stdin.readline().split())
    tree_info[r - 1][c - 1].append(age)

for year in range(K):
    for r in range(N):
        for c in range(N):
            tree = deque()
            next_land = 0
            for age in tree_info[r][c]:
                if land[r][c] >= age:
                    land[r][c] -= age
                    tree.append(age + 1)
                else:
                    next_land += (age // 2)
            land[r][c] += next_land
            tree_info[r][c] = tree

    tmp_trees = [] # (r, c)
    for r in range(N):
        for c in range(N):
            for age in tree_info[r][c]:
                if age % 5 == 0: #
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if not (i == j == 0) and 0 <= r + i < N and 0 <= c + j < N:
                                tmp_trees.append((r + i, c + j))
            land[r][c] += A[r][c]
    for tree in tmp_trees:
        r, c = tree
        tree_info[r][c].appendleft(1)

ltree = 0
for r in range(N):
    for c in range(N):
        ltree += len(tree_info[r][c])
print(ltree)