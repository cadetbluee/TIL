import sys
sys.stdin=open("2485_input.txt")
import math

N=int(input())
cnt=0
GCD=[]

tree_list=[]
for i in range(N):
    tree=int(input())
    tree_list.append(tree)
    if i>0:
        cha=tree-pre_tree
        GCD.append(cha)
    pre_tree=tree
min_GCD=GCD[0]
for i in range(len(GCD)):
    min_GCD=math.gcd(min_GCD,GCD[i])
print(int(math.ceil((tree_list[-1]-tree_list[0])/min_GCD+1-N)))
