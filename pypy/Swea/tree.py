import sys
sys.stdin = open("tree_input.txt", "r")


def pre_order(T):
    if T:
        print(T,end=' ')
        pre_order(left[T])
        pre_order(right[T])


N=int(input())
E=N-1 #간선의 수는 하나 작다
arr=list(map(int,input().split()))
left=[0]*(N+1) #부모를 인덱스로 왼쪽자식 번호 저장
right =[0]*(N+1)
par=[0]*(N+1)
for i in range(E):
    p,c=arr[i*2],arr[i*2+1]
    if left[p]==0:
        left[p]=c
    else:
        right[p]=c
    par[c]=p
c=N
while par[c]!=0:
    c=par[c] #부모를 새로운 자식으로 두고
root=c
pre_order(root)