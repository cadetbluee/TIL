import sys
sys.stdin = open("10804_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=input()
    result=''
    for n in N[::-1]:
        if n=='p':
            result+='q'
        elif n=='b':
            result+='d'
        elif n == 'd':
            result += 'b'
        elif n == 'q':
            result += 'p'
    print(f'#{test_case} {result}')