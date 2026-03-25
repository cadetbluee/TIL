import sys

sys.stdin=open('1806_input.txt')
N,S=map(int,input().split())
arr=list(map(int,input().split()))
answer=0
if sum(arr)<S:
    answer=0
elif max(arr)>=S:
    answer=1
else:
    INF = 10**9
    answer = INF
    hap=0
    left=0
    for right in range(N):
        hap+=arr[right]
        while hap>=S:
            answer=min(answer,right-left+1)
            hap-=arr[left]
            left+=1
    
        
print(answer)