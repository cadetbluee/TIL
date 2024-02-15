n=input()
result=''
stack=[]
for i in n:
    if i in '+-':
        if len(stack)>0 and stack[-1] in '+-':
            result+=stack.pop()
        elif len(stack)>0 and stack[-1] in '*/':
            while stack[-1] in '*/':
                result+=stack.pop()
            if stack[-1] in '*/':
                result+=stack.pop()
        stack.append(i)
        
    elif i in '*/':
        stack.append(i)
    elif i =='(':
        stack.append(i)
    elif i==')':
        while stack[-1]!='(':
            result+=stack.pop()
        stack.pop()
    else:
        result+=i
while len(stack)>0:
    result+=stack.pop()
print(result)