import sys
sys.stdin = open("4839_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    P,Pa,Pb=map(int,input().split())
    def egin(P,P_choice):
        start=1
        end=P
        cnt=0
        while start<=end:
            cnt+=1
            middle=(start+end)//2
            if middle==P_choice:
                return cnt
            elif middle>P_choice:
                end=middle
            else:
                start=middle

    if egin(P,Pa)<egin(P,Pb):
        print(f'#{test_case} A')
    elif egin(P,Pa)>egin(P,Pb):
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')