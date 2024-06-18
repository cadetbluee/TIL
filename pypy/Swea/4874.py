import sys
sys.stdin=open("4874_input.txt")

T=int(input())
for tc in range(1,T+1):
    forth=input().split()
    stack=[]
    forth.pop()
    for i in forth:
        if i.isnumeric()==True:
            stack.append(int(i))
        elif i=='+':
            if len(stack)>1:
                b=stack.pop()
                a=stack.pop()

                stack.append(int(a)+int(b))
            else:
                stack.append('error')
                break
        elif i=='-':
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()

                stack.append(int(a) - int(b))
            else:
                stack.append('error')
                break
        elif i=='/':
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()

                stack.append(int(a/b))
            else:
                stack.append('error')
                break
        elif i=='*':
            if len(stack) > 1:
                b = stack.pop()
                a = stack.pop()

                stack.append(int(a) * int(b))
            else:
                stack.append('error')
                break

    if len(stack)!=1:
        stack.append('error')
    print(f'#{tc} {stack[-1]}')