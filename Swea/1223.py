import sys
sys.stdin=open("1223_input.txt")
T=10
for tc in range(1,T+1):
    N=int(input())
    string=input()
    stack=[]
    back=''
    for i in string:
        if i =='+':
            if len(stack)>0:
                for _ in range(len(stack)):
                    back+=stack.pop()
            stack.append(i)
        elif i=='*':
            stack.append(i)
        else:
            back+=i
    for _ in range(len(stack)):
        back+=stack.pop()
    result=0
    for i in back:
        if i.isnumeric()==True:
            stack.append(i)
        elif i=='+' :
            b=stack.pop()
            a=stack.pop()
            stack.append(int(a)+int(b))
        elif i=='*' :
            b=stack.pop()
            a=stack.pop()
            stack.append(int(a)*int(b))
        
    print(f'#{tc} {stack[-1]}')