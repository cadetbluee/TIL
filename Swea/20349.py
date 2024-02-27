import sys
sys.stdin=open('20349_input.txt')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[i for i in range(1,N+1)]
    over=int(N*0.37)
    perfect=int(N*0.5)
    for _ in range(M):
        arr=arr[N-over:]+arr[:N-over]
        arr2,arr1=arr[N-perfect:],arr[:N-perfect]
        for a in range(N//2):
            arr[2*a]=arr1.pop(0)
            arr[2*a+1]=arr2.pop(0)
        if len(arr1)>0:
            arr[-1]=arr1.pop()

    print(f'#{tc}',*arr)