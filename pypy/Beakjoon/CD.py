import sys
sys.stdin=open('4158_input.txt')
from sys import stdin
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break
    # N_list=[]
    # M_list=[]
    # for i in range(N):
    #     N_list.append(int(input()))
    # for i in range(M):
    #     M_list.append(int(input()))
    # def binary_search(arr,key):
    #     start=0
    #     end=len(arr)-1
    #     while start<=end:
    #         middle=(start+end)//2
    #         if arr[middle]==key:
    #             return 1
    #         elif arr[middle]>key:
    #             end=middle-1
    #         else:
    #             start=middle+1
    #     return 0
    # result=0
    # if len(N_list)<len(M_list):
    #     for i in range(N):
    #         result+=binary_search(M_list,N_list[i])
    # else:
    #     for i in range(M):
    #         result+=binary_search(N_list,M_list[i])
    # print(result)
    N_set=set()
    M_set=set()
    NM_set=set()
    for i in range(N):
        a=stdin.readline().strip()
        N_set.add(a)
        NM_set.add(a)
    for i in range(M):
        a=stdin.readline().strip()
        M_set.add(a)
        NM_set.add(a)
        
    print(len(M_set)+len(N_set)-len(NM_set))