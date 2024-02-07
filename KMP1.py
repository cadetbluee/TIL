def kmp(t,p):
    N=len(t)
    M=len(p)
    lps=[0]*(M+1)
    #preprocessing
    j=0#일치한 개수 ==비교할 패턴 위치
    lps[0]=-1
    for i in range(1,M):
        lps[i]=j
        if p[i]==p[j]:
            j+=1
        else:
            j=0
    lps[M]=j
    