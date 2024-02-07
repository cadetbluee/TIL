import sys
sys.stdin=open("19821_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    S=input()
    result=[]
    ans=-1
    for i in range(len(S)):
        if S[i]=='{'or S[i]=='('or S[i]=='[':
            result.append(S[i])
        elif S[i]=='}'or S[i]==')'or S[i]==']':
            if len(result)==0:
                ans=-1
                break
            else:
                if S[i]== '}' and result.pop()=='{':
                    ans=1
                elif S[i]== ')' and result.pop()=='(':
                    ans=1
                elif S[i] == ']' and result.pop() == '[':
                    ans = 1
                else:
                    ans=-1
                    break
    if len(result)!=0:
        ans=-1
    print(f'#{test_case} {ans}')