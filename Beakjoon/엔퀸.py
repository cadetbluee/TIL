def recur8(i,N):
    global cnt
    if i==N:
        # num=0
        # for i in range(N):
        #     num+=A[i]*10**(N-i-1) #각 자리수마다 10*k을 곱해서 더하기
        # print(num)
        cnt+=1
        return
    for k in range(N):
        if visit[k]==False:
            A[i]=k
            if check(i):
                visit[k]=True
                recur8(i+1,N)
                visit[k]=False

def check(i):
    for j in range(i):
        if A[i]==A[j] or (i-j) == abs(A[i]-A[j]):
            return False
    else:    
        return True
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    A=[0]*N #[1,1,1],[1,1,2]...
    visit=[False]*N
    cnt=0
    recur8(0,N)
    print(f'{tc} {cnt}')