N=int(input())
arr=list(map(int,input().split()))
B,C=map(int,input().split())
#총감독관의 수 : N
result=0
for a in arr:
    cnt=0
    if a>B:
        rest=a-B
        if rest//C==0:
            cnt=1+(rest//C)
        else:
            cnt=1+(rest//C)+1
    else:
        cnt=1
    result+=cnt
print(result)