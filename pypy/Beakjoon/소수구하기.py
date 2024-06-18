import sys
sys.stdin=open("1929_input.txt")
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
#M,N=map(int,input().split())
N=int(input())
cnt=0
arr=list(map(int,input().split()))
for i in range(N):
    if is_prime(arr[i]):
        cnt+=1
print(cnt)
# i=0
# while M+i<=N:
#     if is_prime(i+M)==True:
#         print(i+M)
#     i+=1S
N=int(input())
arr=[]
for i in range(N):
    if is_prime(i):
        arr.append(i)
sum_prime=0
cnt=0
for start in range(0,N-1):
    end=1
    s=sum(arr[start:end])
    while end!=N:
        
        if s+arr[end]==N:
            cnt+=1
        end+=1
    
print(cnt)