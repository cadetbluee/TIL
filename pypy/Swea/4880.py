import sys
sys.stdin=open("4880_input.txt")


def recur(start,end,arr):
    
    if end-start==1:
        
        a=start
        b=end
        if arr[a-1]==arr[b-1]:
            return a
        elif (arr[a-1]==1 and arr[b-1]==3) or(arr[a-1]==2 and arr[b-1]==1) or (arr[a-1]==3 and arr[b-1]==2):
            return a
        else:
            return b
    elif end==start:
        return end
    else:
        # print(arr[i:(i+N)//2+1],arr[(i+N)//2+1:N+1])
        a=recur(start,(start+end)//2,arr)
        b=recur((start+end)//2+1,end,arr)
        if arr[a-1]==arr[b-1]:
            return a
        elif (arr[a-1]==1 and arr[b-1]==3) or(arr[a-1]==2 and arr[b-1]==1) or (arr[a-1]==3 and arr[b-1]==2):
            return a
        else:
            return b
            


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    stack=[]
    recur(0,N-1,arr)
    print(f'#{tc}',recur(1,N,arr))
    