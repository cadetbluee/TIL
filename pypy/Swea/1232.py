import sys
sys.stdin = open("1232_input.txt", "r")
import math



T=10
for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    left=[0]*(N+1)
    right=[0]*(N+1)
    for _ in range(N):
        arr=input().split()
        idx=int(arr[0])
        tree[idx]=arr[1]
        if len(arr)>2:
            left[idx]=int(arr[2])
            if len(arr)>3:
                right[idx] = int(arr[3])
    cal=[]

    stack=[]
    for i in range(N,-1,-1):
        if left[i] and right[i]:
            if tree[i] in '*/+-':
                if tree[i]=='+':
                    tree[i]=float(tree[left[i]])+float(tree[right[i]])
                elif tree[i] == '-':
                    tree[i] = float(tree[left[i]])-float(tree[right[i]])
                elif tree[i] == '/':
                    tree[i] = float(tree[left[i]])/float(tree[right[i]])
                elif tree[i] == '*':
                    tree[i] = float(tree[left[i]])*float(tree[right[i]])
    # for i in cal:
    #     if i.isnumeric()==True:
    #         stack.append(int(i))
    #     # elif i in '+/*-' and len(stack)==2:
    print(f'#{tc}',math.floor(tree[1]))
