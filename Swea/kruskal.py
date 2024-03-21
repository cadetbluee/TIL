import sys
sys.stdin=open('prim_input.txt')
#1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
# -> 코드로 구현 : 전체 간선 정보를 저장 + 가중치로 정렬

#2. 방문 처리
# -> 이때, 사이클이 발생하면 안된다.
# -> 싸이클 여부 ?? ==> union-find 알고리즘이 활용

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

V,E=map(int,input().split())
edges=[] # 간선 정보들을 모두 저장
for _ in range(E):
    s,e,w=map(int,input().split())
    edges.append([s,e,w])
edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 정렬
parents=[i for i in range(V)]
sum_weigh=0
cnt=0
#간선들을 모두 확인한다.
for s,e,w in edges:
    #싸이클이 발생하면 pass
    #-> 이미 같은 집합에 속해 있다면 pass (대표자가 같다)
    if find_set(s)==find_set(e):
        continue
    #싸이클이 없으면 방문 처리
    union(s,e)
    cnt+=1
    sum_weigh+=w
    if cnt==V-1: # MST 완성 > 간선의 개수 : V-1
        break
print(f'The minimum : {sum_weigh}')
