import sys
sys.stdin=open("12789_input.txt")
N=int(input())
N_list=list(map(int,input().split()))
stack=[]
order=1
result='Nice'
i=0
while i<N:
    if len(stack)>0:
        
        if stack[-1]==order:
            stack.pop()
            order+=1
        elif N_list[i]!=order:
            stack.append(N_list[i])
            i+=1
        else:
            order+=1
            i+=1
    else:
        if N_list[i]!=order:
            stack.append(N_list[i])
            i+=1
            
        else:
            order+=1
            i+=1

while len(stack)>0:
    if stack.pop()== order:
        order+=1
    else:
        result='Sad'

print(result)