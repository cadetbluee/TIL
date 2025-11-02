N,M=input().split()
N=N[::-1]
M=M[::-1]
if N>M:
    print(N)
else:
    print(M)
# if N[2]>M[2]:
#     print(N)
# elif M[2]>N[2]:
#     print(M)
# else:
#     if N[1]>M[1]:
#         print(N)
#     elif M[1]>N[1]:
#         print(M)
#     else:
#         if N[0]>M[0]:
#             print(N)
#         elif M[0]>N[0]:
#             print(M)