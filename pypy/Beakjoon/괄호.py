import sys
sys.stdin=open("9012_input.txt")
T=int(input())
for _ in range(T):
    string=input()
    stack=[]
    result='YES'
    for s in string:
        if s=='(':
            stack.append(s)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                result='NO'
                break
    if len(stack)>0:
        result='NO'
    print(result)