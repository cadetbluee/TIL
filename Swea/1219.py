import sys
sys.stdin=open("1219_input.txt")
T = 10
for test_case in range(1, T + 1):
    T,N=map(int,input().split())
    p_list=list(map(int,input().split()))
    list_1=[0]*100
    list_2=[0]*100
    stack=[]
    result=0
    for i in range(N):
        if list_1[p_list[2*i]]==0:
            list_1[p_list[2*i]]=p_list[2*i+1]
        else:
            list_2[p_list[2 * i]] = p_list[2 * i + 1]
    i=0
    visited1=[0]*100
    visited2=[0]*100

    while True:
        if (list_1[i]!=0 and list_2[i]!=0) and (visited1[i]==0 or visited2[i]==0):
            if visited1[i]==0:
                stack.append(i)
                visited1[i]=1
                i=list_1[i]
            elif visited2[i]==0:
                visited2[i]=1
                i=list_2[i]

        elif list_1[i]!=0:
            i=list_1[i]
        elif list_2[i]!=0:
            i=list_2[i]

        else:
            if len(stack)>0:
                i=stack.pop()
            else:
                break
        if i == 99:
            result = 1
            break

    print(f'#{test_case} {result}')
