import sys
sys.stdin = open("5185_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N,N16=input().split()
    N=int(N)
    code=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    x_code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ans=''
    for i in range(N):
        ans+=code[x_code.index(N16[i])]
    print(f'#{tc}',ans)