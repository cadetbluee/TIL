def hap(s):
    global cnt
    if s==N:
        cnt+=1
        return
    elif s>N:
        return
    for j in range(1,4):
        hap(s+j)
T=int(input())
for _ in range(T):
    N=int(input())
    cnt=0
    hap(0)
    print(cnt)