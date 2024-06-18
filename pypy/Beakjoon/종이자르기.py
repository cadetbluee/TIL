import sys
sys.stdin=open("2628_input.txt")
J,I=map(int,input().split())
J=[0,J]
I=[0,I]
I_list=[]
J_list=[]
N=int(input())
I_cut=[]
J_cut=[]
for i in range(N):
    x,j=map(int,input().split())
    if x==0:
        I_cut.append(j)
    else:
        J_cut.append(j)
I_cut=sorted(I_cut)
J_cut=sorted(J_cut)

if len(I_cut)==0:
    I_cut.append(0)
if len(J_cut)==0:
    J_cut.append(0)
    
for i in I_cut:
    # if (i-I[0])==max(i-I[0] ,I[1]-i):
    #     I=[I[0],i] 
        
    # else:
    #     I=[i,I[1]]
    if len(I_list)>0:
        I_list.pop()
    I_list.append(i-I[0])
    I_list.append(I[1]-i)
    I=[i,I[1]]
    
for j in J_cut:
    # if j-J[0]==max(j-J[0] ,J[1]-j):
    #     J=[J[0],j]
    #     J_list.append(J[1]-j)
    # else:
    #     J=[j,J[1]]
    #     J_list.append(j-J[0])
    if len(J_list)>0:
        J_list.pop()
    J_list.append(j-J[0])
    J_list.append(J[1]-j)
    J=[j,J[1]]   
print(I_list,J_list)
print(max(I_list)*max(J_list))