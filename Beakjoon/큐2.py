from collections import deque
from sys import stdin

N=int(input())
Q=deque()
for _ in range(N):
    order=stdin.readline().split()
    if order[0]=='push':
        Q.append(order[1])
    elif order[0]=='pop':
        if len(Q)>0:
            print(Q.popleft())
        else:
            print(-1)
    elif order[0]=='size':
        print(len(Q))
    elif order[0]=='empty':
        if len(Q)>0:
            print(0)
        else:
            print(1)
    elif order[0]=='front':
        if len(Q):
            print(Q[0])
        else:
            print(-1)
    else:
        if len(Q)>0:
            print(Q[-1])
        else:
            print(-1)
    