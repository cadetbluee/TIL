import sys
sys.stdin = open("5186_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N=float(input())
    code=[]
    i=2
    while len(code)<12:
        code.append(1/i)
        i*=2
    ans=''
    for i in range(12):
        if N==0:
            break
        if N>=code[i]:
            ans+='1'
            N-=code[i]
        else:
            ans+='0'
    if N!=0:
        ans='overflow'
    print(f'#{tc}',ans)