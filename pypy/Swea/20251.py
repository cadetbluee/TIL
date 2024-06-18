import sys
sys.stdin = open("20251_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[input().strip() for _ in range(N)]
    lst=''
    for i in range(N):
        lst+=arr[i]
    answer=[]
    for i in range(1,11):
        answer.append(int('0b'+lst[N*(i-1):N*i],2))
    print(f'#{tc}',*answer)