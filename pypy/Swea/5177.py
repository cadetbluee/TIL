import sys
sys.stdin = open("5177_input.txt", "r")


def enq(n):
    global last
    last+=1   #마지막 노드 추가(완전이진트리 유지)
    hap[last]=n #마지막 노드에 데이터 삽입
    c=last    #부모>자식
    p=c//2
    while p>=1 and hap[p]>hap[c]:  #부모가 있는데 더 작으면
        hap[p],hap[c]=hap[c],hap[p]
        c=p
        p=c//2


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    hap = [0] * (N + 1)
    last=0
    for i in arr:
        enq(i)
    an_sum=0
    while N>0:
        an_sum+=hap[N//2]
        N=N//2
    print(f'#{tc}',an_sum)