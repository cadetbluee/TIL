
N,K=map(int,input().split())
Q=[i for i in range(1,N+1)]
print('<',end='')
while len(Q)>1:
    
    for _ in range(K-1):
        a=Q.pop(0)
        Q.append(a)
    print(Q.pop(0),end=', ')
    
print(Q.pop(),'>')