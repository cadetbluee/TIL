import sys
sys.stdin = open('7465_input.txt', 'r')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    groups=[0]*(N+1)
    town=[]
    group_num=1
    for _ in range(M):
        a,b=map(int,input().split())
        if a>b:
            a,b=b,a
        town.append((a,b))
    town.sort()
    for a,b in town:
        if not groups[a] and not groups[b]:
            groups[a]=group_num
            groups[b]=group_num
            group_num+=1
        elif groups[a] and not groups[b]:
            groups[b]=groups[a]
        elif groups[b] and not groups[a]:
            groups[a]=groups[b]
    print(f'#{tc}',group_num-1)