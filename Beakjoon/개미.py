w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
# x,y=1,1
# cnt=1
# while cnt<=t:
#     np=p+x
#     nq=q+y
#     if 0<=np<=w and 0<=nq<=h:
#         p,q=np,nq
#         cnt+=1

#         # print(f'({np},{nq})')
#     elif np<=w and nq>h:
#         y=-1
#     elif nq<=h and np>w:
#         x=-1
#     elif nq>w and nq>h:
#         x,y=-1,-1
#     elif np<0 and 0<=nq:
#         x=1
#     elif nq<0 and 0<=np:
#         y=1
#     else:
#         x,y=1,1
# print(p,q)
if ((t+p)//w)%2==0 and ((t+q)//h)%2==0:
    print((t+p)%w,(t+q)%h)
elif ((t+p)//w)%2==1 and ((t+q)//h)%2==0:
    print(w-(t+p)%w,(t+q)%h)
elif ((t+p)//w)%2==0 and ((t+q)//h)%2==1:
    print((t+p)%w,h-(t+q)%h)
else:
    print(w-(t+p)%w,h-(t+q)%h)