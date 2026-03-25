import sys
import pprint
sys.stdin=open('4963_input.txt')
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    island=[list(map(int,input().split()))for _ in range(h)]
    dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    cnt=0
    for i in range(h):
        for j in range(w):
         
            if island[i][j]==1:
                cnt+=1
                mark=cnt+1
                island[i][j]=mark
                stack=[(i,j)]
                while stack:
                    r,c=stack.pop()
                    for dr,dc in dirs:
                        nr=r+dr
                        nc=c+dc
                        if 0<=nr<h and 0<=nc<w and island[nr][nc]==1:
                            island[nr][nc]=mark
                            stack.append((nr,nc))
    print(cnt) 