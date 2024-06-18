import sys
sys.stdin=open("28278_input.txt")
from sys import stdin
N=int(stdin.readline().strip())
stack=[]
for _ in range(N):
    order=sys.stdin.readline().strip().split()

    if int(order[0])==1:
        stack.append(int(order[1]))
    elif int(order[0])==2:
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif int(order[0])==3:
        print(len(stack))
    elif int(order[0])==4:
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif int(order[0])==5:
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)