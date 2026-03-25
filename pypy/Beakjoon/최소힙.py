import sys
import heapq
sys.stdin=open('1927_input.txt')

# heap=[]
# heapq.heapify(heap)
# N=int(input())
# for _ in range(N):
#     x=int(input())
#     if isinstance(x, int) and x > 0:
#         heapq.heappush(heap,x)
#     elif x==0:
#         if heap:
#             s=heapq.heappop(heap)
#         else:
#             s=0
#         print(s)
        
from collections import deque   
N,K=map(int,input().split())

if N >= K:
    print(N-K)
else:
    visited = [False]*100001
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        x, time = queue.popleft()

        if x == K:
            print(time)
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time+1))
