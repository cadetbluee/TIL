import sys
sys.stdin=open("14425_input.txt","r")
N,M=map(int,input().split())
S=[input() for _ in range(N)]
str_check=[input() for _ in range(M)]
cnt=0
for i in str_check:
    if i in S:
        cnt+=1
print(cnt)