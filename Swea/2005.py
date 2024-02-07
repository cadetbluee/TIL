import sys
sys.stdin=open("2005_input.txt")

def paskal(n):
    s = ''
    if n == 0:
        s = '1'
    else:
        for i in range(n+1):
            val = 1
            for j in range(1,i+1):
                val = val * (n - j+1) / j
            s += str(int(val)) + " "
    return print(s)
T = int(input())

for test_case in range(1, T + 1):
    N=int(input())
    print(f'#{test_case}')
    for i in range(N):
        paskal(i)
