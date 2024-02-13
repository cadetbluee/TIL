import sys
sys.stdin=open("11478_input.txt")
N_str=input()
N=len(N_str)
print(N)
result=0
N_sub=set()
# for i in range(1<<N):
#     sub_str=[]
#     for j in range(N):
#         if i&(1<<j):
#             print(j,end=' ')
#             sub_str.append(N_str[j])
#     print(sorted(sub_str))
#     sub_str=sorted(sub_str)
#     a=''
#     for i in sub_str:
#         a+=i
#     # print(sub_str)
#     N_sub.add(a)
for i in range(N+1):
    for j in range(N+1):
        N_sub.add(N_str[i:j])
print(len(N_sub)-1)