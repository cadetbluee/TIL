import sys
sys.stdin = open("1221_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc,N=input().split()
    N=int(N)
    N_list=list(input().split())
    for i in range(N):
        if N_list[i] == "ZRO":
            N_list[i] = 0
        if N_list[i]=="ONE":
            N_list[i]=1
        if N_list[i]=="TWO":
            N_list[i]=2
        if N_list[i]=="THR":
            N_list[i]=3
        if N_list[i]=="FOR":
            N_list[i]=4
        if N_list[i]=="FIV":
            N_list[i]=5
        if N_list[i]=="SIX":
            N_list[i]=6
        if N_list[i]=="SVN":
            N_list[i]=7
        if N_list[i]=="EGT":
            N_list[i]=8
        if N_list[i]=="NIN":
            N_list[i]=9
    N_list=sorted(N_list)
    for i in range(N):
        if N_list[i] == 0:
            N_list[i] = "ZRO"
        if N_list[i]==1:
            N_list[i]="ONE"
        if N_list[i]==2:
            N_list[i]="TWO"
        if N_list[i]==3:
            N_list[i]="THR"
        if N_list[i]==4:
            N_list[i]="FOR"
        if N_list[i]==5:
            N_list[i]="FIV"
        if N_list[i]==6:
            N_list[i]="SIX"
        if N_list[i]==7:
            N_list[i]="SVN"
        if N_list[i]==8:
            N_list[i]="EGT"
        if N_list[i]==9:
            N_list[i]="NIN"
    print(f'{test_case}')
    print(*N_list)