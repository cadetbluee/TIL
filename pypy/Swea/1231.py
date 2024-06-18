import sys
sys.stdin = open("1231_input.txt", "r")
T=10


def in_order(T):
    if T:
        in_order(left[T])
        print(par[T],end='')
        in_order(right[T])



for tc in range(1,T+1):
    # N=int(input())

    # tree=[0]*(N+1)
    # tree_node=[[] for _ in range(N+1)]
    # for _ in range(N):
    #     lis=input().split()
    #     tree[int(lis[0])]=lis[1]
    #     for i in range(2,len(lis)):
    #         tree_node[int(lis[0])].append(int(lis[i]))
    # visited=[0]*(N+1)
    # for i in range(1,N+1):
    #     if len(tree_node[i])>0:
    #         visited[i]=1
    #     else:


    # print(tree,tree_node)
    # print(f'#{tc}')

    N = int(input())
    E = N - 1  # 간선의 수는 하나 작다

    left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식 번호 저장
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    for i in range(N):

        arr=input().split()
        p, c = int(arr[0]), arr[1]
        if len(arr)>2:
            left[p] = int(arr[2])
        if len(arr)>3:
            right[p] = int(arr[3])
        par[p] = c
    # c = N
    # while par[c] != 0:
    #     c = par[c]  # 부모를 새로운 자식으로 두고
    root = 1
    print(f'#{tc}',end=' ')
    in_order(root)
    print()