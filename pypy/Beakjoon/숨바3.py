import sys
sys.stdin=open('13549_input.txt')
from collections import deque
N,K=map(int,input().split())
MAX = 100001
dist=[MAX]*MAX
dist[N]=0
dq=deque()
dq.append(N)
if N>=K:
    print(N-K)
else:
    
    while dq:
        x=dq.popleft()
        if x==K:
            print(dist[x])
        nx = x * 2
        if 0 <= nx < MAX and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            dq.appendleft(nx)
        nx=x+1
        if 0 <= nx < MAX and dist[nx] > dist[x] + 1:
            dist[nx] = dist[x] + 1
            dq.append(nx)
        nx=x-1
        if 0 <= nx < MAX and dist[nx] > dist[x] + 1:
            dist[nx] = dist[x] + 1
            dq.append(nx)
        
# N에서 2배를 할 수도 있고, 1을 뺄수도 있고 더할 수도 있고