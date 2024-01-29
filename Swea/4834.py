import sys
sys.stdin = open("4834_input.txt", "r")

T = int(input())
print(T)
for test_case in range(1, T + 1):
    N = int(input())
    aq = int(input())
    number= []
    for i in range(N):
        number.append(aq%10)
        aq=aq//10

    print(number)