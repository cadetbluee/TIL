import sys
sys.stdin = open("5178_input.txt", "r")
import math
T=int(input())
for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    left=[0]*(N+1)
    right=[0]*(N+1)
    for _ in range(M):
        leef_num,num=map(int, input().split())
        tree[leef_num]=num
        if leef_num%2==0:
            left[leef_num//2]=leef_num
        else:
            right[leef_num//2]=leef_num
    H = math.floor(math.log2(N))
    for i in range(1,2**(H-1)):
        left[i]=2*i
        right[i]=2*i+1

    for i in range(N, -1, -1):
        if left[i] and right[i]:
            tree[i]=tree[left[i]]+tree[right[i]]
        elif left[i]:
            tree[i]=tree[left[i]]
        elif right[i]:
            tree[i]=tree[right[i]]

    print(f'#{tc}',tree[L])