N=int(input())
stack=[]
for _ in range(N):
    order,x=input().split()
    if order=='push':
        stack.append(x)
    elif order=='pop':
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif order=='size':
        print(len(stack))
    elif order=='empty':
        if len(stack)>0:
            print(0)
        else:
            print(1)
    else:
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)