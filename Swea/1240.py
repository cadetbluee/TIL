import sys
sys.stdin = open("1240_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[input().strip() for _ in range(N)]
    code=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
    arr_code=''
    for i in range(N):
        if '1' in arr[i]:
            for j in range(M-1,-1,-1):
                if arr[i][j]=='1':
                    a=j-55
                    b=j+1
                    arr_code=arr[i][a:b]
                    break
            if len(arr_code)>0:
                break
    answer=[]
    for i in range(1,9):
        answer.append(code.index(arr_code[7*(i-1):7*i]))
    even=0
    odd=0
    for j in range(1,9):
        if j%2==0:
            even+=answer[j-1]
        else:
            odd+=answer[j-1]

    if (odd*3+even)%10==0:
        print(f'#{tc}', odd+even)
    else:
        print(f'#{tc}',0)