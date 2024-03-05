def pre_order(T):
    if T!=0:
        print(T,end='')
        pre_order(left[tree.index(T)])
        pre_order(right[tree.index(T)])

def in_order(T):
    if T!=0:
        pre_order(left[tree.index(T)])
        print(T,end='')
        pre_order(right[tree.index(T)])

def post_order(T):
    if T!=0:
        pre_order(left[tree.index(T)])
        pre_order(right[tree.index(T)])
        print(T,end='')

N=int(input())
tree=[0]*(N+1)
left=[0]*(N+1)
right=[0]*(N+1)
for i in range(1,1+N):
    node,leftn,rightn=input().split()
    tree[i]=node
    if leftn!='.':
        left[i]=leftn
    if rightn!='.':
        right[i]=rightn

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()