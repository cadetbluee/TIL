import sys
sys.stdin=open('7490_input.txt')

T=int(input())
options=[' ','+','-']
def decode(str):
    codes=str.replace(' ','')
    num=''
    c_list=[]
    
    for code in codes:
        if code in ['+','-']:
            c_list.append(num)
            c_list.append(code)
            num=''
        else:
            num+=code
    c_list.append(num)
    answer=0
    s='+'
    for i in range(len(c_list)):
        if i%2==0:
            answer= answer+int(c_list[i]) if s=='+'  else answer-int(c_list[i])
        else:
            s=c_list[i]
    return answer
        
def recur(num,expr):

    if num==N:
        ans=decode(expr)
        if ans==0:
            print(expr)
        return
    for option in options:
        recur(num+1,expr+option+str(num+1))
    
for _ in range(T):
    N=int(input())
    recur(1,'1')
    print()
    
        