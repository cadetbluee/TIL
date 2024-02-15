import sys
sys.stdin=open("5097_input.txt")
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    n_list=list(map(int,input().split()))
    print(f'#{tc}',n_list[M%N])