import sys
sys.stdin=open('5247_input.txt')
from collections import deque
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    Q=deque()
    Q.append((N,0))
    result=1e9
    visited=set()
    while Q:
        num,d=Q.popleft()

        if num==M:
            result=d
            break
        if num>=1e6 or num in visited:
            continue
        visited.add(num)
        Q.append((num+1,d+1))
        Q.append((num-1,d+1))
        Q.append((num*2,d+1))
        Q.append((num-10,d+1))
    print(f'#{tc}',result)