import sys
sys.stdin=open("4866_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    S=input()
    result=[]
    ans=0
    for i in range(len(S)):
        if S[i]=='{'or S[i]=='('or S[i]=='[':
            result.append(S[i])
        elif S[i]=='}'or S[i]==')'or S[i]==']':
            if len(result)==0:
                ans=0
                break
            else:
                if S[i]== '}' and result.pop()=='{':
                    ans=1
                elif S[i]== ')' and result.pop()=='(':
                    ans=1
                elif S[i] == ']' and result.pop() == '[':
                    ans = 1
                else:
                    ans=0
                    break
    if len(result)!=0:
        ans=0
    print(f'#{test_case} {ans}')