import sys
sys.stdin=open("4869_input.txt")


# def pactorial(N):
#     if N==1:
#         return 1
#     else:
#         N*pactorial(N-1)


T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    cnt=0
    while N>20:
        N-=20
        cnt+=1
    result=0
    if N==10:
        for n in range(cnt+1):
            N=cnt+n+1
            r=1+2*n
            v=1
            for i in range(1,r+1):
                v*=((N-i+1)/i)

            # result+=(pactorial(cnt-n)/(pactorial(1+2*n)*pactorial(cnt-1-3*n)))*2**(cnt-2*n)
            result+=v*2**(cnt-n)
    else:
        cnt+=1
        for n in range(cnt + 1):
            N = cnt + n
            r = 2 * n
            v = 1
            for i in range(1, r + 1):
                v *= ((N - i + 1) / i)
            # result += (pactorial(cnt - n) / (pactorial(2 * n) * pactorial(cnt- 3 * n))) * 2 ** (cnt - 2 * n)
            result+=v*2**(cnt-n)
    print(f'#{test_case}',int(result))