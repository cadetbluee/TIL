import sys
sys.stdin=open('10580_input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    AB=[]
    for _ in range(N):
        A,B=map(int,input().split())
        AB.append((A,B))
    cnt=0
    for A,B in AB:
        for a,b in AB:
            if A>a and b>B:
                cnt+=1
    print(f'#{tc} {cnt}')
