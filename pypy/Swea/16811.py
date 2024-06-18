import sys
sys.stdin=open('16811_input.txt')
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    C=list(map(int,input().split()))
    C.sort()
    min_cnt=len(C)
    bol=True
    for i in range(1,N):
        for j in range(1,N-i):
            package = [[] for _ in range(3)]
            package[0].extend(C[:i])
            package[1].extend(C[i:N-j])
            package[2].extend(C[N-j:])
            for i in range(3):
                if len(package[i])>N//2 or len(package[i])==0:
                    break
                elif i ==0:
                    for j in package[0]:
                        if j in package[1] or j in package[2]:
                            bol=False
                            break
                elif i ==1:
                    for j in package[1]:
                        if j in package[0] or j in package[2]:
                            bol=False
                            break
                elif i ==2:
                    for j in package[2]:
                        if j in package[1] or j in package[0]:
                            bol=False
                            break
                if not bol:
                    break
            else:
                a=max(abs(len(package[0])-len(package[1])),abs(len(package[1])-len(package[2])),abs(len(package[2])-len(package[0])))
                if a<min_cnt:
                    min_cnt=a
    if min_cnt!=len(C):
        print(f'#{tc}',min_cnt)
    else:
        print(f'#{tc}',-1)