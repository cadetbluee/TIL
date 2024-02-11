import sys
sys.stdin=open("4949_input.txt")

while True:
    string=input()
    stack=[]
    result='yes'
    if len(string)==1:
        break
    for s in string:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')':
            if len(stack)>0:
                if stack.pop()!='(':
                    result='no'
                    break
            else:
                result='no'
                break
        elif s==']':
            if len(stack)>0:
                if stack.pop()!='[':
                    result='no'
                    break
            else:
                result='no'
                break
    if len(stack)>0:
        result='no'
    print(result)