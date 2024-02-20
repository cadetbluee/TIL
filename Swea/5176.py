import sys
sys.stdin = open("5176_input.txt", "r")
import math
i=1
def in_order(T):
    global i
    if T and len(left)>T and len(right)>T:
        in_order(left[T])
        # print(T,end=' ')

        par.append(T)
        in_order(right[T])


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    left=[0]*(N+1)
    right=[0]*(N+1)

    H=math.floor(math.log2(N))
    par = []
    for i in range(1,2**H):
        left[i]=i*2
        right[i]=i*2+1

    result=[0]*(N+1)
    in_order(1)
    j=1
    for i in par:
        result[i]=j
        j+=1

    print(f'#{tc}',result[1],result[N//2])

