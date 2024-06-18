import sys
S=input()
N=int(input())
for _ in range(N):
    a,start,end=sys.stdin.readline().split()
    cnt=0
    for s in range(int(start),int(end)+1):
        if S[s]==a:
            cnt+=1
    sys.stdout.write(str(cnt))