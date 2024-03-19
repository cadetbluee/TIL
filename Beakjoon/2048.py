import sys
import pprint
sys.stdin=open('12100_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(s, lst=[]):
    global ans
    if s == 5:
        ans = max(ans, play(lst))
        return
    for i in range(4):
        dfs(s+1, lst+[i])
    
def play(nums):
    copy_arr = [i[::] for i in arr]
    
    for num in nums:
        if num == 0:
            u(copy_arr)
        elif num == 1:
            d(copy_arr)
        elif num == 2:
            l(copy_arr)
        else:
            r(copy_arr)
    
    x = 0
    for i in copy_arr:
        x = max(x, max(i))
    
    return x

def u(copy_arr):
    for j in range(N):
        for i in range(N-1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(i+1, N):
                if copy_arr[k][j] != 0:
                    if copy_arr[i][j] == copy_arr[k][j]:
                        copy_arr[i][j] *= 2
                        copy_arr[k][j] = 0
                        break
    
    for j in range(N):
        for i in range(N):
            if copy_arr[i][j] != 0:
                for k in range(i):
                    if copy_arr[k][j] == 0:
                        copy_arr[k][j] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                    break
                
def d(copy_arr):
    for j in range(N):
        for i in range(N-1, 0, -1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(i-1, -1, -1):
                if copy_arr[k][j] != 0:
                    if copy_arr[i][j] == copy_arr[k][j]:
                        copy_arr[i][j] *= 2
                        copy_arr[k][j] = 0
                    break
    
    for j in range(N):
        for i in range(N-1, -1, -1):
            if copy_arr[i][j] != 0:
                for k in range(N-1, i, -1):
                    if copy_arr[k][j] == 0:
                        copy_arr[k][j] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break

def l(copy_arr):
    for i in range(N):
        for j in range(N-1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(j+1, N):
                if copy_arr[i][k] != 0:
                    if copy_arr[i][j] == copy_arr[i][k]:
                        copy_arr[i][j] *= 2
                        copy_arr[i][k] = 0
                    break
    
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] != 0:
                for k in range(j):
                    if copy_arr[i][k] == 0:
                        copy_arr[i][k] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break
                    
def r(copy_arr):
    for i in range(N):
        for j in range(N-1, 0, -1):
            if copy_arr[i][j] == 0:
                continue
                
            for k in range(j-1, -1, -1):
                if copy_arr[i][k] != 0:
                    if copy_arr[i][j] == copy_arr[i][k]:
                        copy_arr[i][j] *= 2
                        copy_arr[i][k] = 0
                    break
    
    for i in range(N):
        for j in range(N-1, -1, -1):
            if copy_arr[i][j] != 0:
                for k in range(N-1, j, -1):
                    if copy_arr[i][k] == 0:
                        copy_arr[i][k] = copy_arr[i][j]
                        copy_arr[i][j] = 0
                        break

ans = 0
dfs(0)
print(ans)



# import sys
# import pprint
# sys.stdin=open('12100_input.txt')
# from copy import deepcopy
# def one(arr):
#     for i in range(N):
#         stack=[]
#         cnt=0
#         for j in range(N):
#             if len(stack)!=0 and stack[-1]==arr[i][j] and cnt==0:
#                 stack.append(stack.pop()*2)
#                 cnt=1
#             elif len(stack)!=0 and arr[i][j]!=0:
#                 stack.append(arr[i][j])
#                 cnt=0
#             elif arr[i][j]!=0:
#                 stack.append(arr[i][j])
#         arr[i]=stack+[0]*(N-len(stack))
#     return arr
# def three(arr):
#     new=[0]*N
#     for i in range(N):
#         stack=[]
#         cnt=0
#         for j in range(N):
#             if len(stack)!=0 and stack[-1]==arr[j][i] and cnt==0:
#                 stack.append(stack.pop()*2)
#                 cnt=1
#             elif len(stack)!=0 and arr[j][i]!=0:
#                 stack.append(arr[j][i])
#                 cnt=0
#             elif arr[j][i]!=0:
#                 stack.append(arr[j][i])
#         new[i]=stack+[0]*(N-len(stack))
#     return [list(elem) for elem in zip(*new)]
# def two(arr):
#     for i in range(N):
#         stack=[]
#         cnt=0
#         for j in range(N-1,-1,-1):
#             if len(stack)!=0 and stack[-1]==arr[i][j] and cnt==0:
#                 stack.append(stack.pop()*2)
#                 cnt=1
#             elif len(stack)!=0 and arr[i][j]!=0:
#                 stack.append(arr[i][j])
#                 cnt=0
#             elif arr[i][j]!=0:
#                 stack.append(arr[i][j])
#         arr[i]=[0]*(N-len(stack))+stack[::-1]
#     return arr
# def four(arr):
#     new=[0]*N
#     for i in range(N):
#         stack=[]
#         cnt=0
#         for j in range(N-1,-1,-1):
#             if len(stack)!=0 and stack[-1]==arr[j][i] and cnt==0:
#                 stack.append(stack.pop()*2)
#                 cnt=1
#             elif len(stack)!=0 and arr[j][i]!=0:
#                 stack.append(arr[j][i])
#                 cnt=0
#             elif arr[j][i]!=0:
#                 stack.append(arr[j][i])
#         new[i]=[0]*(N-len(stack))+stack[::-1]
#     return [list(elem) for elem in zip(*new)]
# def recur(i,arr):
#     global max_block
#     if i==5:
#         for k in arr:
#             for l in k:
#                 max_block=max(l,max_block)
#         return
#     for j in range(1,5):
#         temp=deepcopy(arr)
#         idx[i]=j
#         if j==1:
#             recur(i+1,one(arr))
#         elif j==2:
#             recur(i+1,two(arr))
#         elif j==3:
#             recur(i+1,three(arr))
#         else:
#             recur(i+1,four(arr))
#         arr=temp
# N=int(input())
# arr=[list(map(int,input().split())) for _ in range(N)]
# temp=deepcopy(arr)
# idx=[0]*5
# max_block=0
# recur(0,arr)
# print(max_block)
# # pprint.pprint(temp)
# # pprint.pprint(one(temp))
# # temp=deepcopy(arr)
# # pprint.pprint(two(temp))
# # temp=deepcopy(arr)
# # pprint.pprint(three(temp))
# # temp=deepcopy(arr)
# # pprint.pprint(four(temp))
# # temp=deepcopy(arr)