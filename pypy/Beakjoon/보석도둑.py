import sys
import heapq
sys.stdin=open('1202_input.txt')
N,K=map(int,input().split())
gems=[list(map(int,input().split())) for _ in range(N)]
bags=[int(input()) for _ in range(K)]
bags.sort()
gems.sort(key=lambda x: x[0])
cnt=0
answer=0
heap=[]
for cap in bags:
    while cnt<N and gems[cnt][0]<=cap:
        heapq.heappush(heap,-gems[cnt][1])
        cnt+=1
    if heap:
        answer+=-heapq.heappop(heap)
print(answer)