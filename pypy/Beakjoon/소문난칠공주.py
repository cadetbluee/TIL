import sys
sys.stdin=open("1941_input.txt")
students=[list(input()) for _ in range(5)]
# print(students)
# selected=[]
# frontier=[]
# cntS=0
# cntY=0
# ans=0
connected_list=[[]for _ in range(25)]
N=5
dir=[(1,0),(0,1),(-1,0),(0,-1)]
for r in range(N):
    for c in range(N):
        idx=r*N+c
        for d in dir:
            nr=d[0]+r
            nc=d[1]+c
            if 0<=nc<N and 0<=nr<N:
                nidx=nr*N+nc
                connected_list[idx].append(nidx)

ans_list=set()
def dfs(selected,frontier,cntS,cntY,idx):
    # global ans
   
    if len(selected)==7:
        if cntS>=4 :
            # ans+=1
            ans_list.add(tuple(sorted(selected)))
            # print(selected)
        return
    if cntY>=4:
        return
    remain=7-len(selected)
    if cntS+remain<4:
        return
    for nxt in list(frontier):
        # if nxt<idx:
        #     continue
        if nxt in selected:
            continue
        
        new_selected = selected | {nxt}
        new_frontier = set(frontier)
        new_frontier.remove(nxt)
        for nb in connected_list[nxt]:
           
            if nb not in new_selected:
                new_frontier.add(nb)
        r,c=divmod(nxt,5)
        if students[r][c]=='S':
            dfs(new_selected,new_frontier,cntS+1,cntY,nxt)
        else:
            dfs(new_selected,new_frontier,cntS,cntY+1,nxt)
for start in range(25):
    r, c = divmod(start, 5)
    cntS = 1 if students[r][c] == 'S' else 0
    cntY = 1 - cntS

    # 처음 선택: {start}, frontier: start에 인접한 칸들
    selected0 = { start }
    frontier0 = set(connected_list[start])

    dfs(selected0, frontier0, cntS, cntY, start)

print(len(ans_list))