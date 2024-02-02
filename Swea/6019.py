import sys
sys.stdin = open("6019_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    D,A,B,F=map(int,input().split())
    result=D/(A+B)*F
    #i=0 #제논의 역설에 걸린다
    # while D>0:
    #     # D=D*(F-A)**i/(F+B)**i
    #     if i%2==1:
    #         result+=((D*(F-A)**i)/(F+B)**i)*(F/(F+A))
    #
    #     else:
    #         result +=((D*(F-A)**i)/(F+B)**i)*(F/(F+B))
    #
    #     D = D * (F - A) ** i / (F + B) ** i
    #     #print(D)
    #     i+=1
    print(f'#{test_case} {result}')