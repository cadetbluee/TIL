import sys
sys.stdin=open("1735_input.txt")
boon1,denom1=map(int,input().split())
boon2,denom2=map(int,input().split())
A=boon1*denom2+boon2*denom1
B=denom1*denom2
max_re=max(A,B)
min_re=min(A,B)
i,j=2,2
while min_re!=0:
    max_re,min_re=min_re,max_re%min_re

print(int(A/max_re),int(B/max_re))