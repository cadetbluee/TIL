import sys
sys.stdin=open("19879_input.txt")


def dfs(i,V):
    visited=[0]*(V+1)
    st=[]
    visited[i]=1
    print(i,end='-')
    cnt=1
    while True:
        for w in adjl[i]:
            if visited[w]==0:
                st.append(i)
                i=w
                visited[i]=1
                if cnt==(V-1):
                    print(i,end='')
                else:
                    print(i, end='-')
                    cnt+=1
                break
        else:
            if st:
                i=st.pop()
            else:
                break
    return


T = 1
for test_case in range(1, T + 1):
    V,E=map(int,input().split())
    p_list=list(map(int,input().split()))
    adjl=[[] for _ in range(V+1)]
    for i in range(E):
        n1,n2=p_list[2*i],p_list[2*i+1]
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    print(f'#{test_case}',end=' ')
    dfs(1,V)
