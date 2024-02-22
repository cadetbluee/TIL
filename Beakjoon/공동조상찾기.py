T=int(input())
for _ in range(T):
    N=int(input())
    tree=[[] for _ in range(N+1)]

    for i in range(N):
        p,c=map(int,input().split())
        tree[p].append(c)
    node1,node2=map(int,input().split())
    