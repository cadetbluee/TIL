N=int(input())
N_list=sorted(list(map(int,input().split())))
M=int(input())
M_list=list(map(int,input().split()))
M_list_corr=[0]*M
def binary_search(N_list,key):
    start=0
    end=len(N_list)-1
    while start<=end:
        middle=(start+end)//2
        if N_list[middle]==key:
            return 1
        elif N_list[middle]>key:
            end=middle-1
        else:
            start=middle+1
    return 0
for i in range(M):
    M_list_corr[i]=binary_search(N_list,M_list[i])


print(*M_list_corr)