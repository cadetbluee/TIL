import sys
sys.stdin=open('2531_input.txt')
N,d,k,c=map(int,input().split())
sushies=[int(input()) for _ in range(N)]
my_plate=sushies[0:k]
answer=len(set(my_plate))
if c not in my_plate:
    answer+=1
left=1
for right in range(k,N+k):
    if right>=N:
        my_plate=sushies[left:N]+sushies[0:right-N+1]
    else:
        my_plate=sushies[left:right+1]
    temp=len(set(my_plate))
    if c not in my_plate:
        temp+=1
    answer=max(answer,temp)
    
    left+=1
print(answer)