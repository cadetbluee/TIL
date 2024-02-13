import sys
sys.stdin=open("19966_input.txt")

T=int(input())
for tc in range(1,T+1):
    cal=input()
    stack=[]
    isp=['+-','*/']
    result=''
    for i in cal:
        if i in '+-*/':
            if i in isp[0]:
                if len(stack)>0 and stack[-1] in isp[1]:
                    result+=stack.pop()
                    stack.append(i)
                else:
                    stack.append(i)
            else:
                if len(stack)>0 and stack[-1] in isp[0]:
                    stack.append(i)
                else:
                    stack.append(i)
        else:
            result+=i
            if len(stack)>0 and stack[-1] in isp[1]:
                result+=stack.pop()
    while len(stack)>0:
        result+=stack.pop()
    print(f'#{tc} {result}')