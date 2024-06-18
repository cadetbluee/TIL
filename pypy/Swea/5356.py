import sys
sys.stdin=open('5356_input.txt')
T=int(input())
for tc in range(1,T+1):
    arr=[input().strip() for _ in range(5)]
    ans=''
    max_len=0
    for i in range(5):
        if len(arr[i])>max_len:
            max_len=len(arr[i])
    for i in range(5):
        while len(arr[i])!=max_len:
            arr[i]+=' '
    for i in range(max_len):
        for j in range(5):
            if arr[j][i]!=' ':
                ans+=arr[j][i]
    print(f'#{tc} {ans}')