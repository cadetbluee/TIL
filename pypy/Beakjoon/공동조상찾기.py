import sys
sys.stdin=open("3584_input.txt")

# cnt=0
# def pre_order(T,tar1,tar2):
#     global cnt
#     if T==tar1 or T==tar2:
#         cnt+=1
#     elif cnt==2:
#         return
#     if len(tree[T])>0:
#         print(T,end=' ')
#         pre_order(tree.pop(T))


T=int(input().strip())
for _ in range(T):
    N=int(input().strip())
    par=[0]*(N+1)
    for i in range(N-1):
        p,c=map(int,(input().strip()).split())
        par[c]=p
    
    node1,node2=map(int,(input().strip()).split())
    c=node1
    node1_lst=[c]
    while par[c]!=0:
     
        c=par[c] #부모를 새로운 자식으로 두고
        node1_lst.append(c)
    c=node2
    node2_lst=[c]
    while par[c]!=0:
        
        c=par[c] #부모를 새로운 자식으로 두고
        node2_lst.append(c)
    
    result=[]
    for i in node1_lst:
        for j in node2_lst:
            if i==j:
                result.append(i)
                break
        if len(result)>0:
            break
    print(*result)
    
    
    
    
    # pre_order(root,node1,node2)