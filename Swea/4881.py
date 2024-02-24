import sys
sys.stdin=open("4881_input.txt")


def recur(i,N,s):
    global min_v
    global cnt
    if i==N:
        
        if min_v>s:
            min_v=s
    elif s>=min_v:
        return
    else:
        for a in range(i,N):
            P[i],P[a]=P[a],P[i]
            recur(i+1,N,s+arr[i][P[i]])
            P[i],P[a]=P[a],P[i]


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    P=[i for i in range(N)]
    min_v=100
    cnt=0
    recur(0,N,0)
    print(f'#{tc} {min_v}')
    # sum_min=min(arr[0])
    # pre_min=min(arr[0])
    # pre_next_min=min(arr[1:])
    # pre_index=arr[0].index(sum_min)
    # for i in range(N):
    #     cur_min=min(arr[i])
    #     cur_next_min=min(arr[:i]+arr[i+1:])
    #     cur_index=arr[i].index(cur_min)
    #     if cur_index==pre_index:
    #         if cur_min+pre_next_min==min(cur_min+pre_next_min,cur_next_min+pre_min):
    #             sum_min=sum_min-pre_min+pre_next_min+cur_min
    #             pre_index=cur_index
    #             pre_next_min=cur_next_min
    #             pre_min=cur_min
    #         else:
    #             sum_min+=cur_next_min
    #             pre_index=cur_index
    #         pre_next_min=cur_next_min
    #         pre_min=cur_min
    