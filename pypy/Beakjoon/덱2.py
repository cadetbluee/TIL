from collections import deque
from sys import stdin
N=int(input())
Q=deque()
for i in range(N):
    lis=stdin.readline().split()
    if lis[0]=='6':
        if len(Q)>0:
            print(0)
        else:
            print(1)
    elif lis[0]=='1':
        Q.appendleft(lis[1])
    elif lis[0]=='2':
        Q.append(lis[1])
    elif lis[0]=='3':
        if len(Q)>0:
            print(Q.popleft())
        else:
            print(-1)
    elif lis[0]=='4':
        if len(Q)>0:
            print(Q.pop())
        else:
            print(-1)
    elif lis[0]=='5':
        print(len(Q))
    elif lis[0]=='7':
        if len(Q)>0:
            print(Q[0])
        else:
            print(-1)
    elif lis[0]=='8':
        if len(Q)>0:
            print(Q[-1])
        else:
            print(-1)