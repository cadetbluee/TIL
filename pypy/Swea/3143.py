import sys
sys.stdin=open("3143_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    A,B=input().split()
    cnt=0
    i=0
    while i<len(A):
        if A[i:i+len(B)]==B:
            A=A[:i]+A[i+len(B):]
            cnt+=1
        else:
            i+=1

    print(f'#{test_case} {cnt+len(A)}')
