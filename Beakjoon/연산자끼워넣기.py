# def max_num(i,N,s):
#     global max_re
#     if i==N-1:
#         if max_re<s:
#             max_re=s
#         return
#     for j in range(N-1):
#         if j not in idx[:i]:
#             idx[i]=j
#             if arr[idx[i]]==1:
#                 max_num(i+1,N,s+A[i+1])
#             elif arr[idx[i]]==2:
#                 max_num(i+1,N,s-A[i+1])
#             elif arr[idx[i]]==3:
#                 max_num(i+1,N,s*A[i+1])
#             elif arr[idx[i]]==4:
#                 if s<0:
#                     max_num(i+1,N,-(-s//A[i+1]))
#                 else:
#                     max_num(i+1,N,s//A[i+1])
# def min_num(i,N,s):
#     global min_re
#     if i==N-1:
#         if min_re>s:
#             min_re=s
#         return
#     elif s>min_re:
#         return
#     for j in range(N-1):
#         if j not in idx[:i]:
#             idx[i]=j
#             if arr[idx[i]]==1:
#                 min_num(i+1,N,s+A[i+1])
#             elif arr[idx[i]]==2:
#                 min_num(i+1,N,s-A[i+1])
#             elif arr[idx[i]]==3:
#                 min_num(i+1,N,s*A[i+1])
#             elif arr[idx[i]]==4:
#                 if s<0:
#                     min_num(i+1,N,-(-s//A[i+1]))
#                 else:
#                     min_num(i+1,N,s//A[i+1])
# N=int(input())
# A=list(map(int,input().split()))
# add,mi,mul,div=map(int,input().split())
# arr=[1]*add+[2]*mi+[3]*mul+[4]*div
# print(arr)
# idx=[0]*(add+mi+mul+div)
# max_re=-1e9
# min_re=1e9
# max_num(0,N,A[0])
# min_num(0,N,A[0])
# print(int(max_re))
# print(int(min_re))
def max_min_num(i, N, s, max_dp, min_dp, max_re, min_re):
    if i == N - 1:
        if max_re < s:
            max_re = s
        if min_re > s:
            min_re = s
        return max_re, min_re

    for j in range(N - 1):
        if j not in idx[:i]:
            idx[i] = j
            if arr[idx[i]] == 1:
                max_val, min_val = max_min_num(i + 1, N, s + A[i + 1], max_dp, min_dp, max_re, min_re)
            elif arr[idx[i]] == 2:
                max_val, min_val = max_min_num(i + 1, N, s - A[i + 1], max_dp, min_dp, max_re, min_re)
            elif arr[idx[i]] == 3:
                max_val, min_val = max_min_num(i + 1, N, s * A[i + 1], max_dp, min_dp, max_re, min_re)
            elif arr[idx[i]] == 4:
                if s < 0:
                    max_val, min_val = max_min_num(i + 1, N, -(-s // A[i + 1]), max_dp, min_dp, max_re, min_re)
                else:
                    max_val, min_val = max_min_num(i + 1, N, s // A[i + 1], max_dp, min_dp, max_re, min_re)
            max_re = max(max_re, max_val)
            min_re = min(min_re, min_val)
    return max_re, min_re

N = int(input())
A = list(map(int, input().split()))
add, mi, mul, div = map(int, input().split())
arr = [1] * add + [2] * mi + [3] * mul + [4] * div
idx = [0] * (add + mi + mul + div)
max_re = -1e9
min_re = 1e9
max_dp = [[-1] * (N + 1) for _ in range(N + 1)]
min_dp = [[-1] * (N + 1) for _ in range(N + 1)]

max_result, min_result = max_min_num(0, N, A[0], max_dp, min_dp, max_re, min_re)
print(int(max_re))
print(int(min_re))

#똑똑이 채영이! B 형 따 자 !