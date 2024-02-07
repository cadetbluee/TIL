def f(pat,txt,M,N):
    for i in range(N-M+1): #text에서 비교시작 위치
        for j in range(M):
            if txt[i+j] != pat[j]:
                break
        else:
            return 1
    #모든 위치에서 비교가 끝난경우
    return 0
T=int(input())
for tc in range(1,T+1):
    pat=input()
    txt=input()
    M=len(pat)
    N=len(txt)
    
    ans = f(pat,txt,M,N)
    print(f'#{tc} {ans}')