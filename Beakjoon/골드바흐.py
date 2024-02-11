import sys
sys.stdin=open("17103_input.txt")
def is_prime(N):
    prime=[True]*(N+1)
    for n in range(N+1):
        if n <= 1:
            prime[n]=False
        elif n <= 3:
            prime[n]=True
        elif n % 2 == 0 or n % 3 == 0:
            prime[n]=False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                prime[n]=False
            i += 6
    return prime
T=int(input())
for _ in range(T):
    n=int(input())
    i=1
    cnt=0
    prime_list=is_prime(n)
    while i<=n//2:
        if prime_list[i] and prime_list[n-i]:
            cnt+=1
        i+=1
    print(cnt)