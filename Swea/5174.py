import sys
sys.stdin = open("5174_input.txt", "r")


def pre_order(T):
    global cnt
    if T:
        cnt+=1
        pre_order(left_child[T])
        pre_order(right_child[T])



T=int(input())
for tc in range(1,T+1):
    E,N=map(int,input().split())
    arr=list(map(int,input().split()))
    left_child=[0]*(max(arr)+1)
    right_child=[0]*(max(arr)+1)
    # par = [0] * (E + 1)
    cnt=0
    for i in range(E):
        p,c=arr[2*i],arr[2*i+1]
        if left_child[p]==0:
            left_child[p]=c
        else:
            right_child[p]=c

    pre_order(N)
    print(f'#{tc} {cnt}')