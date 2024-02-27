def recur(i,N,K):
    if i==N:
        print(A)
        return
    for j in range(1,K+1):  # for 문안의 문자는 branch, N은 level 이 된다
        A[i]=j
        recur(i+1,N,K)
def recur1(i):
    if i==3:
        return
    for j in range(2):
        recur1(i+1)

N=4
A=[0]*N
K=3
recur(0,N,K)