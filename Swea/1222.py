import sys
sys.stdin=open("1222_input.txt")

T=10
for tc in range(1,T+1):
    N=int(input())
    N_str=input()
    stack=[]
    sum_N=0
    for i in N_str:
        if i =='+':
            stack.append(i)
        elif len(stack)>0:
            sum_N+=int(i)
            stack.pop()
        else:
            sum_N=int(i)
    print(f'#{tc} {sum_N}')