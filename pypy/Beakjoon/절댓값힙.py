import sys
import heapq
sys.stdin=open('11286_input.txt')
N=int(input())
heap=[]
heapq.heapify(heap)
for _ in range(N):
    x=int(input())
    if x!=0:
        heapq.heappush(heap,(abs(x),0 if x <0 else 1))
    else:
        if heap:
            s=heapq.heappop(heap)
            if s[1]:
                print(s[0])
            else:
                print(-s[0])
        else:
            print(0)
