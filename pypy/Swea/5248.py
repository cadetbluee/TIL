import sys
sys.stdin=open('5248_input.txt')

def make_set(n):
    parent=list(range(n+1))
    rank=[0]*(n+1)
    return parent, rank
def find_set(x): # 대표자(루트)를 찾는 함수
    # while x!=parent[x]:
    #     x=parent[x]
    #return x
    # if parent[x]==x:
    #     return x
    # return find_set(parent[x])
    if parent[x] == x:
        return x
    #경로 압축
    parent[x]=find_set(parent[x])
    return parent[x]

def union(x,y):
    root_x,root_y=find_set(x),find_set(y)
    if root_x!=root_y:
        #랭크가 더 높은 루트를 기준으로 합치기
        if rank[root_x]>rank[root_y]:
            parent[root_y]=root_x
        else:
            parent[root_x]=root_y
            if rank[root_x]==rank[root_y]:
                rank[root_y]+=1

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    M_list=list(map(int,input().split()))
    parent,rank=make_set(N)
    for i in range(M):
        union(M_list[i*2],M_list[i*2+1])
    result=set()
    for i in range(1,N+1):
        result.add(find_set(i))
    print(parent)
    print(f'#{tc}',len(result))