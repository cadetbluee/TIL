import sys
sys.stdin=open("2005_input.txt")


def paskal(n): #파스칼을 한줄씩 출력
    paskal_string = ''
    if n == 0: #첫번째열은 1만
        paskal_string = '1'
    else:
        for i in range(n+1): #두번째 열부터는 조합을 사용하여 nC0~nCr~nCn까지 문자열로 저장
            val = 1
            for r in range(1,i+1):
                val = val * (n - r+1) / r
            paskal_string += str(int(val)) + " "
    return print(paskal_string)


T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    print(f'#{test_case}')
    for i in range(N):
        paskal(i)