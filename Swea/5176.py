import sys
sys.stdin = open("5176_input.txt", "r")
# import math
# i=1
# def in_order(T):
#     global i
#     if T and len(left)>T and len(right)>T:
#         in_order(left[T])
#         # print(T,end=' ')
#
#         par.append(T)
#         in_order(right[T])
#
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     left=[0]*(N+1)
#     right=[0]*(N+1)
#
#     H=math.floor(math.log2(N))
#     par = []
#     for i in range(1,2**H):
#         left[i]=i*2
#         right[i]=i*2+1
#
#     result=[0]*(N+1)
#     in_order(1)
#     j=1
#     for i in par:
#         result[i]=j
#         j+=1
#
#     print(f'#{tc}',result[1],result[N//2])

def making_tree(x):
    global count
    if x <= N:  # 현재 노드는 범위 내에 있어야 함
        making_tree(x * 2)  # 왼쪽 자식 노드
        tree[x] = count  # 현재 노드에 값을 할당, count 1증가
        count += 1
        making_tree(x * 2 + 1)  # 오른쪽 자식 노드


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 이진 트리의 노드 수
    tree = [0 for _ in range(N + 1)]  # 각 노드의 값을 저장할 배열 초기화
    count = 1  # 노드에 할당할 값
    making_tree(1)  # 함수를 root node(1)로 호출하여 배열 채우기

    print(f'#{tc} {tree[1]} {tree[N // 2]}')