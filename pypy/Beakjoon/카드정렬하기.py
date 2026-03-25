import heapq
import sys
sys.stdin=open('1715_input.txt')
N = int(input())
heap=[]
answer=0
for _ in range(N):
    heapq.heappush(heap,int(input()))

while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    heapq.heappush(heap,a+b)
    answer+=a+b
print(answer)