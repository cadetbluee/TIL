import sys
sys.stdin=open("1234_input.txt")
T = 10
for test_case in range(1, T + 1):
    N,s=input().split()
    # s_list=[0]*N
    # for i in range(N-1,-1,-1):
    #     s,res=divmod(s,10)
    #     s_list[i]=res
    N=int(N)
    i=0
    while i<len(s)-1:

        if s[i]==s[i+1]:
            s=s[:i]+s[i+2:]
            i=0
        else:
            i+=1
    print(f'#{test_case} {s}')