from collections import deque
N=int(input())
Q=deque()
for i in range(1,N+1):
    Q.append(i)
i=1
while len(Q)>1:
    if i%2==0:
        a=Q.popleft()
        Q.append(a)
    else:
        Q.popleft()
    i+=1
print(*Q)
