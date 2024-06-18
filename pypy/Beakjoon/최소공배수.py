import sys
sys.stdin=open("1934_input.txt")
T=int(input())
for tc in range(T):
    A,B=map(int,input().split())
    max_re=max(A,B)
    min_re=min(A,B)
    i,j=2,2
    while min_re!=0:
        
        max_re,min_re=min_re,max_re%min_re
        # if A_re>B_re:
        #     B_re=B*j
        #     j+=1
        # elif B_re>A_re:
        #     A_re=A*i
        #     i+=1
    print(int(A*B/max_re))