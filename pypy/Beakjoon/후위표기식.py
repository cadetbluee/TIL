
# top=-1

# icp={'(':3,'*':2,'/':2,'+':1,'-':1}
# isp={'(':0,'*':2,'/':2,'+':1,'-':1}
# n=input()
# result=''
# stack=[0]*(len(n))
# for tk in n: #여는 괄호면 push, 연산자의 경우 top 원소보다 우선순위가 높으면 push
#     if tk =='(' :
#         top+=1
#         stack[top]=tk
#     elif tk==')':
#         while stack[top]!='(':
#             top-=1
#             result+=stack[top+1]
#         top-=1
#     elif tk not in '+-*/':
#         result+=tk
#     else:
#         if stack[top]!=0 and isp[stack[top]]>=icp[tk]:
#             while isp[stack[top]]>=icp[tk]:
#                 top-=1
#                 result+=stack[top+1]
#         top+=1
#         stack[top]=tk
#     # elif tk in '*/+-' and isp[stack[top]]<icp[tk]:
#     #     top+=1
#     #     stack[top]=tk
#     # elif tk in '*/+-' and isp[stack[top]]>=icp[tk]:
#     #     while isp[stack[top]]>=icp[tk]:
#     #         top-=1
#     #         result+=stack[top+1]
#     #     top+=1
#     #     stack[top]=tk
#     # elif tk==')': #닫는 괄호, 여는 괄호를 만날때까지 pop
#     #     while stack[top]!='(':
#     #         top-=1
#     #         result+=stack[top+1]
#     #     top-=1
#     #     stack[top+1]
#     # else:
#     #     result+=tk
# if top!=-1:
#     while top!=-1:
#         top-=1
#         result+=stack[top+1]
# print(result)
icp={'(':3,'*':2,'/':2,'+':1,'-':1}
isp={'(':0,'*':2,'/':2,'+':1,'-':1}
n=input()
result=''
stack=[]
for tk in n:
    if tk =='(':
        stack.append(tk)
    elif tk in '*/+-':
        while stack and stack[-1] != '(' and isp.get(stack[-1], 0) >= icp[tk]:
            result += stack.pop()
        stack.append(tk)
    elif tk == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()  # pop '('
    else:
        result += tk

while stack:
    result += stack.pop()

print(result)
