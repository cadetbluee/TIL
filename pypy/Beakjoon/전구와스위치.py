import sys
sys.stdin=open('2138_input.txt')

N=int(input())
status=list(input())
result=list(input())
origin = status[:]  # 원본 저장

case1 = origin[:]   # 0번 안 누른 경우
case2 = origin[:]   # 0번 누른 경우
first0=0
first1=0
def flip(arr, idx):
    for d in [-1,0,1]:
        ni = idx + d
        if 0 <= ni < N:
            arr[ni] = '1' if arr[ni] == '0' else '0'
for i in range(1,N):
    
    if case1[i-1]!=result[i-1]:
        flip(case1,i)
        first0+=1

flip(case2,0)
first1+=1
for i in range(1,N):
    if case2[i-1]!=result[i-1]:
        flip(case2,i)
        first1+=1
if case1==result and case2==result:
    print(min(first0,first1))
elif case2==result:
    print(first1)
elif case1==result:
    print(first0)
else:
    print(-1)
# print(first0)



# # 인덱스 0을 뒤집냐 안뒤집냐 두가지 가능성
# visited=[0]*(N+1)
# visited[0]=1
# def recur(idx,cost):
#     # print(idx)
#     if idx==N:
#         if status==end:
#             print(cost)
#         return
#     if visited[idx+1]==0:
#         visited[idx+1]=1
#         recur(idx+1,cost)
#         for d in dirs:
#             ni=idx+d
#             if 0<=ni<N:
#                 if status[ni]=='0':
#                     status[ni]='1'
#                 else:
#                     status[ni]='0'
#         recur(idx+1,cost+1)
# recur(0,0)