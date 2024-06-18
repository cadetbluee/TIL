def pre_order(T):
    if T != '.':
        print(T,end='')
        pre_order(tree[T][0])
        pre_order(tree[T][1])

def in_order(T):
    if T != '.':
        in_order(tree[T][0])
        print(T,end='')
        in_order(tree[T][1])

def post_order(T):
    if T != '.':
        post_order(tree[T][0])
        post_order(tree[T][1])
        print(T,end='')

N=int(input())
list_upper = [chr(i) for i in range(65, 91)]
tree={list_upper[i]: [[],[]] for i in range(N)}
left=[0]*(N+1)
right=[0]*(N+1)
for i in range(1,1+N):
    node,leftn,rightn=input().split()

    tree[node][0]=leftn
    tree[node][1]=rightn

pre_order('A')
print()
in_order('A')
print()
post_order('A')
