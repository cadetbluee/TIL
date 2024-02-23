import sys
sys.stdin = open("20279_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=input().strip()
    code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']
    x_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    bi_N=''
    for i in N:
        bi_N+=code[x_code.index(i)]
    ans=[]
    while len(bi_N)>7:
        ans.append(bi_N[:7])
        bi_N=bi_N[7:]
    ans.append(bi_N)
    print(f'#{tc}',end=' ')
    for i in ans:
        print(int('0b'+i,2),end=' ')
    print()