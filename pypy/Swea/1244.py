import sys
sys.stdin=open('1244_input.txt')


def max_mon(cnt):
    global ans
    if cnt==N:
        if int(''.join(arr))>ans:
            ans=int(''.join(arr))
        return
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            arr[i],arr[j]=arr[j],arr[i]
            if (''.join(arr),cnt+1) not in visit:
                visit.append((''.join(arr),cnt+1))
                max_mon(cnt+1)
            arr[i], arr[j] = arr[j] , arr[i]


T=int(input())
for tc in range(1,T+1):
    s,N=input().split()
    N=int(N)
    arr=list(s)
    # sorted_arr=sorted(arr,reverse=True)
    visit=[]
    # cnt=0
    # while cnt<N:
    #     index = 0
    #     for i in range(len(arr)):
    #         if arr.index(sorted_arr[i])!=index:
    #             compare=[]
    #             for j in range(len(arr)):
    #                 if arr[j]==sorted_arr[i]:
    #                     arr[j],arr[index]=arr[index],arr[j]
    #                     compare.append(arr)
    #                     arr[j], arr[index] = arr[index], arr[j]
    #             arr=max(compare)
    #             cnt+=1
    #             break
    #         else:
    #             index+=1
    ans=0
    max_mon(0)

    print(f'#{tc} {ans}')