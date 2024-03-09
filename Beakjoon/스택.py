from sys import stdin
from collections import deque
N=int(input())
stack=deque()
for _ in range(N):
    order=stdin.readline().split()
    if order[0]=='push_front':
        stack.appendleft(order[1])
    elif order[0]=='push_back':
        stack.append(order[1])
    elif order[0]=='pop_front':
        if len(stack)>0:
            print(stack.popleft())
        else:
            print(-1)
    elif order[0]=='pop_back':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif order[0]=='size':
        print(len(stack))
    elif order[0]=='empty':
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif order[0]=='front':
        if len(stack)>0:
            print(stack[0])
        else:
            print(-1)
    else:
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)