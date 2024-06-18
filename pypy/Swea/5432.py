import sys
sys.stdin=open("5432_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    N=input()
    stack=[]
    cnt=0
    for i in range(len(N)):
        if N[i]=='(' and N[i+1]==')':
            if len(stack)>0:
                cnt+=len(stack)
        elif N[i]=='(':
            stack.append(i)
        elif N[i-1]==')':
            stack.pop()
            cnt+=1
    print(f'#{test_case} {cnt}')