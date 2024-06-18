import sys
sys.stdin=open("1860_input.txt")
T=int(input())
# from heapq import heapify, heappop
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    N_list=list(map(int,input().split()))
    N_list=sorted(N_list)
    max_time=max(N_list)
    time=0
    boog=0

    result='Possible'
    while time<=max_time:
        if time>0 and time%M==0:
            boog+=K
        while len(N_list)>0 and N_list[0]==time:
            N_list.pop(0)
            if boog>0:
                boog-=1
            else:
                result = 'Impossible'
                break
        time+=1
    print(f'#{tc}',result)