N=int(input())
qs=list(map(int,input().split()))
in_s=list(map(int,input().split()))
M=int(input())
input_s=list(map(int,input().split()))
q=[]
for i in range(N-1,-1,-1):
    if not qs[i]:
        q.append(in_s[i])
if M>len(q):
    print(*q,*input_s[:M-len(q)])
else:
    for i in range(M):
        print(q[i],end=' ')