T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    N_arr=input().split()
    M_arr=input().split()
    Q=int(input())
    ans=[]
    for _ in range(Q):
        Y=int(input())
        ans.append(N_arr[Y%N-1]+M_arr[Y%M-1])
    print(f'#{tc}',*ans)