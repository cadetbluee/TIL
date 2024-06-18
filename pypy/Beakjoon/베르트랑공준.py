import sys
sys.stdin=open("4948_input.txt")
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
while True:
    n=int(input())
    if n==0:
        break
    i=n+1
    cnt=0
    while i<=2*n:
        if is_prime(i)==True:
            cnt+=1
        i+=1
    print(cnt)