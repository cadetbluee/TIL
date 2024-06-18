import sys
sys.stdin=open("4408_input.txt")
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    cnt=[0]*201
    for _ in range(N):
        cur,dep=map(int,input().split())
        
        for i in range((min(cur,dep)+1)//2,(max(cur,dep)+1)//2+1):
            cnt[i]+=1
    print(f'#{tc}',max(cnt))