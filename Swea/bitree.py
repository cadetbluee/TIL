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


def solution(numbers):
    answer = []
    for i in numbers:
        ans = 1
        bi_i = bin(i)[2:]
        if bi_i=='0':
            ans=0
        H = math.floor(math.log2(len(bi_i)))
        while len(bi_i) < (2 ** (H + 1) - 1):
            bi_i = '0' + bi_i
        print(bi_i)

        for h in range(1, H + 1):
            lis = []
            for k in range(1, len(bi_i), 2):
                if (k + 1) % 2 ** h == 0:
                    lis.append(k)

            for j in lis:
                if (bi_i[j - 2 ** (h - 1)] == '1' or bi_i[j + 2 ** (h - 1)] == '1') and bi_i[j] == '0':
                    print(j,h)
                    ans = 0
                    break
        if ans == 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer


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
