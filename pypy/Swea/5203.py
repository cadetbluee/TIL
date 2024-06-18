import sys
sys.stdin=open('5203_input.txt')


def baby_gin(count):
    for i in range(10):
        if count[i]>=3:
            return 1
        elif i<8 and count[i]!=0 and count[i+1]!=0 and count[i+2]!=0:
            return 1
    return 0


T=int(input())

for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    player1=[0]*10
    player2=[0]*10
    result = 0
    player1[arr[0]]+=1
    player2[arr[1]] += 1
    player1[arr[2]] += 1
    player2[arr[3]] += 1
    for i in range(2,len(arr)//2):
        player1[arr[2*i]]+=1
        player2[arr[2*i+1]]+=1

        if baby_gin(player1):
            result=1
            break
        if baby_gin(player2):
            result = 2
            break

    print(f'#{tc} {result}')