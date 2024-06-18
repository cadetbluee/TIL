import sys
sys.stdin = open("20281_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=input().strip()
    code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']
    x_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    codebit=['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']
    bi_N = ''
    for i in N:
        bi_N += code[x_code.index(i)]
    for i in range(len(bi_N)-1,-1,-1):
        if bi_N[i]=='1':
            bi_N=bi_N[:i+1]
            break
    ans = []
    while len(bi_N) > 6:
        ans.append(bi_N[len(bi_N)-6:])
        bi_N = bi_N[:len(bi_N)-6]
    print(f'#{tc}',end=' ')
    for i in range(len(ans)-1,-1,-1):
        print(codebit.index(ans[i]),end=' ')
    print()