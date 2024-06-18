import sys
sys.stdin=open("9184_input.txt")
while True:
    A,B,C=map(int,input().split())
    if A==-1 and B==-1 and C==-1:
        break
    dp=[[[0]*21 for _ in range(21)] for _ in range(21)]
    if A>20 or B>20 or C>20:
        A,B,C=20,20,20
    if A<0 or B<0 or C<0:
        print(1)
    else:
        for a in range(A):
            for b in range(B):
                for c in range(C):
                    if a<b and b<c:
                        dp[a][b][c]=dp[a][b][c-1]+dp[a][b-1][c-1]-dp[a][b-1][c]
                    else:
                        dp[a][b][c]=dp[a-1][b][c]+dp[a-1][b-1][c]+dp[a-1][b][c-1]-dp[a-1][b-1][c-1]
        print(dp[a][b][c])