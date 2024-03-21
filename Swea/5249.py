import sys
sys.stdin = open("5249_input.txt", "r")

def find_set(x):
    if parents[x]==x:
        return x
    #경로 압축
    parents[x]=find_set(parents[x])
    return parents[x]
def union(x,y):
    x=find_set(x)
    y=find_set(y)
    #같은 집합이면 pass
    if x==y:
        return
    if x<y:
        parents[y]=x
    else:
        parents[x]=y


T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    edges = []
    for _ in range(E):
        n1,n2,w=map(int,input().split())
        edges.append([n1,n2,w])
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)]
    sum_weigh = 0

    # 간선들을 모두 확인한다.
    for s, e, w in edges:
        # 싸이클이 발생하면 pass
        # -> 이미 같은 집합에 속해 있다면 pass (대표자가 같다)
        if find_set(s) == find_set(e):
            continue
        # 싸이클이 없으면 방문 처리
        union(s, e)
        sum_weigh += w

    print(f'#{tc} {sum_weigh}')