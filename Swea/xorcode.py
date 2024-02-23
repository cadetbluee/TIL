KEY=1004

def encode_decode(num):
    return num^KEY
print(encode_decode(1000))
print(encode_decode(4))

for i in range(6):
    print(bin(1<<i),1<<i)
# N,M=map(int,input().split())
# for i in bin(M)[len(bin(M))-1:len(bin(M))-N-1:-1]:
#
#     if i!='1':
#         print('OFF')
#         break
# else:
#     print('ON')
print([int(x/4) for x in [12,8,8,4]])